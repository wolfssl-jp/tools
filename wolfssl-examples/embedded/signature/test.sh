#!/bin/bash



#  
#   Usage : ./test "GCC_OPTION"
#   
#   Example : ./test "-DWOLFSSL_SMALL_STACK"
#   
#  Output : RSA and ECC results　stored in results.txt
#
#  # Output format : CSV format
#  
#       ,   benchmark,  stack,   heap 
#   tfm,    $,          $,      $
#   sp_c32, $,          $,      $
#   sp_c64, $,          $,      $
# sp_arm64  $bench,     $stack, $heap
# sp_x86_64 $,          $,      $
# 
#
#  $ ->  (result) | Error | None
#  delimiter : conmma and one space
# 
# Exit status :
# Build Error -> 5
# Execute Error -> 6





echo "Init:"
echo "  Please Make Sure WOLFROOT is set in Makefile of each directory"
echo ""

#  User specified Options being given to Compiler
#  set default Option and receive extra Options
option=""
option+=$1
echo "Options : ${option}" | tee results.txt
echo "" | tee -a results.txt


# Initialize variables to "Error"
export bench
export stack
export heap
InitVariables(){
    bench="Error";
    stack="Error";
    heap="Error"
}

# Execute and store result to the variables. if not exist then error
ExecuteRSA(){
    # Execute program and output an Error whenever error occur.
    if ! ./verify >/dev/null 2>&1;  then 
        echo -n "  [-] ERROR in Executing verify in RSA " >&2
        return 5
    fi
#Each command in a pipeline is executed in its own subshell (see Command Execution Environment) - Bash Reference Manual.
# This means We cannot give to read command from a pipeline.
    if ! ./verify_bench | grep "Cycles/sec" | awk '{ print $7 }' > tmp.txt ;  then 
        echo -n "  [-] ERROR in Executing verify_bench in RSA " >&2
        bench="Error"
        return 5
    else 
        read bench < tmp.txt;
    fi
        # Extract the  stack size
    if ! ./verify_mem 2>&1 | grep "stack" | awk '{ print $4 }' > tmp.txt ;    then 
        echo -n "  [-] ERROR in Executing verify_mem in RSA " >&2
        stack="Error"
        return  5
    else 
        read stack < tmp.txt;
    fi
         # Extract the heap peak bytes
    if ! ./verify_mem 2>&1 | grep "peak" | awk '{ print $4 }' > tmp.txt ;   then 
        echo -n "  [-] ERROR in Executing verify_mem in RSA " >&2
        heap="Error"
        return 5
    else 
        read heap < tmp.txt
    fi
}


ExecuteECC(){
     #Execute program and output Error whenever error occur.
    if ! ./ecc_sign_verify >/dev/null 2>&1;  then 
        echo -n "  [-] ERROR in Executing ecc_sign_verify" >&2
        return 5
    fi

    if ! ./ecc_sign_verify_bench | grep "256" | awk '{ print $5 }'  > tmp.txt ;  then 
        echo -n "  [-] ERROR in Executing ecc_sign_verify_bench">&2
        bench="Error"
        return 5
    else 
        read bench < tmp.txt;
    fi
        # Take stack size
    if ! ./ecc_sign_verify_mem 2>&1 | grep "stack" | awk '{ print $4 }' > tmp.txt ;    then 
        echo -n "  [-] ERROR in Executing ecc_sign_verify_mem" >&2
        stack="Error"
        return 5
    else 
        read stack < tmp.txt;
    fi
         # Take heap peak
    if ! ./ecc_sign_verify_mem 2>&1 | grep "peak" | awk '{ print $4 }' > tmp.txt ;   then 
        echo -n "  [-] ERROR in Executing ecc_sign_verify_mem" >&2 
        heap="Error"
        return 5
    else 
        read heap < tmp.txt
    fi
}



#### Main ####


echo "Test:"

# RSA
cd rsa_vfy_only
echo "- RSA Signature" >> ../results.txt
echo "   , bench, stack, heap" >> ../results.txt

InitVariables
if ! make math=tfm EX_CFLAGS="-DBENCH_TIME_SEC=0.3 ${option}" > output.txt 2>&1; then
        echo "  [-] BUILD ERROR! in rsa_vfy_only tfm " >&2
        echo "Error Message  :"
        cat output.txt
        rm output.txt
        exit 5
elif ! ExecuteRSA; then  
        # already printed "[-] Error in Executing verify_mem in RSA " if error 
        echo "with TFM"
        exit 6 
fi
echo "  [*] PASS:  RSA with TFM"
echo "tfm, $bench, $stack, $heap" >> ../results.txt

# RSA with sp_c32
InitVariables
if ! make math=sp arch=c32 EX_CFLAGS="-DBENCH_TIME_SEC=0.3 ${option}" > output.txt 2>&1; then
        echo "  [-] BUILD ERROR! in rsa_vfy_only sp_c32 " >&2
        echo "Error Message  :"
        cat output.txt
        rm output.txt
        exit 5 
elif ! ExecuteRSA; then 
        echo "with sp_c32"
        exit 6 
fi
echo "  [*] PASS:  RSA with sp_c32"
echo "sp_c32, $bench, $stack, $heap" >> ../results.txt

# RSA with sp_c64
InitVariables
if ! make math=sp arch=c64 EX_CFLAGS="-DBENCH_TIME_SEC=0.3 ${option}" > output.txt 2>&1; then
        echo "  [-] BUILD ERROR! in rsa_vfy_only sp_c64 " >&2
        echo "Error Message  :"
        cat output.txt
        rm output.txt
        exit 5 
elif ! ExecuteRSA; then 
    echo "with sp_c64"
    exit 6
    
fi
echo "  [*] PASS:  RSA with sp_c64"
echo "sp_c64, $bench, $stack, $heap" >>  ../results.txt


# RSA with sp_arm64
InitVariables
# Don't exit here if build fails
if ! make math=sp arch=arm64 EX_CFLAGS="-DBENCH_TIME_SEC=0.5 ${option}" >/dev/null 2>&1; then
        # echo "  [-] BUILD ERROR! in rsa_vfy_only sp_arm64 " >&2
        echo "  [+] SKIP:  RSA with sp_arm64"
        bench="None"
        stack="None"
        heap="None"

# IF successfully passed build with sp_arm64
else       
    if ! ExecuteRSA; then 
        echo "with sp_arm64"
        exit 6
    # IF successfully passed build and executing
    else
        echo "  [*] PASS:  RSA with sp_arm64"
    fi
fi

echo "sp_arm64, $bench, $stack, $heap" >>  ../results.txt


# RSA with sp_x86_64
InitVariables
# Don't exit here if build fails
if ! make math=sp arch=x64 EX_CFLAGS="-DBENCH_TIME_SEC=0.5 ${option}" >/dev/null 2>&1; then
        # echo "  [-] BUILD ERROR! in rsa_vfy_only sp_x86_64 " >&2
        echo "  [+] SKIP:  RSA with sp_x86_64"
        bench="None"
        stack="None"
        heap="None"

# IF successfully passed build with sp_x86_64
else       
    if ! ExecuteRSA; then 
        echo "with sp_x86_64"
        exit 6
    # IF successfully passed build and executing
    else
        echo "  [*] PASS:  RSA with sp_x86_64"
    fi
fi

echo "sp_x86_64, $bench, $stack, $heap" >>  ../results.txt

rm tmp.txt output.txt
cd ..

# ECC
cd ecc-sign-verify
echo "" >> ../results.txt
echo "- ECC Signature" >> ../results.txt
echo "   , bench, stack, heap" >> ../results.txt

# ECC with TFM
InitVariables
if ! make math=tfm EX_CFLAGS="-DBENCH_TIME_SEC=0.1 ${option}" > output.txt 2>&1; then
        echo "  [-] BUILD ERROR! in ecc-sign-verify tfm " >&2
        echo "Error Message  :"
        cat output.txt
        rm output.txt
        exit 5
elif ! ExecuteECC; then  
        # already printed "[-] Error in Executing verify_mem in RSA " if error 
        echo "with TFM"
        exit 6 
fi
echo "  [*] PASS:  ECC with TFM"
echo "tfm, $bench, $stack, $heap" >> ../results.txt

# ECC with sp_c32
InitVariables
if ! make math=sp arch=c32 EX_CFLAGS="-DBENCH_TIME_SEC=0.1 ${option}" > output.txt 2>&1; then
        echo "  [-] BUILD ERROR! in ecc-sign-verify sp_c32 " >&2
        echo "Error Message  :"
        cat output.txt
        rm output.txt
        exit 5 
elif ! ExecuteECC; then 
        echo "with sp_c32"
        exit 6 
fi
echo "  [*] PASS:  ECC with sp_c32"
echo "sp_c32, $bench, $stack, $heap" >> ../results.txt

# ECC with sp_c64
InitVariables
if ! make math=sp arch=c64 EX_CFLAGS="-DBENCH_TIME_SEC=0.1 ${option}" > output.txt 2>&1; then
        echo "  [-] BUILD ERROR! in ecc-sign-verify sp_c64 " >&2
        echo "Error Message  :"
        cat output.txt
        rm output.txt
        exit 5 
elif ! ExecuteECC; then 
    echo "with sp_c64"
    exit 6
    
fi
echo "  [*] PASS:  ECC with sp_c64"
echo "sp_c64, $bench, $stack, $heap" >>  ../results.txt


# ECC with sp_arm64
InitVariables
# Don't exit here if build fails
if ! make math=sp arch=arm64 EX_CFLAGS="-DBENCH_TIME_SEC=0.2 ${option}" >/dev/null 2>&1; then
        # echo "  [-] BUILD ERROR! in rsa_vfy_only sp_arm64 " >&2
        echo "  [+] SKIP:  ECC with sp_arm64"
        bench="None"
        stack="None"
        heap="None"

# IF successfully passed build with sp_arm64
else       
    if ! ExecuteECC; then 
        echo "with sp_arm64"
        exit 6
    # IF successfully passed build and executing
    else
        echo "  [*] PASS:  ECC with sp_arm64"
    fi
fi

echo "sp_arm64, $bench, $stack, $heap" >>  ../results.txt


# ECC with sp_x86_64
InitVariables
# Don't exit here if build fails
if ! make math=sp arch=x64 EX_CFLAGS="-DBENCH_TIME_SEC=0.2 ${option}" >/dev/null 2>&1; then
        # echo "  [-] BUILD ERROR! in rsa_vfy_only sp_x86_64 " >&2
        echo "  [+] SKIP:  ECC with sp_x86_64"
        bench="None"
        stack="None"
        heap="None"

# IF successfully passed build with sp_x86_64
else       
    if ! ExecuteECC; then 
        echo "with sp_x86_64"
        exit 6
    # IF successfully passed build and executing
    else
        echo "  [*] PASS:  ECC with sp_x86_64"
    fi
fi

echo "sp_x86_64, $bench, $stack, $heap" >>  ../results.txt

rm tmp.txt output.txt
cd ..

echo ""
echo "Successfully Passed Tests! (see results.txt)"
# cat results.txt
