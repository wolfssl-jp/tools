#!/bin/bash

rsync -a --exclude include.am $1/src/* $2/src
rsync -a --exclude include.am --exclude selftest.c $1/wolfcrypt/src/* $2/wolfcrypt/src
rsync -a --exclude include.am $1/wolfcrypt/test/* $2/wolfcrypt/test
rsync -a --exclude include.am $1/wolfcrypt/benchmark/* $2/wolfcrypt/benchmark
rsync -a --exclude include.am --exclude selftest.h $1/wolfssl/* $2/wolfssl
rsync -a --exclude include.am $1/tests/* $2/tests
rsync -a --exclude include.am $1/scripts/* $2/scripts
rsync -a --exclude include.am $1/examples/* $2/examples
rsync -a --exclude include.am $1/certs/* $2/certs
