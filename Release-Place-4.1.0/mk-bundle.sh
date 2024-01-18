#!/bin/bash

set -e

RELEASE_BUNDLE=/path/to/Release/bundle/dir
LICENSE_REPLACE=/path/to/license_replace/license.pl
echo $#
if [ "$#" -ne 7 ]; then
    echo "Error: Number of Args"
    echo "Usage:"
    echo "./mk-bundle.sh <SSL version> <Crypt version> <Base bundle> <Dir name> <Release bundle> <Dir name> <password>"
    exit 1
fi

SSL_Ver=$1
CRYPT_Ver=$2
BASE=$3
BASE_DIR=$4
REL=$5
REL_DIR=$6
REL_PASSWD=$7


if test -d base-version
then
    rm -rf base-version/*
else
    mkdir base-version
fi
if test -d Release
then
    rm -rf Release/*
else
    mkdir Release
fi
if test -d wolfssl
then
    echo Use wolfssl repo
else
    git clone https://github.com/wolfssl-jp/wolfssl wolfssl
fi
if test -d wolfcrypt
then
    echo Use wolfcrypt repo
else
    git clone https://github.com/wolfssl-jp/wolfssl wolfcrypt
fi

echo ======== Unziping Base Bundle under Release dir ======== 
if test -f  "$RELEASE_BUNDLE/$BASE.7z"
then
    cp "$RELEASE_BUNDLE/$BASE.7z" ./base-version/
else
    echo "$RELEASE_BUNDLE/$BASE.7z" does not exist
fi

if test -d Release/$BASE_DIR
then
    rm -rf Release/$BASE_DIR
fi
cp base-version/$BASE.7z ./Release; cd Release; 
7z x $BASE.7z
cd ..; ls -l ./Release
if test -d "./Release/$REL_DIR"; then
    rm -r ./Release/$REL_DIR
fi
echo mv ./Release/$BASE_DIR ./Release/$REL_DIR
mv ./Release/$BASE_DIR ./Release/$REL_DIR

echo SSL Version:   $1
echo CRYTO Version: $2
echo Base Bundle:   $3, Dir Name: $4
echo Release Bundle:$5, Dir Name: $6, Password:$7

echo 
echo ======== Checking out SSL ============ 
cd ./wolfssl; git checkout $SSL_Ver; cd ..

echo 
echo ======== Checking out Cryto ========== 
cd ./wolfcrypt; git checkout $CRYPT_Ver; cd ..

echo 
echo ======== Copy SSL to Release Dir and Overwrite Crypt ==========
if test -d ./Release/merged
then
    rm -rf ./Release/merged/*
fi
    mkdir -p ./Release/merged
cp -r ./wolfssl/* ./Release/merged

./cp-crypt.sh ./wolfcrypt ./Release/merged

cd ./Release/merged
echo ./autogen.sh
./autogen.sh >> ./log.txt
echo ./configure  --enable-selftest
./configure  --enable-selftest >> ./log.txt

#make check
make clean
make dist
tar xf wolfssl-*.tar.gz
rm wolfssl-*.tar.gz
if test -d "../merged2"; then
    rm -rf ../merged2
fi
mkdir ../merged2
mv wolfssl-?.*.* ../merged2
cd ../..

echo 
echo ======== Commercial License =======
perl $LICENSE_REPLACE ./Release/merged2 wolfssl commercial > /dev/null
echo 
echo ======== Copy new version to Base Bundle under Release dir ======== 
./cp-new.sh ./Release/merged2/wolfssl-4.1.0 ./Release/$REL_DIR

echo 
echo ======== Set Configure version $SSL_Ver =======
sed "s/XXXXXX/$SSL_Ver/g" ./configure-template > ./Release/$REL_DIR/configure

echo 
echo ======== Zipping Relase Bundle ========
pwd
chmod 755 ./Release/$REL_DIR/configure ./Release/$REL_DIR/build-aux/*
if test -d ./Release/$REL/.vscode
then
rm -r ./Release/$REL/.vscode
fi
if test -f ./Release/$REL.7z
then
    rm ./Release/$REL.7z
fi
if test -f ./Release/$REL-$REL_PASSWD.7z
then
    rm ./Release/$REL-$REL_PASSWD.7z
fi
7z a -p$REL_PASSWD ./Release/$REL.7z ./Release/$REL_DIR 
7z a -p$REL_PASSWD ./Release/$REL-$REL_PASSWD.7z ./Release/$REL_DIR 

echo 
echo ======== Relase Bundle Completed ========
echo CHECK BUNDLE SIZE
ls -l ./Release/$REL*.7z