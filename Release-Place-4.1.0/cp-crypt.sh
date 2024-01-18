#!/bin/bash
set -e
cp $1/wolfcrypt/src/dh.c     $2/wolfcrypt/src/dh.c
cp $1/wolfcrypt/src/ecc.c    $2/wolfcrypt/src/ecc.c
cp $1/wolfcrypt/src/rsa.c    $2/wolfcrypt/src/rsa.c
cp $1/wolfcrypt/src/dsa.c    $2/wolfcrypt/src/dsa.c
cp $1/wolfcrypt/src/aes.c    $2/wolfcrypt/src/aes.c
cp $1/wolfcrypt/src/aes_asm.? $2/wolfcrypt/src/aes_asm.S
cp $1/wolfcrypt/src/aes_asm.asm $2/wolfcrypt/src/aes_asm.asm
cp $1/wolfcrypt/src/sha.c    $2/wolfcrypt/src/sha.c
cp $1/wolfcrypt/src/sha256.c $2/wolfcrypt/src/sha256.c
cp $1/wolfcrypt/src/sha512.c $2/wolfcrypt/src/sha512.c
cp $1/wolfcrypt/src/hmac.c   $2/wolfcrypt/src/hmac.c
cp $1/wolfcrypt/src/random.c   $2/wolfcrypt/src/random.c
cp $1/wolfssl/wolfcrypt/dh.h     $2/wolfssl/wolfcrypt/dh.h
cp $1/wolfssl/wolfcrypt/ecc.h    $2/wolfssl/wolfcrypt/ecc.h
cp $1/wolfssl/wolfcrypt/rsa.h    $2/wolfssl/wolfcrypt/rsa.h
cp $1/wolfssl/wolfcrypt/dsa.h    $2/wolfssl/wolfcrypt/dsa.h
cp $1/wolfssl/wolfcrypt/aes.h    $2/wolfssl/wolfcrypt/aes.h
cp $1/wolfssl/wolfcrypt/sha.h    $2/wolfssl/wolfcrypt/sha.h
cp $1/wolfssl/wolfcrypt/sha256.h $2/wolfssl/wolfcrypt/sha256.h
cp $1/wolfssl/wolfcrypt/sha512.h $2/wolfssl/wolfcrypt/sha512.h
cp $1/wolfssl/wolfcrypt/hmac.h   $2/wolfssl/wolfcrypt/hmac.h
cp $1/wolfssl/wolfcrypt/random.h   $2/wolfssl/wolfcrypt/random.h

