### `--disable-option-checking`

ignore unrecognized --enable/--with options 

### `--enable-option-checking`

 

### `--disable-FEATURE`

do not include FEATURE (same as --enable-FEATURE=no) 

### `--enable-FEATURE`

include FEATURE [ARG=yes] 

### `--enable-maintainer-mode`

enable make rules and dependencies not useful (and sometimes confusing) to the casual installer 

### `--disable-maintainer-mode`

 

### `--enable-dependency-tracking`

do not reject slow dependency extractors 

### `--disable-dependency-tracking`

speeds up one-time build 

### `--enable-silent-rules`

less verbose build output (undo: "make V=1") 

### `--disable-silent-rules`

verbose build output (undo: "make V=0") 

### `--enable-static`

build static libraries [default=no] 

### `--disable-static`

 

### `--enable-shared`

build shared libraries [default=yes] 

### `--disable-shared`

 

#### Enables
- `WOLFSSL_TEST_STATIC_BUILD`

### `--enable-fast-install`

optimize for fast installation [default=yes] 

### `--disable-fast-install`

 

### `--disable-libtool-lock`

avoid locking (might break parallel builds) 

### `--enable-libtool-lock`

 

### `--enable-experimental`

(default: disabled) 

#### Enables
- `WOLFSSL_EXPERIMENTAL_SETTINGS`

### `--disable-experimental`

 

### `--enable-threadlocal`

Enable thread local support (default: enabled) 

### `--disable-threadlocal`

 

#### Removes
- `HAVE_THREAD_LS`
- `ERROR_QUEUE_PER_THREAD`

### `--enable-debug`

Add debug code/turns off optimizations (yes|no) [default=no] 

#### Enables
- `DEBUG_WOLFSSL`

### `--disable-debug`

 

### `--enable-debug-code-points`

Include source file and line number in 

#### Enables
- `WOLFSSL_DEBUG_CODEPOINTS`

### `--disable-debug-code-points`

 

### `--enable-verbose`

messages. 

### `--disable-verbose`

 

### `--enable-debug-trace-errcodes`

Print trace messages when library errors are thrown. 

#### Enables
- `WOLFSSL_DEBUG_TRACE_ERROR_CODES`

### `--disable-debug-trace-errcodes`

 

### `--enable-harden-tls`

Enable requirements from RFC9325. Possible values are <yes>, <112>, or <128>. <yes> is equivalent to <112>. (default: disabled) 

#### Enables
- `WOLFSSL_HARDEN_TLS`
- `WOLFSSL_EXTRA_ALERTS`
- `WOLFSSL_CHECK_ALERT_ON_ERR`

### `--disable-harden-tls`

 

### `--enable-32bit`

Enables 32-bit support (default: disabled) 

### `--disable-32bit`

 

### `--enable-16bit`

Enables 16-bit support (default: disabled) 

#### Enables
- `WC_16BIT_CPU`

#### Removes
- `WOLFSSL_SHA512`
- `WOLFSSL_SHA384`

### `--disable-16bit`

 

### `--enable-64bit`

Enables 64-bit support (default: disabled) 

### `--disable-64bit`

 

### `--enable-kdf`

Enables kdf support (default: enabled) 

### `--disable-kdf`

 

### `--enable-hmac`

Enables HMAC support (default: enabled) 

### `--disable-hmac`

 

#### Enables
- `NO_HMAC`

### `--enable-do178`

Enable DO-178, Will NOT work w/o DO178 license (default: disabled) 

#### Enables
- `HAVE_DO178`

#### Removes
- `NO_DO178`

### `--disable-do178`

 

### `--enable-asm`

Enables option for assembly (default: enabled) 

### `--disable-asm`

 

#### Enables
- `WOLFSSL_NO_ASM`
- `TFM_NO_ASM`
- `NO_CHACHA_ASM`

#### Removes
- `WOLFSSL_AARCH64_BUILD`
- `WOLFSSL_SP_ARM64`
- `WOLFSSL_SP_MATH_ALL`

### `--enable-fips`

Enable FIPS 140-2, Will NOT work w/o FIPS license (default: disabled) 

#### Enables
- `NO_CHACHA_ASM`
- `TFM_NO_ASM`
- `WOLFSSL_NO_ASM`

#### Removes
- `WOLFSSL_SP_ARM64`
- `WOLFSSL_SP_MATH_ALL`
- `WOLFSSL_AARCH64_BUILD`

### `--disable-fips`

 

### `--enable-wolfprovider`

Enable wolfProvider options (default: disabled) 

#### Enables
- `HAVE_BLAKE2B`
- `HAVE_ECC_SECPR2`
- `HAVE_CURVE25519`
- `WOLFSSL_PSS_SALT_LEN_DISCOVER`
- `HAVE_ECC_KOBLITZ`
- `WOLFCRYPT_HAVE_SAKKE`
- `WOLFSSL_RIPEMD`
- `HAVE_ECC_ENCRYPT`
- `HAVE_ANON`
- `ASN_BER_TO_DER`
- `WOLFSSL_HAVE_SP_DH`
- `WOLFSSL_SP_ARM64_ASM`
- `WOLFSSL_BASE16`
- `WOLFSSL_ECDSA_DETERMINISTIC_K_VARIANT`
- `NO_OLD_WC_NAMES`
- `WC_RSA_NO_PADDING`
- `WOLFCRYPT_HAVE_SRP`
- `HAVE_COMP_KEY`
- `WOLFSSL_AES_CBC_LENGTH_CHECKS`
- `WOLFSSL_CUSTOM_CURVES`
- `HAVE_OCSP`
- `SESSION_CERTS`
- `HAVE_SCRYPT`
- `HAVE_CURVE448`
- `HAVE_CERTIFICATE_STATUS_REQUEST`
- `HAVE_TRUNCATED_HMAC`
- `WOLFSSL_ARMASM_CRYPTO_SHA512`
- `NO_OLD_SSL_NAMES`
- `WOLFSSL_NO_HASH_RAW`
- `WOLFSSL_ED25519_STREAMING_VERIFY`
- `HAVE_PUBLIC_FFDHE`
- `HAVE_WOLFPROVIDER`
- `WOLFSSL_AES_XTS`
- `WOLFSSL_CMAC`
- `WOLFSSL_HAVE_SP_RSA`
- `HAVE_X963_KDF`
- `MAX_ECC_BITS`
- `WOLFSSL_AESGCM_STREAM`
- `RSA_MAX_SIZE`
- `NO_OLD_SHA_NAMES`
- `HAVE_CAMELLIA`
- `WOLFSSL_ALLOW_RC4`
- `HAVE_ECC_BRAINPOOL`
- `HAVE_BLAKE2`
- `WOLFSSL_SP_4096`
- `WOLFSSL_AES_OFB`
- `WOLFSSL_HAVE_ISSUER_NAMES`
- `HAVE_AES_DECRYPT`
- `WOLFSSL_WOLFSSH`
- `WOLFSSL_PUBLIC_MP`
- `HAVE_OPENSSL_CMD`
- `HAVE_ECC521`
- `WOLF_CRYPTO_CB`
- `WOLFSSL_KEY_GEN`
- `WOLFSSL_HASH_FLAGS`
- `HAVE_FFDHE_8192`
- `WOLFSSL_MD2`
- `NO_OLD_MD5_NAME`
- `HAVE_ALPN`
- `HAVE_ED448`
- `WOLFSSL_CERT_REQ`
- `HAVE_ECC_CDH`
- `HAVE_NULL_CIPHER`
- `HAVE_MAX_FRAGMENT`
- `HAVE_CRL`
- `WOLFSSL_SP_LARGE_CODE`
- `WOLFSSL_SIPHASH`
- `WOLFSSL_CERT_EXT`
- `WOLFSSL_DH_EXTRA`
- `HAVE_TRUSTED_CA`
- `HAVE_BLAKE2S`
- `HAVE_PKCS7`
- `WOLFSSL_ARMASM`
- `HAVE_ECC384`
- `WOLFSSL_CERT_GEN`
- `WOLFSSL_BASE64_ENCODE`
- `KEEP_PEER_CERT`
- `HAVE_AESCCM`
- `HAVE_CERTIFICATE_STATUS_REQUEST_V2`
- `WOLFSSL_HAVE_SP_ECC`
- `HAVE_ED25519`
- `WC_SRTP_KDF`
- `WOLFSSL_SP_521`
- `WOLFSSL_ASN_ALL`
- `WOLFSSL_AES_SIV`
- `HAVE_PK_CALLBACKS`
- `WOLFSSL_SP_1024`
- `FP_ECC`
- `WOLFSSL_ALT_NAMES`
- `WOLFSSL_DES_ECB`
- `HAVE_XCHACHA`
- `WOLFCRYPT_HAVE_ECCSI`
- `WOLFSSL_SP_ASM`
- `WOLFSSL_SP_384`
- `HAVE_FFDHE_6144`
- `HAVE_ECC_SECPR3`
- `WOLFSSL_AES_EAX`
- `HAVE_AES_ECB`
- `ATOMIC_USER`
- `OPENSSL_COEXIST`
- `WOLFSSL_TLS_OCSP_MULTI`
- `HAVE_FFDHE_3072`
- `WOLFSSL_ARMASM_CRYPTO_SHA3`
- `WOLFSSL_ENCRYPTED_KEYS`
- `WOLFSSL_SHAKE256`
- `WOLFSSL_AES_COUNTER`
- `WOLFSSL_ED448_STREAMING_VERIFY`
- `WOLFSSL_AES_DIRECT`
- `WOLFSSL_SHAKE128`
- `WOLFSSL_SEP`
- `HAVE_AES_KEYWRAP`
- `WOLFSSL_AES_CFB`

#### Removes
- `NO_DES3`
- `NO_MD4`
- `NO_PSK`
- `NO_RC4`
- `WOLFSSL_NO_SHAKE128`
- `WOLFSSL_NO_SHAKE256`
- `NO_DSA`

### `--disable-wolfprovider`

 

### `--enable-engine`

Enable wolfEngine options (default: disabled) 

### `--disable-engine`

 

### `--enable-reproducible-build`

Enable maximally reproducible build (default: disabled) 

#### Enables
- `HAVE_REPRODUCIBLE_BUILD`

#### Removes
- `HAVE_WC_INTROSPECTION`

### `--disable-reproducible-build`

 

### `--enable-benchmark`

Build benchmark when building crypttests (default: enabled) 

### `--disable-benchmark`

 

### `--enable-linuxkm`

Enable Linux Kernel Module (default: disabled) 

### `--disable-linuxkm`

 

### `--enable-linuxkm-defaults`

Enable feature defaults for Linux Kernel Module (default: disabled) 

#### Enables
- `WOLFSSL_DH_CONST`
- `WOLFSSL_SP_MOD_WORD_RP`
- `WOLFSSL_TEST_SUBROUTINE`
- `WOLFSSL_SMALL_STACK`
- `WOLFSSL_SP_DIV_WORD_HALF`
- `WOLFSSL_SP_DIV_64`
- `WOLFSSL_OLD_PRIME_CHECK`
- `WOLFSSL_SMALL_STACK_STATIC`

### `--disable-linuxkm-defaults`

 

### `--enable-linuxkm-pie`

Enable relocatable object build of Linux kernel module (default: disabled) 

#### Enables
- `HAVE_LINUXKM_PIE_SUPPORT`

### `--disable-linuxkm-pie`

 

### `--enable-linuxkm-benchmarks`

Enable crypto benchmarking autorun at module load time for Linux kernel module (default: disabled) 

#### Enables
- `WOLFSSL_LINUXKM_BENCHMARKS`

### `--disable-linuxkm-benchmarks`

 

### `--enable-sp`

Enable Single Precision maths implementation (default: disabled) 

#### Enables
- `WOLFSSL_HAVE_SP_RSA`
- `WOLFSSL_SP_384`
- `HAVE_ECC384`
- `WOLFSSL_HAVE_SP_DH`
- `WOLFSSL_HAVE_SP_ECC`
- `HAVE_ECC521`
- `WOLFSSL_SP_521`
- `WOLFSSL_SP_LARGE_CODE`
- `WOLFSSL_SP_4096`

### `--disable-sp`

 

### `--enable-sp-math-all`

Enable Single Precision math implementation for full algorithm suite (default: enabled) 

### `--disable-sp-math-all`

 

#### Enables
- `NO_BIG_INT`

#### Removes
- `WOLFSSL_AARCH64_BUILD`
- `WOLFSSL_SP_ARM64`
- `WOLFSSL_SP_MATH_ALL`

### `--enable-sp-math`

Enable Single Precision math implementation with restricted algorithm suite (default: disabled) 

#### Enables
- `WOLFSSL_SP_4096`
- `WOLFSSL_SP_ASM`
- `WOLFSSL_HAVE_SP_DH`
- `WOLFSSL_SP_384`
- `WOLFSSL_SP_521`
- `NO_BIG_INT`
- `HAVE_ECC521`
- `WOLFSSL_HAVE_SP_RSA`
- `WOLFSSL_HAVE_SP_ECC`
- `WOLFSSL_SP_LARGE_CODE`
- `WOLFSSL_SP_ARM64_ASM`
- `HAVE_ECC384`
- `WOLFSSL_SP_MATH`

#### Removes
- `WOLFSSL_AARCH64_BUILD`
- `WOLFSSL_SP_MATH_ALL`
- `WOLFSSL_SP_ARM64`

### `--disable-sp-math`

 

### `--enable-sp-asm`

Enable Single Precision assembly implementation (default: enabled on x86_64/aarch64/amd64) 

#### Enables
- `HAVE_ECC521`
- `WOLFSSL_HAVE_SP_ECC`
- `WOLFSSL_SP_521`
- `WOLFSSL_HAVE_SP_DH`
- `HAVE_ECC384`
- `WOLFSSL_SP_ARM64_ASM`
- `WOLFSSL_SP_384`
- `WOLFSSL_HAVE_SP_RSA`
- `WOLFSSL_SP_LARGE_CODE`
- `WOLFSSL_SP_ASM`
- `WOLFSSL_SP_4096`

### `--disable-sp-asm`

 

### `--enable-fastmath`

Enable legacy Tom's Fast Math back end (default: disabled) 

#### Enables
- `USE_FAST_MATH`

#### Removes
- `WOLFSSL_SP_ARM64`
- `WOLFSSL_SP_MATH_ALL`

### `--disable-fastmath`

 

### `--enable-fasthugemath`

Enable legacy Tom's Fast Math + huge code (default: disabled) 

#### Enables
- `TFM_SMALL_SET`
- `TFM_HUGE_SET`
- `USE_FAST_MATH`

#### Removes
- `WOLFSSL_SP_MATH_ALL`
- `WOLFSSL_SP_ARM64`

### `--disable-fasthugemath`

 

### `--enable-leanpsk`

Enable Lean PSK build (default: disabled) 

#### Enables
- `WOLFSSL_LEANPSK`
- `NO_ERROR_STRINGS`
- `NO_CERTS`
- `NO_DH`
- `NO_FILESYSTEM`
- `ED25519_SMALL`
- `NO_SHA`
- `RSA_LOW_MEM`
- `HAVE_NULL_CIPHER`
- `NO_DEV_RANDOM`
- `NO_MD5`
- `USE_SLOW_SHA512`
- `NO_WRITEV`
- `USE_SLOW_SHA256`
- `USE_SLOW_SHA`
- `NO_ASN_CRYPT`
- `NO_ASN`
- `WOLFSSL_NO_ASYNC_IO`
- `GCM_SMALL`
- `NO_PWDBASED`
- `SINGLE_THREADED`
- `NO_RSA`
- `WOLFSSL_AES_NO_UNROLL`
- `WOLFSSL_AES_SMALL_TABLES`
- `NO_SESSION_CACHE`
- `WOLFSSL_USER_IO`
- `NO_CODING`
- `WOLFSSL_SMALL_CERT_VERIFY`
- `WOLFSSL_STATIC_PSK`
- `CURVE25519_SMALL`
- `NO_AES`
- `NO_PKCS12`

#### Removes
- `HAVE_FFDHE_2048`
- `WC_RSA_PSS`
- `WOLFSSL_TLS13`
- `WOLFSSL_PSS_LONG_SALT`
- `HAVE_SUPPORTED_CURVES`
- `NO_PSK`
- `WOLFSSL_SHA512`
- `HAVE_SERVER_RENEGOTIATION_INFO`
- `HAVE_CHACHA`
- `HAVE_ECC`
- `HAVE_WC_INTROSPECTION`
- `GCM_TABLE_4BIT`
- `WOLFSSL_ASN_TEMPLATE`
- `TFM_ECC256`
- `WOLFSSL_SYS_CA_CERTS`
- `HAVE_DH_DEFAULT_PARAMS`
- `HAVE_POLY1305`
- `ECC_SHAMIR`
- `WOLFSSL_SHA384`
- `HAVE_AESGCM`

### `--disable-leanpsk`

 

### `--enable-asn`

Enable ASN (default: enabled) 

### `--disable-asn`

 

### `--enable-heapmath`

Enable heap based integer.c math ops (default: disabled) 

#### Enables
- `USE_INTEGER_HEAP_MATH`

#### Removes
- `WOLFSSL_AARCH64_BUILD`
- `WOLFSSL_SP_MATH_ALL`
- `WOLFSSL_SP_ARM64`

### `--disable-heapmath`

 

### `--enable-all`

Enable all wolfSSL features, except SSLv3 (default: disabled) 

#### Enables
- `HAVE_ECC_SECPR3`
- `WOLFSSL_AES_XTS`
- `WOLFSSL_ASN_ALL`
- `WOLFSSL_NO_HASH_RAW`
- `WOLFSSL_TRUST_PEER_CERT`
- `WOLFSSL_DTLS`
- `HAVE_CRL_IO`
- `WOLFSSL_ASIO`
- `WOLFSSL_TLS_OCSP_MULTI`
- `WOLFSSL_AES_OFB`
- `HAVE_OCSP`
- `HAVE_CRL_MONITOR`
- `WOLFSSL_NGINX`
- `WOLFSSL_AESGCM_STREAM`
- `WOLFCRYPT_HAVE_SRP`
- `HAVE_PK_CALLBACKS`
- `WOLFSSL_AES_CFB`
- `WOLFSSL_IP_ALT_NAME`
- `WOLFSSL_PRIORITIZE_PSK`
- `HAVE_ECC384`
- `HAVE_BLAKE2`
- `OPENSSL_EXTRA`
- `HAVE_ECC_BRAINPOOL`
- `WOLFSSL_SHAKE256`
- `WOLFSSL_OPENVPN`
- `HAVE_EXT_CACHE`
- `HAVE_X963_KDF`
- `WOLFSSL_ALWAYS_KEEP_SNI`
- `ATOMIC_USER`
- `WOLFSSL_SRTP`
- `RSA_MAX_SIZE`
- `HAVE_NULL_CIPHER`
- `WOLFSSL_AES_DIRECT`
- `WOLFSSL_KEY_GEN`
- `HAVE_BLAKE2S`
- `OPENSSL_ALL`
- `WOLFSSL_ECDSA_DETERMINISTIC_K_VARIANT`
- `HAVE_ANON`
- `WOLFSSL_FPKI`
- `WOLFSSL_DH_EXTRA`
- `WOLFSSL_SIGNER_DER_CERT`
- `WOLFSSL_ARMASM_CRYPTO_SHA3`
- `HAVE_AES_KEYWRAP`
- `WOLFSSL_SP_ARM64_ASM`
- `HAVE_IO_TIMEOUT`
- `WOLFSSL_SP_1024`
- `WOLFSSL_AES_SIV`
- `WOLFSSL_SP_384`
- `NO_SESSION_CACHE_REF`
- `HAVE_XCHACHA`
- `HAVE_ED25519`
- `HAVE_BLAKE2B`
- `SSL_TXT_TLSV1_2`
- `WOLFSSL_VERBOSE_ERRORS`
- `WOLFSSL_SIPHASH`
- `OPENSSL_NO_EC`
- `HAVE_RPK`
- `WOLFSSL_ALWAYS_VERIFY_CB`
- `FORTRESS`
- `HAVE_SMIME`
- `NO_OLD_SHA_NAMES`
- `WOLFSSL_HASH_FLAGS`
- `WOLFSSL_CERT_EXT`
- `WOLFSSL_AES_EAX`
- `WOLFSSL_ALT_CERT_CHAINS`
- `WOLFSSL_SEP`
- `HAVE_SCRYPT`
- `NO_OLD_RNGNAME`
- `HAVE_ALPN`
- `HAVE_TRUSTED_CA`
- `HAVE_MAX_FRAGMENT`
- `ASN_BER_TO_DER`
- `WOLFSSL_POST_HANDSHAKE_AUTH`
- `KEEP_OUR_CERT`
- `HAVE_STUNNEL`
- `HAVE_OPENSSL_CMD`
- `WOLFSSL_DER_LOAD`
- `WOLFSSL_CHECK_ALERT_ON_ERR`
- `WOLFSSL_CERT_GEN`
- `HAVE_ECH`
- `BOOST_ASIO_USE_WOLFSSL`
- `HAVE_PKCS7`
- `WOLFSSL_CERT_REQ`
- `NO_OLD_SSL_NAMES`
- `WOLFSSL_EITHER_SIDE`
- `WOLFSSL_ALLOW_RC4`
- `HAVE_LIGHTY`
- `WOLFSSL_QUIC`
- `WOLFSSL_HAVE_CERT_SERVICE`
- `WOLFSSL_TICKET_NONCE_MALLOC`
- `NO_OLD_MD5_NAME`
- `WOLFSSL_CERT_NAME_ALL`
- `HAVE_HPKE`
- `HAVE_CERTIFICATE_STATUS_REQUEST_V2`
- `WOLFSSL_SUBJ_DIR_ATTR`
- `WOLFCRYPT_HAVE_SAKKE`
- `HAVE_CAMELLIA`
- `WOLFSSL_NO_OCSP_ISSUER_CHECK`
- `HAVE_CURVE448`
- `WOLFSSL_EARLY_DATA`
- `PERSIST_CERT_CACHE`
- `HAVE_ECC_SECPR2`
- `HAVE_ECC_ENCRYPT`
- `WOLFSSL_RIPEMD`
- `FP_MAX_BITS`
- `HAVE_CRL`
- `WOLFSSL_WOLFSSH`
- `PERSIST_SESSION_CACHE`
- `WOLFSSL_MD2`
- `WOLFSSL_CMAC`
- `WOLFSSL_ARMASM_CRYPTO_SHA512`
- `WOLFSSL_HAVE_SP_RSA`
- `SP_INT_BITS`
- `WOLFSSL_ALT_NAMES`
- `WOLFSSL_MULTICAST`
- `WOLFSSL_BASE16`
- `HAVE_FFDHE_3072`
- `WOLFSSL_SP_LARGE_CODE`
- `WOLFSSL_AES_CBC_LENGTH_CHECKS`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_LIBWEBSOCKETS`
- `WOLFSSL_BASE64_ENCODE`
- `HAVE_AESCCM`
- `ASIO_USE_WOLFSSL`
- `WOLFSSL_SEND_HRR_COOKIE`
- `HAVE_ECC_KOBLITZ`
- `WOLFSSL_CUSTOM_CURVES`
- `WOLFSSL_HAVE_SP_ECC`
- `HAVE_EX_DATA`
- `WOLFSSL_SUBJ_INFO_ACC`
- `WOLFSSL_HAVE_ISSUER_NAMES`
- `WOLFSSL_AES_COUNTER`
- `WOLFSSL_SHAKE128`
- `WOLFSSL_HAVE_SP_DH`
- `HAVE_ECC521`
- `SESSION_CERTS`
- `WOLFSSL_HAVE_WOLFSCEP`
- `HAVE_COMP_KEY`
- `HAVE_WEBSERVER`
- `WOLFSSL_ED25519_STREAMING_VERIFY`
- `WOLFSSL_QT`
- `WOLFSSL_OPENSSH`
- `HAVE_AES_DECRYPT`
- `HAVE_ED448`
- `HAVE_CERTIFICATE_STATUS_REQUEST`
- `HAVE_WOLFSSL_SSL_H`
- `HAVE_SESSION_TICKET`
- `WC_SRTP_KDF`
- `HAVE_FALLBACK_SCSV`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `HAVE_ECC_CDH`
- `WOLFSSL_SP_4096`
- `KEEP_PEER_CERT`
- `OPENSSL_COMPATIBLE_DEFAULTS`
- `HAVE_CURVE25519`
- `HAVE_TRUNCATED_HMAC`
- `WOLFSSL_PUBLIC_MP`
- `WOLFSSL_ENCRYPTED_KEYS`
- `WOLFSSL_SP_521`
- `WOLFSSL_TLS13_NO_PEEK_HANDSHAKE_DONE`
- `WOLF_CRYPTO_CB`
- `HAVE_KEYING_MATERIAL`
- `OPENSSL_NO_SSL3`
- `NO_OLD_WC_NAMES`
- `WC_RSA_NO_PADDING`
- `HAVE_AES_ECB`
- `OPENSSL_NO_SSL2`
- `WOLFSSL_SP_ASM`
- `WOLFSSL_ED448_STREAMING_VERIFY`
- `WOLFSSL_DES_ECB`
- `WOLFCRYPT_HAVE_ECCSI`
- `WOLFSSL_ARMASM`
- `FP_ECC`

#### Removes
- `NO_PSK`
- `WOLFSSL_NO_SHAKE256`
- `NO_RC4`
- `NO_MD4`
- `NO_DES3`
- `HAVE_DH_DEFAULT_PARAMS`
- `NO_DSA`
- `WOLFSSL_NO_SHAKE128`

### `--disable-all`

 

### `--enable-all-osp`

Enable all OSP meta feature sets (default: disabled) 

#### Enables
- `WOLFSSL_BASE16`
- `WOLFSSL_NO_OCSP_ISSUER_CHECK`
- `WOLFSSL_AES_COUNTER`
- `NO_OLD_SHA_NAMES`
- `WOLFSSL_ALT_CERT_CHAINS`
- `HAVE_ECC_SECPR3`
- `OPENSSL_EXTRA`
- `HAVE_ALPN`
- `WOLFSSL_CERT_GEN`
- `HAVE_ED25519`
- `WOLFSSL_TLS13_NO_PEEK_HANDSHAKE_DONE`
- `FORTRESS`
- `SESSION_CERTS`
- `NO_SESSION_CACHE_REF`
- `WOLFSSL_IP_ALT_NAME`
- `HAVE_OCSP`
- `HAVE_TRUSTED_CA`
- `OPENSSL_NO_COMP`
- `WOLFSSL_TICKET_NONCE_MALLOC`
- `HAVE_AES_KEYWRAP`
- `OPENSSL_NO_SSL2`
- `HAVE_PKCS7`
- `HAVE_SMIME`
- `WOLFSSL_PUBLIC_MP`
- `NO_OLD_SSL_NAMES`
- `WOLFSSL_CHECK_ALERT_ON_ERR`
- `HAVE_MAX_FRAGMENT`
- `OPENSSL_NO_SSL3`
- `HAVE_CERTIFICATE_STATUS_REQUEST`
- `WOLFSSL_ASIO`
- `WOLFSSL_TICKET_HAVE_ID`
- `HAVE_OPENSSL_CMD`
- `WOLFSSL_LIBWEBSOCKETS`
- `WOLFSSL_PRIORITIZE_PSK`
- `NO_OLD_RNGNAME`
- `WOLFSSL_ALLOW_RC4`
- `SINGLE_THREADED`
- `HAVE_WOLFSSL_SSL_H`
- `WOLFSSL_ALLOW_TLSV10`
- `HAVE_LIGHTY`
- `OPENSSL_NO_EC`
- `WOLFSSL_ALWAYS_VERIFY_CB`
- `WOLFSSL_WOLFSSH`
- `WC_RSA_NO_PADDING`
- `ASIO_USE_WOLFSSL`
- `WOLFSSL_ALLOW_SSLV3`
- `WOLFSSL_OPENSSH`
- `WOLFSSL_CUSTOM_CURVES`
- `HAVE_CRL`
- `WOLFSSL_CERT_NAME_ALL`
- `HAVE_SESSION_TICKET`
- `HAVE_ECC_BRAINPOOL`
- `HAVE_EXT_CACHE`
- `HAVE_COMP_KEY`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `HAVE_CURVE25519`
- `WOLFSSL_KEY_GEN`
- `WOLFSSL_NGINX`
- `KEEP_OUR_CERT`
- `HAVE_ECC_SECPR2`
- `OPENSSL_ALL`
- `KEEP_PEER_CERT`
- `WOLFSSL_ALWAYS_KEEP_SNI`
- `NO_OLD_WC_NAMES`
- `WOLFSSL_SIGNER_DER_CERT`
- `HAVE_KEYING_MATERIAL`
- `BOOST_ASIO_USE_WOLFSSL`
- `HAVE_X963_KDF`
- `WOLFSSL_DER_LOAD`
- `SSL_TXT_TLSV1_2`
- `WOLFSSL_OPENVPN`
- `OPENSSL_COMPATIBLE_DEFAULTS`
- `HAVE_WEBSERVER`
- `WOLFSSL_EITHER_SIDE`
- `WOLFSSL_RIPEMD`
- `WOLFSSL_TRUST_PEER_CERT`
- `WOLFSSL_AES_DIRECT`
- `WOLFSSL_ENCRYPTED_KEYS`
- `WOLFSSL_CERT_EXT`
- `HAVE_EX_DATA`
- `NO_OLD_MD5_NAME`
- `HAVE_STUNNEL`
- `HAVE_CERTIFICATE_STATUS_REQUEST_V2`
- `HAVE_TRUNCATED_HMAC`
- `WOLFSSL_DES_ECB`
- `WOLFSSL_QT`
- `HAVE_ANON`
- `HAVE_ECC_KOBLITZ`

#### Removes
- `HAVE_DH_DEFAULT_PARAMS`
- `NO_PSK`
- `NO_DSA`
- `NO_MD4`
- `NO_RC4`
- `NO_DES3`

### `--disable-all-osp`

 

### `--enable-all-asm`

Enable all applicable assembly accelerations (default: disabled) 

#### Enables
- `WOLFSSL_HAVE_SP_DH`
- `WOLFSSL_SP_ASM`
- `WOLFSSL_HAVE_SP_RSA`
- `WOLFSSL_SP_384`
- `WOLFSSL_SP_4096`
- `WOLFSSL_ARMASM_CRYPTO_SHA512`
- `HAVE_ECC521`
- `WOLFSSL_SP_LARGE_CODE`
- `WOLFSSL_NO_HASH_RAW`
- `WOLFSSL_ARMASM_CRYPTO_SHA3`
- `WOLFSSL_SP_ARM64_ASM`
- `WOLFSSL_ARMASM`
- `HAVE_ECC384`
- `WOLFSSL_HAVE_SP_ECC`
- `WOLFSSL_SP_521`

### `--disable-all-asm`

 

### `--enable-all-crypto`

Enable all wolfcrypt algorithms (default: disabled) 

#### Enables
- `WOLFSSL_SIPHASH`
- `HAVE_ECC521`
- `SP_INT_BITS`
- `HAVE_CURVE448`
- `HAVE_ED448`
- `WOLFSSL_KEY_GEN`
- `HAVE_MAX_FRAGMENT`
- `HAVE_CRL`
- `WOLFSSL_WOLFSSH`
- `WOLFSSL_ED448_STREAMING_VERIFY`
- `WOLFSSL_HAVE_ISSUER_NAMES`
- `WOLFSSL_AES_CFB`
- `FP_MAX_BITS`
- `HAVE_CURVE25519`
- `HAVE_ECC_SECPR2`
- `WOLFSSL_ARMASM_CRYPTO_SHA3`
- `WOLFSSL_SP_ASM`
- `WOLFSSL_SP_521`
- `WOLFSSL_PUBLIC_MP`
- `WOLFSSL_AES_EAX`
- `WOLFSSL_ED25519_STREAMING_VERIFY`
- `HAVE_OPENSSL_CMD`
- `HAVE_ECC_ENCRYPT`
- `WOLFSSL_CERT_EXT`
- `WOLFSSL_CUSTOM_CURVES`
- `WOLFSSL_DES_ECB`
- `HAVE_BLAKE2`
- `HAVE_TRUSTED_CA`
- `WOLFSSL_SEP`
- `WOLFSSL_AES_COUNTER`
- `HAVE_XCHACHA`
- `FP_ECC`
- `WOLFSSL_AES_CBC_LENGTH_CHECKS`
- `ATOMIC_USER`
- `WOLFSSL_AESGCM_STREAM`
- `HAVE_ECC_CDH`
- `WOLFSSL_ARMASM_CRYPTO_SHA512`
- `WC_SRTP_KDF`
- `WOLFSSL_SP_384`
- `WOLFSSL_MD2`
- `WOLFSSL_CERT_GEN`
- `HAVE_COMP_KEY`
- `WOLFSSL_AES_SIV`
- `WOLF_CRYPTO_CB`
- `HAVE_NULL_CIPHER`
- `HAVE_CERTIFICATE_STATUS_REQUEST`
- `WOLFSSL_CMAC`
- `HAVE_FFDHE_3072`
- `HAVE_ED25519`
- `WOLFSSL_BASE64_ENCODE`
- `WOLFSSL_TLS_OCSP_MULTI`
- `WOLFSSL_AES_DIRECT`
- `WOLFSSL_ARMASM`
- `HAVE_ECC_BRAINPOOL`
- `HAVE_CERTIFICATE_STATUS_REQUEST_V2`
- `HAVE_BLAKE2B`
- `HAVE_TRUNCATED_HMAC`
- `WOLFSSL_ENCRYPTED_KEYS`
- `WOLFSSL_HASH_FLAGS`
- `HAVE_ALPN`
- `SESSION_CERTS`
- `RSA_MAX_SIZE`
- `HAVE_ECC_SECPR3`
- `WOLFSSL_AES_XTS`
- `WOLFSSL_BASE16`
- `WOLFSSL_ALLOW_RC4`
- `WOLFSSL_SP_4096`
- `WOLFSSL_SHAKE256`
- `WOLFSSL_NO_HASH_RAW`
- `WOLFCRYPT_HAVE_ECCSI`
- `HAVE_X963_KDF`
- `WOLFSSL_SP_LARGE_CODE`
- `WOLFSSL_RIPEMD`
- `HAVE_SCRYPT`
- `WOLFSSL_HAVE_SP_ECC`
- `HAVE_OCSP`
- `HAVE_AES_DECRYPT`
- `WOLFCRYPT_HAVE_SAKKE`
- `ASN_BER_TO_DER`
- `WOLFSSL_CERT_REQ`
- `WOLFSSL_HAVE_SP_DH`
- `WOLFSSL_HAVE_SP_RSA`
- `HAVE_BLAKE2S`
- `HAVE_AES_KEYWRAP`
- `WOLFSSL_SHAKE128`
- `WOLFSSL_ECDSA_DETERMINISTIC_K_VARIANT`
- `HAVE_ECC_KOBLITZ`
- `WOLFSSL_ALT_NAMES`
- `HAVE_CAMELLIA`
- `WOLFSSL_SP_1024`
- `WOLFSSL_AES_OFB`
- `HAVE_ECC384`
- `KEEP_PEER_CERT`
- `HAVE_PK_CALLBACKS`
- `WOLFSSL_ASN_ALL`
- `HAVE_ANON`
- `HAVE_PKCS7`
- `HAVE_AESCCM`
- `WOLFSSL_DH_EXTRA`
- `WOLFSSL_SP_ARM64_ASM`
- `WOLFCRYPT_HAVE_SRP`
- `HAVE_AES_ECB`

#### Removes
- `NO_DES3`
- `NO_MD4`
- `WOLFSSL_NO_SHAKE256`
- `WOLFSSL_NO_SHAKE128`
- `NO_RC4`
- `NO_DSA`
- `NO_PSK`

### `--disable-all-crypto`

 

### `--enable-kyber`

Enable KYBER (requires --enable-experimental) (default: disabled) 

#### Enables
- `WOLFSSL_SHAKE256`
- `WOLFSSL_SHAKE128`
- `WOLFSSL_WC_KYBER`
- `WOLFSSL_HAVE_KYBER`

#### Removes
- `WOLFSSL_NO_SHAKE256`
- `WOLFSSL_NO_SHAKE128`

### `--disable-kyber`

 

### `--enable-dilithium`

Enable DILITHIUM (requires --enable-experimental) (default: disabled) 

#### Enables
- `WOLFSSL_SHAKE128`
- `HAVE_DILITHIUM`
- `WOLFSSL_SHAKE256`
- `WOLFSSL_WC_DILITHIUM`

#### Removes
- `WOLFSSL_NO_SHAKE256`
- `WOLFSSL_NO_SHAKE128`

### `--disable-dilithium`

 

### `--enable-xmss`

Enable stateful XMSS/XMSS^MT signatures (default: disabled) 

#### Enables
- `WOLFSSL_HAVE_XMSS`
- `WOLFSSL_WC_XMSS`

### `--disable-xmss`

 

### `--enable-lms`

Enable stateful LMS/HSS signatures (default: disabled) 

#### Enables
- `WOLFSSL_HAVE_LMS`
- `WOLFSSL_WC_LMS`

### `--disable-lms`

 

### `--enable-singlethreaded`

Enable wolfSSL single threaded (default: disabled) 

#### Enables
- `SINGLE_THREADED`

#### Removes
- `ERROR_QUEUE_PER_THREAD`

### `--disable-singlethreaded`

 

### `--enable-rwlock`

Enable use of rwlock (default: disabled) 

#### Enables
- `WOLFSSL_USE_RWLOCK`

### `--disable-rwlock`

 

### `--enable-cryptonly`

Enable wolfCrypt Only build (default: disabled) 

#### Enables
- `WOLFCRYPT_ONLY`
- `WOLFSSL_NO_TLS12`

#### Removes
- `HAVE_HKDF`
- `WOLFSSL_PSS_LONG_SALT`
- `HAVE_EXTENDED_MASTER`
- `WOLFSSL_TLS13`
- `WC_RSA_PSS`
- `HAVE_SERVER_RENEGOTIATION_INFO`

### `--disable-cryptonly`

 

### `--enable-ech`

Enable ECH (default: disabled) 

#### Enables
- `HAVE_TRUSTED_CA`
- `HAVE_ALPN`
- `HAVE_HPKE`
- `HAVE_MAX_FRAGMENT`
- `HAVE_ECH`
- `HAVE_CURVE25519`
- `HAVE_TRUNCATED_HMAC`

### `--disable-ech`

 

### `--enable-dtls`

Enable wolfSSL DTLS (default: disabled) 

#### Enables
- `WOLFSSL_DTLS`

### `--disable-dtls`

 

### `--enable-dtls-mtu`

Enable setting the MTU size for wolfSSL DTLS (default: disabled) 

#### Enables
- `WOLFSSL_DTLS_MTU`

### `--disable-dtls-mtu`

 

### `--enable-keylog-export`

Enable insecure export of TLS secrets to an NSS keylog file (default: disabled) 

#### Enables
- `WOLFSSL_SSLKEYLOGFILE`
- `SHOW_SECRETS`
- `WOLFSSL_KEYLOG_EXPORT_WARNED`
- `HAVE_SECRET_CALLBACK`

### `--disable-keylog-export`

 

### `--enable-tls13-draft18`

Enable wolfSSL TLS v1.3 Draft 18 (default: disabled) 

### `--disable-tls13-draft18`

 

### `--enable-tls13`

Enable wolfSSL TLS v1.3 (default: enabled) 

### `--disable-tls13`

 

#### Removes
- `WOLFSSL_TLS13`
- `WC_RSA_PSS`
- `HAVE_HKDF`
- `WOLFSSL_PSS_LONG_SALT`

### `--enable-quic`

Enable QUIC API with wolfSSL TLS v1.3 (default: disabled) 

#### Enables
- `HAVE_EX_DATA`
- `OPENSSL_EXTRA`
- `WOLFSSL_ENCRYPTED_KEYS`
- `WOLFSSL_QUIC`
- `WOLFSSL_AES_COUNTER`
- `HAVE_ALPN`
- `WOLFSSL_AES_DIRECT`
- `HAVE_CURVE25519`

### `--disable-quic`

 

### `--enable-postauth`

Enable wolfSSL Post-handshake Authentication (default: disabled) 

#### Enables
- `WOLFSSL_POST_HANDSHAKE_AUTH`

### `--disable-postauth`

 

### `--enable-hrrcookie`

Enable the server to send Cookie Extension in HRR with state (default: disabled) 

#### Enables
- `WOLFSSL_SEND_HRR_COOKIE`

### `--disable-hrrcookie`

 

### `--enable-rng`

Enable compiling and using RNG (default: enabled) 

### `--disable-rng`

 

#### Enables
- `WC_NO_RNG`

#### Removes
- `WC_RSA_BLINDING`

### `--enable-sctp`

Enable wolfSSL DTLS-SCTP support (default: disabled) 

#### Enables
- `WC_NO_RNG`

#### Removes
- `WC_RSA_BLINDING`

### `--disable-sctp`

 

### `--enable-srtp`

Enable wolfSSL DTLS-SRTP support (default: disabled) 

#### Enables
- `WOLFSSL_AES_DIRECT`
- `WC_SRTP_KDF`
- `WOLFSSL_SRTP`
- `HAVE_KEYING_MATERIAL`
- `HAVE_AES_ECB`
- `WOLFSSL_DTLS`

### `--disable-srtp`

 

### `--enable-mcast`

Enable wolfSSL DTLS multicast support (default: disabled) 

#### Enables
- `HAVE_NULL_CIPHER`
- `WOLFSSL_MULTICAST`
- `WOLFSSL_DTLS`

### `--disable-mcast`

 

### `--enable-bind`

Enable Bind DNS compatibility build (default: disabled) 

#### Enables
- `WC_RSA_NO_PADDING`
- `OPENSSL_COMPATIBLE_DEFAULTS`
- `WOLFSSL_DSA_768_MODULUS`
- `WOLFSSL_AES_DIRECT`
- `WOLFSSL_KEY_GEN`
- `HAVE_ALPN`
- `WOLFSSL_DES_ECB`
- `WOLFSSL_CERT_NAME_ALL`
- `OPENSSL_ALL`
- `WOLFSSL_NO_OCSP_ISSUER_CHECK`
- `WOLFSSL_ALT_CERT_CHAINS`
- `WOLFSSL_TRUST_PEER_CERT`
- `WOLFSSL_EITHER_SIDE`
- `WOLFSSL_TLS13_NO_PEEK_HANDSHAKE_DONE`
- `WOLFSSL_BIND`
- `WOLFSSL_CERT_GEN`
- `HAVE_AES_ECB`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `NO_SESSION_CACHE_REF`
- `WOLFSSL_PRIORITIZE_PSK`
- `OPENSSL_EXTRA`
- `HAVE_OPENSSL_CMD`
- `WOLFSSL_CHECK_ALERT_ON_ERR`
- `HAVE_OCSP`
- `WOLFSSL_TICKET_HAVE_ID`
- `HAVE_COMP_KEY`

#### Removes
- `NO_DSA`

### `--disable-bind`

 

### `--enable-libssh2`

Enable libssh2 compatibility build (default: disabled) 

#### Enables
- `WOLFSSL_AES_DIRECT`
- `WOLFSSL_KEY_GEN`
- `OPENSSL_EXTRA`
- `WOLFSSL_AES_COUNTER`

#### Removes
- `NO_DES3`
- `NO_DSA`

### `--disable-libssh2`

 

### `--enable-openssh`

Enable OpenSSH compatibility build (default: disabled) 

#### Enables
- `HAVE_CURVE25519`
- `WOLFSSL_OPENSSH`
- `HAVE_EX_DATA`
- `HAVE_ED25519`
- `WOLFSSL_AES_DIRECT`
- `OPENSSL_EXTRA`
- `WOLFSSL_ALWAYS_VERIFY_CB`
- `WOLFSSL_BASE16`
- `WOLFSSL_KEY_GEN`
- `WOLFSSL_CERT_GEN`
- `FORTRESS`
- `WOLFSSL_DER_LOAD`
- `WOLFSSL_AES_COUNTER`
- `WOLFSSL_RIPEMD`
- `WOLFSSL_ALLOW_RC4`

#### Removes
- `NO_DSA`
- `NO_RC4`
- `NO_DES3`

### `--disable-openssh`

 

### `--enable-openvpn`

Enable OpenVPN compatibility build (default: disabled) 

#### Enables
- `OPENSSL_ALL`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `HAVE_OCSP`
- `WOLFSSL_DES_ECB`
- `HAVE_COMP_KEY`
- `WOLFSSL_EITHER_SIDE`
- `WOLFSSL_CERT_EXT`
- `HAVE_CRL`
- `WC_RSA_NO_PADDING`
- `HAVE_EX_DATA`
- `SESSION_CERTS`
- `OPENSSL_EXTRA`
- `WOLFSSL_CERT_NAME_ALL`
- `WOLFSSL_OPENVPN`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_CERT_GEN`
- `WOLFSSL_KEY_GEN`
- `HAVE_OPENSSL_CMD`
- `WOLFSSL_AES_COUNTER`
- `WOLFSSL_AES_DIRECT`
- `HAVE_KEYING_MATERIAL`

#### Removes
- `NO_DSA`
- `NO_DES3`

### `--disable-openvpn`

 

### `--enable-openresty`

Enable openresty (default: disabled) 

#### Enables
- `HAVE_OPENSSL_CMD`
- `WOLFSSL_NGINX`
- `WC_RSA_NO_PADDING`
- `HAVE_CERTIFICATE_STATUS_REQUEST`
- `OPENSSL_EXTRA`
- `HAVE_ANON`
- `HAVE_COMP_KEY`
- `NO_SESSION_CACHE_REF`
- `WOLFSSL_ALWAYS_KEEP_SNI`
- `WOLFSSL_EITHER_SIDE`
- `HAVE_CERTIFICATE_STATUS_REQUEST_V2`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_PRIORITIZE_PSK`
- `WOLFSSL_TLS13_NO_PEEK_HANDSHAKE_DONE`
- `HAVE_TRUNCATED_HMAC`
- `WOLFSSL_SIGNER_DER_CERT`
- `HAVE_EX_DATA`
- `OPENSSL_COMPATIBLE_DEFAULTS`
- `KEEP_PEER_CERT`
- `SESSION_CERTS`
- `WOLFSSL_ALWAYS_VERIFY_CB`
- `WOLFSSL_ALT_CERT_CHAINS`
- `HAVE_TRUSTED_CA`
- `WOLFSSL_NO_OCSP_ISSUER_CHECK`
- `HAVE_CRL`
- `OPENSSL_ALL`
- `WOLFSSL_CERT_NAME_ALL`
- `WOLFSSL_KEY_GEN`
- `HAVE_MAX_FRAGMENT`
- `HAVE_ALPN`
- `HAVE_EXT_CACHE`
- `KEEP_OUR_CERT`
- `HAVE_OCSP`
- `WOLFSSL_CERT_GEN`
- `WOLFSSL_CHECK_ALERT_ON_ERR`
- `WOLFSSL_TRUST_PEER_CERT`
- `HAVE_SESSION_TICKET`
- `WOLFSSL_ERROR_CODE_OPENSSL`

#### Removes
- `NO_DSA`

### `--disable-openresty`

 

### `--enable-nginx`

Enable nginx (default: disabled) 

#### Enables
- `WOLFSSL_NO_OCSP_ISSUER_CHECK`
- `HAVE_OCSP`
- `WOLFSSL_ALT_CERT_CHAINS`
- `WOLFSSL_KEY_GEN`
- `HAVE_SESSION_TICKET`
- `WOLFSSL_NGINX`
- `HAVE_TRUNCATED_HMAC`
- `WOLFSSL_PRIORITIZE_PSK`
- `HAVE_CERTIFICATE_STATUS_REQUEST_V2`
- `SESSION_CERTS`
- `WOLFSSL_TRUST_PEER_CERT`
- `HAVE_CERTIFICATE_STATUS_REQUEST`
- `HAVE_EXT_CACHE`
- `OPENSSL_EXTRA`
- `NO_SESSION_CACHE_REF`
- `OPENSSL_COMPATIBLE_DEFAULTS`
- `WOLFSSL_ALWAYS_KEEP_SNI`
- `WOLFSSL_TLS13_NO_PEEK_HANDSHAKE_DONE`
- `WOLFSSL_SIGNER_DER_CERT`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `WOLFSSL_ALWAYS_VERIFY_CB`
- `WOLFSSL_CHECK_ALERT_ON_ERR`
- `WOLFSSL_TICKET_HAVE_ID`
- `HAVE_CRL`
- `HAVE_TRUSTED_CA`
- `KEEP_OUR_CERT`
- `HAVE_OPENSSL_CMD`
- `HAVE_EX_DATA`
- `HAVE_ALPN`
- `WOLFSSL_CERT_GEN`
- `HAVE_ANON`
- `KEEP_PEER_CERT`
- `HAVE_MAX_FRAGMENT`

#### Removes
- `NO_DSA`

### `--disable-nginx`

 

### `--enable-chrony`

Enable chrony support (default: disabled) 

#### Enables
- `HAVE_TRUNCATED_HMAC`
- `WOLFSSL_CERT_GEN`
- `WOLFSSL_EITHER_SIDE`
- `HAVE_COMP_KEY`
- `HAVE_OPENSSL_CMD`
- `OPENSSL_ALL`
- `HAVE_ALPN`
- `WOLFSSL_AES_DIRECT`
- `HAVE_KEYING_MATERIAL`
- `OPENSSL_EXTRA`
- `WC_RSA_NO_PADDING`
- `WOLFSSL_CERT_NAME_ALL`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_AES_SIV`
- `WOLFSSL_CMAC`
- `HAVE_MAX_FRAGMENT`
- `HAVE_OCSP`
- `HAVE_TRUSTED_CA`
- `HAVE_ED25519`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `WOLFSSL_AES_COUNTER`
- `WOLFSSL_ALWAYS_KEEP_SNI`

### `--disable-chrony`

 

### `--enable-openldap`

Enable OpenLDAP support (default: disabled) 

#### Enables
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `HAVE_OPENSSL_CMD`
- `HAVE_COMP_KEY`
- `OPENSSL_EXTRA`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_EITHER_SIDE`
- `HAVE_OCSP`
- `WOLFSSL_CERT_NAME_ALL`
- `WOLFSSL_SIGNER_DER_CERT`
- `OPENSSL_ALL`
- `WC_RSA_NO_PADDING`
- `WOLFSSL_CERT_GEN`

### `--disable-openldap`

 

### `--enable-mosquitto`

Enable Mosquitto support (default: disabled) 

#### Enables
- `OPENSSL_EXTRA`
- `HAVE_COMP_KEY`
- `HAVE_CRL`
- `SESSION_CERTS`
- `HAVE_EX_DATA`
- `WOLFSSL_CERT_NAME_ALL`
- `HAVE_CERTIFICATE_STATUS_REQUEST`
- `WOLFSSL_TICKET_HAVE_ID`
- `HAVE_OCSP`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `HAVE_MOSQUITTO`
- `WOLFSSL_EITHER_SIDE`
- `OPENSSL_ALL`
- `WC_RSA_NO_PADDING`
- `HAVE_OPENSSL_CMD`

#### Removes
- `NO_PSK`

### `--disable-mosquitto`

 

### `--enable-lighty`

Enable lighttpd/lighty (default: disabled) 

#### Enables
- `SESSION_CERTS`
- `HAVE_EXT_CACHE`
- `KEEP_PEER_CERT`
- `HAVE_OCSP`
- `WOLFSSL_KEY_GEN`
- `HAVE_ALPN`
- `HAVE_OPENSSL_CMD`
- `OPENSSL_NO_SSL3`
- `HAVE_CERTIFICATE_STATUS_REQUEST_V2`
- `HAVE_SESSION_TICKET`
- `OPENSSL_EXTRA`
- `HAVE_LIGHTY`
- `OPENSSL_ALL`
- `OPENSSL_NO_COMP`
- `KEEP_OUR_CERT`
- `HAVE_TRUSTED_CA`
- `WOLFSSL_ENCRYPTED_KEYS`
- `SINGLE_THREADED`
- `HAVE_MAX_FRAGMENT`
- `HAVE_CERTIFICATE_STATUS_REQUEST`
- `OPENSSL_NO_SSL2`
- `WOLFSSL_ALWAYS_KEEP_SNI`
- `HAVE_EX_DATA`
- `HAVE_CRL`
- `WOLFSSL_CERT_GEN`
- `HAVE_WOLFSSL_SSL_H`
- `HAVE_TRUNCATED_HMAC`
- `WOLFSSL_ALWAYS_VERIFY_CB`

### `--disable-lighty`

 

### `--enable-rsyslog`

Enable rsyslog (default: disabled) 

#### Enables
- `WOLFSSL_RSYSLOG`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `WOLFSSL_CERT_NAME_ALL`
- `HAVE_OPENSSL_CMD`
- `WOLFSSL_EITHER_SIDE`
- `HAVE_COMP_KEY`
- `WOLFSSL_CHECK_ALERT_ON_ERR`
- `WOLFSSL_TLS13_NO_PEEK_HANDSHAKE_DONE`
- `WC_RSA_NO_PADDING`
- `WOLFSSL_TRUST_PEER_CERT`
- `OPENSSL_EXTRA`
- `HAVE_ANON`
- `OPENSSL_ALL`
- `WOLFSSL_ALT_CERT_CHAINS`
- `WOLFSSL_PRIORITIZE_PSK`
- `OPENSSL_COMPATIBLE_DEFAULTS`
- `HAVE_EX_DATA`
- `WOLFSSL_NO_OCSP_ISSUER_CHECK`
- `NO_SESSION_CACHE_REF`
- `HAVE_OCSP`

### `--disable-rsyslog`

 

### `--enable-haproxy`

Enable haproxy (default: disabled) 

#### Enables
- `WOLFSSL_ALLOW_SSLV3`
- `HAVE_OPENSSL_CMD`
- `WOLFSSL_PRIORITIZE_PSK`
- `HAVE_MAX_FRAGMENT`
- `HAVE_EXT_CACHE`
- `RSA_MAX_SIZE`
- `WOLFSSL_CHECK_ALERT_ON_ERR`
- `OPENSSL_EXTRA`
- `WOLFSSL_KEY_GEN`
- `KEEP_OUR_CERT`
- `HAVE_ALPN`
- `WOLFSSL_CERT_GEN`
- `WOLFSSL_ALWAYS_VERIFY_CB`
- `KEEP_PEER_CERT`
- `NO_SESSION_CACHE_REF`
- `WC_RSA_NO_PADDING`
- `WOLFSSL_TICKET_HAVE_ID`
- `HAVE_EX_DATA`
- `OPENSSL_COMPATIBLE_DEFAULTS`
- `HAVE_CRL`
- `HAVE_TRUNCATED_HMAC`
- `SESSION_CERTS`
- `WOLFSSL_CERT_REQ`
- `FP_MAX_BITS`
- `WOLFSSL_CERT_NAME_ALL`
- `WOLFSSL_SIGNER_DER_CERT`
- `HAVE_SESSION_TICKET`
- `HAVE_SECURE_RENEGOTIATION`
- `OPENSSL_ALL`
- `HAVE_OCSP`
- `SP_INT_BITS`
- `HAVE_COMP_KEY`
- `WOLFSSL_TLS13_NO_PEEK_HANDSHAKE_DONE`
- `WOLFSSL_NO_OCSP_ISSUER_CHECK`
- `HAVE_ANON`
- `WOLFSSL_TRUST_PEER_CERT`
- `WOLFSSL_EITHER_SIDE`
- `WOLFSSL_HAPROXY`
- `HAVE_CERTIFICATE_STATUS_REQUEST_V2`
- `HAVE_CERTIFICATE_STATUS_REQUEST`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `WOLFSSL_ALT_CERT_CHAINS`
- `WOLFSSL_ALWAYS_KEEP_SNI`
- `HAVE_TRUSTED_CA`

#### Removes
- `NO_OLD_TLS`

### `--disable-haproxy`

 

### `--enable-wpas`

Enable wpa_supplicant support (default: disabled) 

#### Enables
- `WOLFSSL_VALIDATE_ECC_IMPORT`
- `HAVE_COMP_KEY`
- `OPENSSL_COMPATIBLE_DEFAULTS`
- `WOLFSSL_CMAC`
- `WOLFSSL_ALWAYS_KEEP_SNI`
- `WOLFSSL_CHECK_ALERT_ON_ERR`
- `SESSION_CERTS`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_CERT_GEN`
- `WOLFSSL_CERT_EXT`
- `OPENSSL_EXTRA_X509_SMALL`
- `WOLFSSL_PUBLIC_MP`
- `HAVE_SECRET_CALLBACK`
- `HAVE_SESSION_TICKET`
- `WOLFSSL_ALWAYS_VERIFY_CB`
- `HAVE_TRUNCATED_HMAC`
- `WOLFSSL_TLS13_NO_PEEK_HANDSHAKE_DONE`
- `WOLFSSL_WPAS`
- `ATOMIC_USER`
- `OPENSSL_EXTRA`
- `WOLFSSL_ENCRYPTED_KEYS`
- `KEEP_OUR_CERT`
- `HAVE_MAX_FRAGMENT`
- `WOLFSSL_EITHER_SIDE`
- `HAVE_AES_KEYWRAP`
- `WOLFSSL_ALLOW_RC4`
- `KEEP_PEER_CERT`
- `HAVE_CERTIFICATE_STATUS_REQUEST`
- `WC_CTC_NAME_SIZE`
- `HAVE_OCSP`
- `WOLFSSL_DER_LOAD`
- `HAVE_CERTIFICATE_STATUS_REQUEST_V2`
- `WOLFSSL_SIGNER_DER_CERT`
- `WOLFSSL_KEY_GEN`
- `HAVE_EXT_CACHE`
- `NO_SESSION_CACHE_REF`
- `WOLFSSL_AES_DIRECT`
- `WOLFSSL_NO_OCSP_ISSUER_CHECK`
- `HAVE_STUNNEL`
- `HAVE_ANON`
- `WOLFSSL_TRUST_PEER_CERT`
- `WOLFSSL_ALT_CERT_CHAINS`
- `WOLFSSL_PRIORITIZE_PSK`
- `WOLFSSL_DES_ECB`
- `HAVE_EX_DATA`
- `HAVE_KEYING_MATERIAL`
- `WOLFSSL_PUBLIC_ECC_ADD_DBL`
- `HAVE_CRL`

#### Removes
- `NO_DSA`
- `NO_RC4`
- `NO_PSK`
- `NO_MD4`
- `NO_DES3`

### `--disable-wpas`

 

### `--enable-wpas-dpp`

Enable wpa_supplicant support with dpp (default: disabled) 

#### Enables
- `HAVE_ECC_SECPR3`
- `WOLFSSL_CERT_EXT`
- `WOLFSSL_CHECK_ALERT_ON_ERR`
- `HAVE_EXT_CACHE`
- `HAVE_SECRET_CALLBACK`
- `NO_SESSION_CACHE_REF`
- `HAVE_OPENSSL_CMD`
- `WOLFSSL_ALT_CERT_CHAINS`
- `WOLFSSL_AES_DIRECT`
- `OPENSSL_ALL`
- `OPENSSL_EXTRA_X509_SMALL`
- `WOLFSSL_TLS13_NO_PEEK_HANDSHAKE_DONE`
- `WOLFSSL_ENCRYPTED_KEYS`
- `OPENSSL_EXTRA`
- `HAVE_ECC_CDH`
- `WC_CTC_NAME_SIZE`
- `WOLFSSL_CERT_REQ`
- `WOLFSSL_ALWAYS_VERIFY_CB`
- `HAVE_X963_KDF`
- `WOLFSSL_EITHER_SIDE`
- `WOLFSSL_KEY_GEN`
- `WOLFSSL_SIGNER_DER_CERT`
- `WOLFSSL_TRUST_PEER_CERT`
- `HAVE_MAX_FRAGMENT`
- `OPENSSL_COMPATIBLE_DEFAULTS`
- `WOLFSSL_VALIDATE_ECC_IMPORT`
- `WOLFSSL_DES_ECB`
- `HAVE_ECC_KOBLITZ`
- `HAVE_STUNNEL`
- `HAVE_EX_DATA`
- `WOLFSSL_ALLOW_RC4`
- `WOLFSSL_PUBLIC_MP`
- `HAVE_SESSION_TICKET`
- `HAVE_CERTIFICATE_STATUS_REQUEST_V2`
- `HAVE_TRUNCATED_HMAC`
- `WOLFSSL_WPAS`
- `ATOMIC_USER`
- `HAVE_ECC_BRAINPOOL`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_CERT_NAME_ALL`
- `HAVE_ECC_SECPR2`
- `WOLFSSL_NO_OCSP_ISSUER_CHECK`
- `HAVE_AES_KEYWRAP`
- `WOLFSSL_PUBLIC_ECC_ADD_DBL`
- `HAVE_CERTIFICATE_STATUS_REQUEST`
- `KEEP_PEER_CERT`
- `WOLFSSL_DER_LOAD`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `WOLFSSL_ALWAYS_KEEP_SNI`
- `HAVE_ANON`
- `WOLFSSL_PRIORITIZE_PSK`
- `WOLFSSL_CUSTOM_CURVES`
- `SESSION_CERTS`
- `KEEP_OUR_CERT`
- `HAVE_KEYING_MATERIAL`
- `HAVE_PKCS7`
- `HAVE_COMP_KEY`
- `HAVE_OCSP`
- `WC_RSA_NO_PADDING`
- `WOLFSSL_CERT_GEN`
- `HAVE_CRL`
- `WOLFSSL_CMAC`

#### Removes
- `NO_PSK`
- `NO_DSA`
- `NO_RC4`
- `NO_DES3`
- `NO_MD4`

### `--disable-wpas-dpp`

 

### `--enable-ntp`

Enable ntp support (default: disabled) 

#### Enables
- `WOLFSSL_EITHER_SIDE`
- `OPENSSL_EXTRA`
- `WOLFSSL_AES_DIRECT`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `WOLFSSL_TICKET_HAVE_ID`
- `OPENSSL_ALL`
- `WOLFSSL_CERT_NAME_ALL`
- `HAVE_OCSP`
- `WOLFSSL_CMAC`
- `HAVE_COMP_KEY`
- `WOLFSSL_CERT_GEN`
- `WC_RSA_NO_PADDING`
- `WOLFSSL_KEY_GEN`
- `HAVE_OPENSSL_CMD`

#### Removes
- `NO_DSA`

### `--disable-ntp`

 

### `--enable-fortress`

Enable SSL fortress build (default: disabled) 

#### Enables
- `WOLFSSL_ALWAYS_VERIFY_CB`
- `OPENSSL_EXTRA`
- `WOLFSSL_AES_COUNTER`
- `WOLFSSL_DER_LOAD`
- `WOLFSSL_AES_DIRECT`
- `WOLFSSL_KEY_GEN`
- `FORTRESS`

### `--disable-fortress`

 

### `--enable-libwebsockets`

Enable libwebsockets (default: disabled) 

#### Enables
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `HAVE_COMP_KEY`
- `WOLFSSL_TICKET_HAVE_ID`
- `WC_RSA_NO_PADDING`
- `WOLFSSL_LIBWEBSOCKETS`
- `OPENSSL_ALL`
- `HAVE_OPENSSL_CMD`
- `OPENSSL_EXTRA`
- `WOLFSSL_CERT_NAME_ALL`
- `HAVE_EX_DATA`
- `WOLFSSL_EITHER_SIDE`
- `HAVE_OCSP`
- `OPENSSL_NO_EC`

### `--disable-libwebsockets`

 

### `--enable-net-snmp`

Enable net-snmp (default: disabled) 

#### Enables
- `HAVE_OCSP`
- `WOLFSSL_DTLS`
- `HAVE_OPENSSL_CMD`
- `SESSION_CERTS`
- `HAVE_CRL`
- `WOLFSSL_CERT_NAME_ALL`
- `WOLFSSL_AES_CFB`
- `WOLFSSL_EITHER_SIDE`
- `HAVE_COMP_KEY`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `WOLFSSL_TICKET_HAVE_ID`
- `HAVE_EX_DATA`
- `OPENSSL_EXTRA`
- `WC_RSA_NO_PADDING`
- `OPENSSL_ALL`

#### Removes
- `NO_DES3`

### `--disable-net-snmp`

 

### `--enable-krb`

Enable kerberos 5 support (default: disabled) 

#### Enables
- `WOLFSSL_CERT_NAME_ALL`
- `OPENSSL_ALL`
- `HAVE_CRL`
- `WOLFSSL_KRB`
- `HAVE_AES_KEYWRAP`
- `HAVE_COMP_KEY`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `WOLFSSL_DES_ECB`
- `WC_RSA_NO_PADDING`
- `HAVE_PKCS7`
- `WOLFSSL_ALLOW_RC4`
- `WOLFSSL_TICKET_HAVE_ID`
- `HAVE_EX_DATA`
- `WOLFSSL_EITHER_SIDE`
- `HAVE_OPENSSL_CMD`
- `OPENSSL_EXTRA`
- `HAVE_X963_KDF`
- `WOLFSSL_AES_DIRECT`
- `HAVE_OCSP`

#### Removes
- `NO_RC4`
- `NO_MD4`
- `NO_DES3`

### `--disable-krb`

 

### `--enable-ffmpeg`

Enable FFmpeg support (default: disabled) 

#### Enables
- `WOLFSSL_TICKET_HAVE_ID`
- `OPENSSL_EXTRA`
- `WOLFSSL_CHECK_ALERT_ON_ERR`
- `OPENSSL_COMPATIBLE_DEFAULTS`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `WOLFSSL_TLS13_NO_PEEK_HANDSHAKE_DONE`
- `HAVE_COMP_KEY`
- `HAVE_OCSP`
- `WOLFSSL_ALT_CERT_CHAINS`
- `WOLFSSL_CERT_NAME_ALL`
- `HAVE_OPENSSL_CMD`
- `WOLFSSL_NO_OCSP_ISSUER_CHECK`
- `OPENSSL_ALL`
- `WOLFSSL_FFMPEG`
- `WC_RSA_NO_PADDING`
- `NO_SESSION_CACHE_REF`
- `WOLFSSL_TRUST_PEER_CERT`
- `WOLFSSL_EITHER_SIDE`
- `WOLFSSL_PRIORITIZE_PSK`

### `--disable-ffmpeg`

 

### `--enable-ip-alt-name`

Enable IP subject alternative name (default: disabled) 

#### Enables
- `WOLFSSL_IP_ALT_NAME`

### `--disable-ip-alt-name`

 

### `--enable-qt`

Enable qt (default: disabled) 

#### Enables
- `WOLFSSL_CERT_EXT`
- `WOLFSSL_EITHER_SIDE`
- `HAVE_OCSP`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `HAVE_ECC_SECPR2`
- `SESSION_CERTS`
- `WOLFSSL_CERT_NAME_ALL`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_CUSTOM_CURVES`
- `WOLFSSL_QT`
- `WC_RSA_NO_PADDING`
- `NO_OLD_SHA_NAMES`
- `WOLFSSL_ENCRYPTED_KEYS`
- `HAVE_EX_DATA`
- `NO_OLD_MD5_NAME`
- `WOLFSSL_CERT_GEN`
- `WOLFSSL_ALLOW_RC4`
- `OPENSSL_EXTRA`
- `NO_OLD_WC_NAMES`
- `HAVE_ECC_BRAINPOOL`
- `HAVE_OPENSSL_CMD`
- `HAVE_ECC_KOBLITZ`
- `HAVE_ECC_SECPR3`
- `NO_OLD_SSL_NAMES`
- `WOLFSSL_KEY_GEN`
- `WOLFSSL_ALLOW_SSLV3`
- `OPENSSL_NO_SSL2`
- `NO_OLD_RNGNAME`
- `WOLFSSL_ALLOW_TLSV10`
- `OPENSSL_ALL`

#### Removes
- `HAVE_DH_DEFAULT_PARAMS`
- `NO_DSA`
- `NO_DES3`
- `NO_RC4`
- `NO_OLD_TLS`
- `NO_PSK`

### `--disable-qt`

 

### `--enable-bump`

Enable SSL Bump build (default: disabled) 

#### Enables
- `WOLFSSL_MD2`
- `OPENSSL_EXTRA`
- `WOLFSSL_TEST_CERT`
- `SP_INT_BITS`
- `HUGE_SESSION_CACHE`
- `WOLFSSL_ALT_NAMES`
- `WOLFSSL_CERT_GEN`
- `WOLFSSL_DER_LOAD`
- `FP_MAX_BITS`
- `WOLFSSL_KEY_GEN`
- `RSA_MAX_SIZE`
- `LARGE_STATIC_BUFFERS`

### `--disable-bump`

 

### `--enable-sniffer`

Enable wolfSSL sniffer support (default: disabled) 

#### Enables
- `WOLFSSL_DH_EXTRA`
- `WOLFSSL_SNIFFER`
- `WOLFSSL_STATIC_EPHEMERAL`

### `--disable-sniffer`

 

### `--enable-signal`

Enable signal (default: disabled) 

#### Enables
- `OPENSSL_EXTRA`
- `WOLFSSL_AES_DIRECT`
- `HAVE_TRUSTED_CA`
- `WOLFSSL_AES_COUNTER`
- `WOLFSSL_SIGNAL`
- `HAVE_ALPN`
- `WOLFSSL_ENCRYPTED_KEYS`
- `HAVE_MAX_FRAGMENT`
- `HAVE_TRUNCATED_HMAC`

### `--disable-signal`

 

### `--enable-strongswan`

Enable strongSwan support (default: disabled) 

#### Enables
- `OPENSSL_EXTRA`
- `WOLFSSL_LOG_PRINTF`
- `WC_RSA_NO_PADDING`
- `HAVE_OPENSSL_CMD`
- `WOLFSSL_CERT_NAME_ALL`
- `WOLFSSL_EITHER_SIDE`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_CERT_EXT`
- `SESSION_CERTS`
- `WOLFSSL_KEY_GEN`
- `HAVE_CRL`
- `OPENSSL_ALL`
- `WOLFSSL_CERT_REQ`
- `HAVE_EX_DATA`
- `WOLFSSL_DES_ECB`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `HAVE_OCSP`
- `WOLFSSL_CERT_GEN`
- `HAVE_COMP_KEY`
- `WOLFSSL_PUBLIC_MP`
- `WOLFSSL_DTLS`

#### Removes
- `NO_DES3`

### `--disable-strongswan`

 

### `--enable-hitch`

Enable hitch support (default: disabled) 

#### Enables
- `WC_RSA_NO_PADDING`
- `WOLFSSL_KEY_GEN`
- `WOLFSSL_EITHER_SIDE`
- `WOLFSSL_SIGNER_DER_CERT`
- `OPENSSL_EXTRA`
- `OPENSSL_ALL`
- `WOLFSSL_NO_OCSP_ISSUER_CHECK`
- `OPENSSL_COMPATIBLE_DEFAULTS`
- `SESSION_CERTS`
- `WOLFSSL_HITCH`
- `WOLFSSL_PRIORITIZE_PSK`
- `HAVE_ALPN`
- `HAVE_OPENSSL_CMD`
- `WOLFSSL_ENCRYPTED_KEYS`
- `HAVE_EX_DATA`
- `WOLFSSL_TRUST_PEER_CERT`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_CERT_GEN`
- `HAVE_COMP_KEY`
- `HAVE_OCSP`
- `WOLFSSL_ALT_CERT_CHAINS`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `WOLFSSL_CERT_NAME_ALL`
- `WOLFSSL_TLS13_NO_PEEK_HANDSHAKE_DONE`
- `WOLFSSL_CHECK_ALERT_ON_ERR`
- `NO_SESSION_CACHE_REF`
- `WOLFSSL_CIPHER_INTERNALNAME`

### `--disable-hitch`

 

### `--enable-memcached`

Enable memcached support (default: disabled) 

#### Enables
- `HAVE_MEMCACHED`
- `HAVE_EXT_CACHE`
- `WOLFSSL_SESSION_ID_CTX`

### `--disable-memcached`

 

### `--enable-opensslcoexist`

Enable coexistence of wolfssl/openssl (default: disabled) 

#### Enables
- `NO_OLD_SSL_NAMES`
- `NO_OLD_WC_NAMES`
- `NO_OLD_SHA_NAMES`
- `NO_OLD_MD5_NAME`
- `OPENSSL_COEXIST`

### `--disable-opensslcoexist`

 

### `--enable-smime`

Enable S/MIME (default: disabled) 

#### Enables
- `HAVE_SMIME`
- `HAVE_PKCS7`
- `HAVE_OPENSSL_CMD`
- `HAVE_COMP_KEY`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_EITHER_SIDE`
- `WOLFSSL_CERT_NAME_ALL`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `WOLFSSL_AES_DIRECT`
- `HAVE_AES_KEYWRAP`
- `OPENSSL_EXTRA`
- `HAVE_OCSP`
- `WC_RSA_NO_PADDING`
- `HAVE_X963_KDF`
- `OPENSSL_ALL`

### `--disable-smime`

 

### `--enable-psa`

use Platform Security Architecture (PSA) interface (default: disabled) 

#### Enables
- `WOLFSSL_HAVE_PSA`

### `--disable-psa`

 

### `--enable-psa-lib-static`

Link PSA as static library (default: disable) 

### `--disable-psa-lib-static`

 

### `--enable-opensslall`

Enable all OpenSSL API, size++ (default: disabled) 

#### Enables
- `OPENSSL_ALL`
- `OPENSSL_EXTRA`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `WC_RSA_NO_PADDING`
- `HAVE_OPENSSL_CMD`
- `WOLFSSL_TICKET_HAVE_ID`
- `HAVE_COMP_KEY`
- `WOLFSSL_CERT_NAME_ALL`
- `WOLFSSL_EITHER_SIDE`
- `HAVE_OCSP`

### `--disable-opensslall`

 

### `--enable-opensslextra`

Enable extra OpenSSL API, size+ (default: disabled). Skip compat header install using "noinstall" 

#### Enables
- `OPENSSL_EXTRA`
- `WOLFSSL_ENCRYPTED_KEYS`

### `--disable-opensslextra`

 

### `--enable-error-queue-per-thread`

Enable one error queue per thread. Requires thread local storage. (default: disabled) 

### `--disable-error-queue-per-thread`

 

#### Removes
- `ERROR_QUEUE_PER_THREAD`

### `--enable-maxstrength`

Enable Max Strength build, allows TLSv1.2-AEAD-PFS ciphers only (default: disabled) 

#### Enables
- `WOLFSSL_MAX_STRENGTH`
- `WOLFSSL_CIPHER_TEXT_CHECK`

### `--disable-maxstrength`

 

### `--enable-harden`

Enable Hardened build, Enables Timing Resistance and Blinding (default: enabled) 

### `--disable-harden`

 

#### Enables
- `WC_NO_CACHE_RESISTANT`
- `WC_NO_HARDEN`

#### Removes
- `TFM_TIMING_RESISTANT`
- `WC_RSA_BLINDING`
- `ECC_TIMING_RESISTANT`

### `--enable-ipv6`

Enable testing of IPV6 (default: disabled) 

#### Enables
- `TEST_IPV6`
- `WOLFSSL_IPV6`

### `--disable-ipv6`

 

### `--enable-leantls`

Enable Lean TLS build (default: disabled) 

#### Enables
- `ECC_USER_CURVES`
- `ED25519_SMALL`
- `CURVE25519_SMALL`
- `WOLFSSL_LEANTLS`
- `RSA_LOW_MEM`
- `WOLFSSL_AES_SMALL_TABLES`
- `NO_PWDBASED`
- `NO_WOLFSSL_CM_VERIFY`
- `USE_SLOW_SHA256`
- `NO_SHA`
- `NO_RSA`
- `NO_MD5`
- `NO_WRITEV`
- `WOLFSSL_NO_ASYNC_IO`
- `NO_DH`
- `NO_WOLFSSL_MEMORY`
- `USE_SLOW_SHA512`
- `WOLFSSL_SMALL_CERT_VERIFY`
- `NO_SESSION_CACHE`
- `WOLFSSL_AES_NO_UNROLL`
- `USE_SLOW_SHA`
- `NO_WOLFSSL_SERVER`
- `GCM_SMALL`
- `NO_ERROR_STRINGS`

#### Removes
- `HAVE_CHACHA`
- `WOLFSSL_SHA384`
- `HAVE_POLY1305`
- `HAVE_FFDHE_2048`
- `HAVE_WC_INTROSPECTION`
- `WOLFSSL_SHA512`
- `WOLFSSL_PSS_LONG_SALT`
- `HAVE_DH_DEFAULT_PARAMS`
- `ECC_SHAMIR`
- `WC_RSA_PSS`
- `GCM_TABLE_4BIT`

### `--disable-leantls`

 

### `--enable-lowresource`

Enable low resource options for memory/flash (default: disabled) 

#### Enables
- `GCM_SMALL`
- `USE_SLOW_SHA256`
- `WOLFSSL_SMALL_CERT_VERIFY`
- `USE_SLOW_SHA512`
- `USE_SLOW_SHA`
- `WOLFSSL_AES_SMALL_TABLES`
- `RSA_LOW_MEM`
- `ALT_ECC_SIZE`
- `NO_SESSION_CACHE`
- `WOLFSSL_NO_ASYNC_IO`
- `ED25519_SMALL`
- `CURVE25519_SMALL`
- `WOLFSSL_AES_NO_UNROLL`

#### Removes
- `GCM_TABLE_4BIT`
- `HAVE_WC_INTROSPECTION`
- `ECC_SHAMIR`

### `--disable-lowresource`

 

### `--enable-titancache`

Enable titan session cache (default: disabled) 

#### Enables
- `TITAN_SESSION_CACHE`

### `--disable-titancache`

 

### `--enable-hugecache`

Enable huge session cache (default: disabled) 

#### Enables
- `HUGE_SESSION_CACHE`

### `--disable-hugecache`

 

### `--enable-bigcache`

Enable big session cache (default: disabled) 

#### Enables
- `BIG_SESSION_CACHE`

### `--disable-bigcache`

 

### `--enable-smallcache`

Enable small session cache (default: disabled) 

#### Enables
- `SMALL_SESSION_CACHE`

### `--disable-smallcache`

 

### `--enable-savesession`

Enable persistent session cache (default: disabled) 

#### Enables
- `PERSIST_SESSION_CACHE`

### `--disable-savesession`

 

### `--enable-savecert`

Enable persistent cert cache (default: disabled) 

#### Enables
- `PERSIST_CERT_CACHE`

### `--disable-savecert`

 

### `--enable-writedup`

Enable write duplication of WOLFSSL objects (default: disabled) 

#### Enables
- `HAVE_WRITE_DUP`

### `--disable-writedup`

 

### `--enable-atomicuser`

Enable Atomic User Record Layer (default: disabled) 

#### Enables
- `ATOMIC_USER`

### `--disable-atomicuser`

 

### `--enable-pkcallbacks`

Enable Public Key Callbacks (default: disabled) 

#### Enables
- `HAVE_PK_CALLBACKS`

### `--disable-pkcallbacks`

 

### `--enable-aescbc`

Enable wolfSSL AES-CBC support (default: enabled) 

### `--disable-aescbc`

 

#### Enables
- `NO_AES_CBC`

### `--enable-aescbc-length-checks`

Enable AES-CBC length validity checks (default: disabled) 

#### Enables
- `WOLFSSL_AES_CBC_LENGTH_CHECKS`

### `--disable-aescbc-length-checks`

 

### `--enable-aesgcm`

Enable wolfSSL AES-GCM support (default: enabled) 

### `--disable-aesgcm`

 

#### Removes
- `HAVE_AESGCM`
- `GCM_TABLE_4BIT`

### `--enable-aesgcm-stream`

Enable wolfSSL AES-GCM support with streaming APIs (default: disabled) 

#### Enables
- `WOLFSSL_AESGCM_STREAM`

### `--disable-aesgcm-stream`

 

### `--enable-aesccm`

Enable wolfSSL AES-CCM support (default: disabled) 

#### Enables
- `HAVE_AESCCM`

### `--disable-aesccm`

 

### `--enable-aeseax`

Enable wolfSSL AES-EAX support (default: disabled) 

#### Enables
- `WOLFSSL_AES_EAX`
- `WOLFSSL_AES_COUNTER`
- `WOLFSSL_CMAC`
- `WOLFSSL_AES_DIRECT`

### `--disable-aeseax`

 

### `--enable-aessiv`

Enable AES-SIV (RFC 5297) (default: disabled) 

#### Enables
- `WOLFSSL_CMAC`
- `WOLFSSL_AES_DIRECT`
- `WOLFSSL_AES_SIV`
- `WOLFSSL_AES_COUNTER`

### `--disable-aessiv`

 

### `--enable-aesctr`

Enable wolfSSL AES-CTR support (default: disabled) 

#### Enables
- `WOLFSSL_AES_COUNTER`
- `WOLFSSL_AES_DIRECT`

### `--disable-aesctr`

 

### `--enable-aesofb`

Enable wolfSSL AES-OFB support (default: disabled) 

#### Enables
- `WOLFSSL_AES_DIRECT`
- `WOLFSSL_AES_OFB`

### `--disable-aesofb`

 

### `--enable-aescfb`

Enable wolfSSL AES-CFB support (default: disabled) 

#### Enables
- `WOLFSSL_AES_CFB`

### `--disable-aescfb`

 

### `--enable-aes-bitsliced`

Enable bitsliced implementation of AES (default: disabled) 

#### Enables
- `HAVE_AES_ECB`
- `WC_AES_BITSLICED`
- `WOLFSSL_AES_DIRECT`

### `--disable-aes-bitsliced`

 

### `--enable-sm4-ecb`

Enable wolfSSL SM4-ECB support (default: disabled) 

#### Enables
- `WOLFSSL_SM4_ECB`
- `WOLFSSL_SM4`

### `--disable-sm4-ecb`

 

### `--enable-sm4-cbc`

Enable wolfSSL SM4-CBC support (default: disabled) 

#### Enables
- `WOLFSSL_SM4_CBC`
- `WOLFSSL_SM4`

### `--disable-sm4-cbc`

 

### `--enable-sm4-ctr`

Enable wolfSSL SM4-CTR support (default: disabled) 

#### Enables
- `WOLFSSL_SM4`
- `WOLFSSL_SM4_CTR`

### `--disable-sm4-ctr`

 

### `--enable-sm4-gcm`

Enable wolfSSL SM4-GCM support (default: disabled) 

#### Enables
- `WOLFSSL_SM4`
- `WOLFSSL_SM4_GCM`

### `--disable-sm4-gcm`

 

### `--enable-sm4-ccm`

Enable wolfSSL SM4-CCM support (default: disabled) 

#### Enables
- `WOLFSSL_SM4`
- `WOLFSSL_SM4_CCM`

### `--disable-sm4-ccm`

 

### `--enable-armasm`

Enable wolfSSL ARMv8 ASM support (default: disabled). Set to sha512-crypto or sha3-crypto to use SHA512 and SHA3 instructions with Aarch64 CPU. 

#### Enables
- `WOLFSSL_NO_HASH_RAW`
- `WOLFSSL_ARMASM_CRYPTO_SHA512`
- `WOLFSSL_ARMASM_CRYPTO_SHA3`
- `WOLFSSL_ARMASM`

### `--disable-armasm`

 

### `--enable-riscv-asm`

Enable wolfSSL RISC-V ASM support (default: disabled). 

#### Enables
- `WOLFSSL_RISCV_ASM`

### `--disable-riscv-asm`

 

### `--enable-xilinx`

Enable wolfSSL support for Xilinx hardened crypto(default: disabled) 

#### Enables
- `WOLFSSL_XILINX`
- `WOLFSSL_XILINX_CRYPT`

### `--disable-xilinx`

 

### `--enable-aria`

Enable wolfSSL support for ARIA (default: disabled) 

### `--disable-aria`

 

### `--enable-caam`

Enable wolfSSL support for CAAM (default: disabled) 

#### Enables
- `WOLFSSL_CAAM`
- `WOLF_CRYPTO_CB`

### `--disable-caam`

 

### `--enable-aesni`

Enable wolfSSL AES-NI support (default: disabled) 

#### Enables
- `WOLFSSL_AESNI`

### `--disable-aesni`

 

### `--enable-intelasm`

Enable All Intel ASM speedups (default: disabled) 

#### Enables
- `WOLFSSL_AESNI`
- `USE_INTEL_SPEEDUP`

### `--disable-intelasm`

 

### `--enable-aligndata`

align data for ciphers (default: enabled) 

### `--disable-aligndata`

 

#### Removes
- `WOLFSSL_USE_ALIGN`

### `--enable-intelrand`

Enable Intel rdrand as preferred RNG source (default: disabled) 

#### Enables
- `HAVE_INTEL_RDRAND`

### `--disable-intelrand`

 

### `--enable-amdrand`

Enable AMD rdseed as preferred RNG seeding source (default: disabled) 

#### Enables
- `HAVE_AMD_RDSEED`

### `--disable-amdrand`

 

### `--enable-afalg`

Enable Linux af_alg use for crypto (default: disabled) 

#### Enables
- `WOLFSSL_AFALG_HASH_KEEP`
- `WOLFSSL_AFALG_HASH`
- `WOLFSSL_AFALG`

#### Removes
- `WOLFSSL_SHA224`

### `--disable-afalg`

 

### `--enable-kcapi-hash`

Enable libkcapi use for hashing (default: disabled) 

#### Enables
- `WOLFSSL_KCAPI_HASH`
- `WOLFSSL_KCAPI`
- `WOLFSSL_NOSHA512_256`
- `WOLFSSL_KCAPI_HASH_KEEP`
- `WOLFSSL_NOSHA512_224`

### `--disable-kcapi-hash`

 

### `--enable-kcapi-hmac`

Enable libkcapi use for HMAC (default: disabled) 

#### Enables
- `WOLFSSL_KCAPI`
- `WOLFSSL_KCAPI_HMAC`

### `--disable-kcapi-hmac`

 

### `--enable-kcapi-aes`

Enable libkcapi use for AES (default: disabled) 

#### Enables
- `WOLFSSL_KCAPI`
- `WOLFSSL_KCAPI_AES`

### `--disable-kcapi-aes`

 

### `--enable-kcapi-rsa`

Enable libkcapi use for RSA (default: disabled) 

#### Enables
- `WOLFSSL_KCAPI_RSA`
- `WOLFSSL_KCAPI`

### `--disable-kcapi-rsa`

 

### `--enable-kcapi-dh`

Enable libkcapi use for DH (default: disabled) 

#### Enables
- `WOLFSSL_KCAPI_DH`
- `WOLFSSL_KCAPI`
- `WOLFSSL_DH_EXTRA`

### `--disable-kcapi-dh`

 

### `--enable-kcapi-ecc`

Enable libkcapi use for ECC (default: disabled) 

#### Enables
- `WOLFSSL_KCAPI`
- `WOLFSSL_KCAPI_ECC`

### `--disable-kcapi-ecc`

 

### `--enable-kcapi`

Enable libkcapi use for crypto (default: disabled) 

#### Enables
- `WOLFSSL_KCAPI_HASH`
- `WOLFSSL_KCAPI_RSA`
- `WOLFSSL_KCAPI`
- `WOLFSSL_KCAPI_ECC`
- `WOLFSSL_KCAPI_AES`
- `WOLFSSL_KCAPI_HMAC`
- `WOLFSSL_DH_EXTRA`
- `WOLFSSL_NOSHA512_256`
- `WOLFSSL_KCAPI_HASH_KEEP`
- `WOLFSSL_NOSHA512_224`
- `WOLFSSL_KCAPI_DH`

### `--disable-kcapi`

 

### `--enable-devcrypto`

Enable Linux dev crypto calls: all | aes (all aes support) | hash (all hash algos) | cbc (aes-cbc only) (default: disabled) 

#### Enables
- `WOLFSSL_DEVCRYPTO_HASH_KEEP`
- `WOLFSSL_DEVCRYPTO_AES`
- `WOLFSSL_DEVCRYPTO_HASH`
- `WOLFSSL_NO_HASH_RAW`
- `WOLFSSL_DEVCRYPTO_CBC`
- `WOLFSSL_DEVCRYPTO`

#### Removes
- `WOLFSSL_SHA224`

### `--disable-devcrypto`

 

### `--enable-camellia`

Enable wolfSSL Camellia support (default: disabled) 

#### Enables
- `HAVE_CAMELLIA`

### `--disable-camellia`

 

### `--enable-md2`

Enable wolfSSL MD2 support (default: disabled) 

#### Enables
- `WOLFSSL_MD2`

### `--disable-md2`

 

### `--enable-nullcipher`

Enable wolfSSL NULL cipher support (default: disabled) 

#### Enables
- `HAVE_NULL_CIPHER`

### `--disable-nullcipher`

 

### `--enable-ripemd`

Enable wolfSSL RIPEMD-160 support (default: disabled) 

#### Enables
- `WOLFSSL_RIPEMD`

### `--disable-ripemd`

 

### `--enable-blake2`

Enable wolfSSL BLAKE2b support (default: disabled) 

#### Enables
- `HAVE_BLAKE2B`
- `HAVE_BLAKE2`

### `--disable-blake2`

 

### `--enable-blake2s`

Enable wolfSSL BLAKE2s support (default: disabled) 

#### Enables
- `HAVE_BLAKE2S`

### `--disable-blake2s`

 

### `--enable-sha224`

Enable wolfSSL SHA-224 support (default: enabled on x86_64/amd64/aarch64) 

### `--disable-sha224`

 

#### Removes
- `WOLFSSL_SHA224`

### `--enable-sha3`

Enable wolfSSL SHA-3 support (default: enabled on x86_64/amd64/aarch64) 

### `--disable-sha3`

 

#### Removes
- `WOLFSSL_SHA3`

### `--enable-shake128`

Enable wolfSSL SHAKE128 support (default: disabled) 

#### Enables
- `WOLFSSL_SHAKE128`

#### Removes
- `WOLFSSL_NO_SHAKE128`

### `--disable-shake128`

 

### `--enable-shake256`

Enable wolfSSL SHAKE256 support (default: disabled) 

#### Enables
- `WOLFSSL_SHAKE256`

#### Removes
- `WOLFSSL_NO_SHAKE256`

### `--disable-shake256`

 

### `--enable-sha512`

Enable wolfSSL SHA-512 support (default: enabled) 

### `--disable-sha512`

 

#### Removes
- `WOLFSSL_SHA512`

### `--enable-sha384`

Enable wolfSSL SHA-384 support (default: enabled) 

### `--disable-sha384`

 

#### Removes
- `WOLFSSL_SHA384`

### `--enable-sm3`

Enable wolfSSL SM3 support (default: disabled) 

#### Enables
- `WOLFSSL_SM3`

### `--disable-sm3`

 

### `--enable-sessioncerts`

Enable session cert storing (default: disabled) 

#### Enables
- `SESSION_CERTS`

### `--disable-sessioncerts`

 

### `--enable-keygen`

Enable key generation (only applies to RSA key generation) (default: disabled) 

#### Enables
- `WOLFSSL_KEY_GEN`

### `--disable-keygen`

 

### `--enable-acert`

Enable attribute certificate support (default: disabled) 

#### Enables
- `WOLFSSL_ACERT`

### `--disable-acert`

 

### `--enable-certgen`

Enable cert generation (default: disabled) 

#### Enables
- `WOLFSSL_CERT_GEN`

### `--disable-certgen`

 

### `--enable-certreq`

Enable cert request generation (default: disabled) 

#### Enables
- `WOLFSSL_CERT_REQ`

### `--disable-certreq`

 

### `--enable-certext`

Enable cert request extensions (default: disabled) 

#### Enables
- `WOLFSSL_CERT_EXT`

### `--disable-certext`

 

### `--enable-certgencache`

Enable decoded cert caching (default: disabled) 

#### Enables
- `WOLFSSL_CERT_GEN_CACHE`

### `--disable-certgencache`

 

### `--enable-sep`

Enable sep extensions (default: disabled) 

#### Enables
- `WOLFSSL_SEP`
- `KEEP_PEER_CERT`

### `--disable-sep`

 

### `--enable-hkdf`

Enable HKDF (HMAC-KDF) support (default: disabled) 

### `--disable-hkdf`

 

### `--enable-hpke`

Enable HKPE support (default: disabled) 

#### Enables
- `HAVE_HPKE`

### `--disable-hpke`

 

### `--enable-x963kdf`

Enable X9.63 KDF support (default: disabled) 

#### Enables
- `HAVE_X963_KDF`

### `--disable-x963kdf`

 

### `--enable-srtp-kdf`

Enable SRTP-KDF support (default: disabled) 

#### Enables
- `HAVE_AES_ECB`
- `WOLFSSL_AES_DIRECT`
- `WC_SRTP_KDF`

### `--disable-srtp-kdf`

 

### `--enable-dsa`

Enable DSA (default: disabled) 

#### Removes
- `NO_DSA`

### `--disable-dsa`

 

### `--enable-eccshamir`

Enable ECC Shamir (default: enabled) 

### `--disable-eccshamir`

 

#### Removes
- `ECC_SHAMIR`

### `--enable-ecc`

Enable ECC (default: enabled) 

### `--disable-ecc`

 

#### Removes
- `TFM_ECC256`
- `HAVE_ECC`
- `ECC_SHAMIR`

### `--enable-sm2`

Enable wolfSSL SM2 support (default: disabled) 

#### Enables
- `WOLFSSL_SM2`
- `WOLFSSL_BASE16`

### `--disable-sm2`

 

### `--enable-ecccustcurves`

Enable ECC custom curves (default: disabled) 

#### Enables
- `HAVE_ECC_BRAINPOOL`
- `WOLFSSL_CUSTOM_CURVES`

### `--disable-ecccustcurves`

 

### `--enable-compkey`

Enable compressed keys support (default: disabled) 

#### Enables
- `HAVE_COMP_KEY`

### `--disable-compkey`

 

### `--enable-brainpool`

Enable Brainpool ECC curves (default: enabled with ECC custom curves) 

### `--disable-brainpool`

 

### `--enable-curve25519`

Enable Curve25519 (default: disabled) 

#### Enables
- `HAVE_CURVE25519`

### `--disable-curve25519`

 

### `--enable-ed25519`

Enable ED25519 (default: disabled) 

#### Enables
- `HAVE_ED25519`

### `--disable-ed25519`

 

### `--enable-ed25519-stream`

Enable wolfSSL ED25519 support with streaming verify APIs (default: disabled) 

### `--disable-ed25519-stream`

 

### `--enable-curve448`

Enable Curve448 (default: disabled) 

#### Enables
- `HAVE_CURVE448`

### `--disable-curve448`

 

### `--enable-ed448`

Enable ED448 (default: disabled) 

#### Enables
- `HAVE_ED448`
- `WOLFSSL_SHAKE256`

#### Removes
- `WOLFSSL_NO_SHAKE256`

### `--disable-ed448`

 

### `--enable-ed448-stream`

Enable wolfSSL ED448 support with streaming verify APIs (default: disabled) 

### `--disable-ed448-stream`

 

### `--enable-fpecc`

Enable Fixed Point cache ECC (default: disabled) 

#### Enables
- `FP_ECC`

### `--disable-fpecc`

 

### `--enable-eccencrypt`

Enable ECC encrypt (default: disabled). yes = SEC1 standard, geniv = Generate IV, iso18033 = ISO 18033 standard, old = original wolfSSL algorithm 

#### Enables
- `HAVE_ECC_ENCRYPT`

### `--disable-eccencrypt`

 

### `--enable-eccsi`

Enable ECCSI (default: disabled) 

#### Enables
- `WOLFCRYPT_HAVE_ECCSI`
- `WOLFSSL_PUBLIC_MP`

### `--disable-eccsi`

 

### `--enable-sakke`

Enable SAKKE - paring based crypto (default: disabled) 

#### Enables
- `WOLFCRYPT_HAVE_SAKKE`

### `--disable-sakke`

 

### `--enable-psk`

Enable PSK (default: disabled) 

#### Removes
- `NO_PSK`

### `--disable-psk`

 

### `--enable-psk-one-id`

Enable PSK (default: disabled) 

#### Enables
- `WOLFSSL_PSK_ONE_ID`

#### Removes
- `NO_PSK`

### `--disable-psk-one-id`

 

### `--enable-errorstrings`

Enable error strings table (default: enabled) 

### `--disable-errorstrings`

 

#### Enables
- `NO_ERROR_STRINGS`

### `--enable-errorqueue`

Disables adding nodes to error queue when compiled with OPENSSL_EXTRA (default: enabled) 

### `--disable-errorqueue`

 

#### Enables
- `NO_ERROR_QUEUE`

### `--enable-sslv3`

Enable SSL version 3.0 (default: disabled) 

#### Enables
- `WOLFSSL_ALLOW_SSLV3`

#### Removes
- `NO_OLD_TLS`

### `--disable-sslv3`

 

### `--enable-tlsv10`

Enable old TLS versions 1.0 (default: disabled) 

#### Enables
- `WOLFSSL_ALLOW_TLSV10`

#### Removes
- `NO_OLD_TLS`

### `--disable-tlsv10`

 

### `--enable-oldtls`

Enable old TLS versions < 1.2 (default: disabled) 

#### Removes
- `NO_OLD_TLS`

### `--disable-oldtls`

 

### `--enable-tlsv12`

Enable TLS versions 1.2 (default: enabled) 

### `--disable-tlsv12`

 

#### Enables
- `WOLFSSL_NO_TLS12`
- `NO_SESSION_CACHE`

#### Removes
- `HAVE_SERVER_RENEGOTIATION_INFO`

### `--enable-stacksize`

Enable stack size info on examples (default: disabled) 

#### Enables
- `HAVE_STACK_SIZE`

### `--disable-stacksize`

 

### `--enable-memory`

Enable memory callbacks (default: enabled) 

### `--disable-memory`

 

#### Enables
- `NO_WOLFSSL_MEMORY`

### `--enable-trackmemory`

Enable memory use info on wolfCrypt and wolfSSL cleanup (default: disabled) 

#### Enables
- `WOLFSSL_TRACK_MEMORY`

### `--disable-trackmemory`

 

### `--enable-memorylog`

Enable dynamic memory logging (default: disabled) 

#### Enables
- `WOLFSSL_MEMORY_LOG`

### `--disable-memorylog`

 

### `--enable-stacklog`

Enable stack logging (default: disabled) 

#### Enables
- `WOLFSSL_STACK_LOG`

### `--disable-stacklog`

 

### `--enable-wolfsentry`

Enable wolfSentry hooks and plugins (default: disabled) 

#### Enables
- `WOLFSSL_WOLFSENTRY_HOOKS`
- `HAVE_EX_DATA_CLEANUP_HOOKS`
- `OPENSSL_EXTRA`
- `HAVE_EX_DATA`
- `WOLFSSL_ENCRYPTED_KEYS`

### `--disable-wolfsentry`

 

### `--enable-qt-test`

Enable qt tests (default: disabled) 

#### Enables
- `OPENSSL_NO_SSL3`
- `WOLFSSL_STATIC_PSK`
- `WOLFSSL_STATIC_RSA`

### `--disable-qt-test`

 

### `--enable-rsa`

Enable RSA (default: enabled) 

### `--disable-rsa`

 

#### Enables
- `NO_RSA`

#### Removes
- `WC_RSA_PSS`
- `WOLFSSL_PSS_LONG_SALT`

### `--enable-oaep`

Enable RSA OAEP (default: enabled) 

### `--disable-oaep`

 

#### Enables
- `WC_NO_RSA_OAEP`

### `--enable-rsapub`

Enable RSA Public Only (default: disabled) 

#### Enables
- `WOLFSSL_RSA_PUBLIC_ONLY`

### `--disable-rsapub`

 

### `--enable-rsavfy`

Enable RSA Verify Inline Only (default: disabled) 

#### Enables
- `WOLFSSL_RSA_PUBLIC_ONLY`
- `NO_CHECK_PRIVATE_KEY`
- `NO_SIG_WRAPPER`
- `WOLFSSL_RSA_VERIFY_INLINE`
- `WOLFSSL_RSA_VERIFY_ONLY`

### `--disable-rsavfy`

 

### `--enable-rsapss`

Enable RSA-PSS (default: disabled) 

### `--disable-rsapss`

 

### `--enable-dh`

Enable DH (default: enabled) 

### `--disable-dh`

 

#### Enables
- `NO_DH`

#### Removes
- `HAVE_DH_DEFAULT_PARAMS`
- `HAVE_FFDHE_2048`

### `--enable-anon`

Enable Anonymous (default: disabled) 

#### Enables
- `HAVE_ANON`

### `--disable-anon`

 

### `--enable-asn-print`

Enable ASN Print API (default: enabled) 

### `--disable-asn-print`

 

#### Removes
- `WOLFSSL_ASN_PRINT`

### `--enable-aes`

Enable AES (default: enabled) 

### `--disable-aes`

 

### `--enable-dtls13`

Enable wolfSSL DTLS v1.3 (default: disabled) 

### `--disable-dtls13`

 

### `--enable-dtlscid`

Enable wolfSSL DTLS ConnectionID (default: disabled) 

### `--disable-dtlscid`

 

### `--enable-dtls-frag-ch`

Enable wolfSSL DTLS 1.3 ClientHello fragmenting (default: disabled) 

### `--disable-dtls-frag-ch`

 

### `--enable-coding`

Enable Coding base 16/64 (default: enabled) 

### `--disable-coding`

 

#### Enables
- `NO_CODING`

### `--enable-base64encode`

Enable Base64 encoding (default: enabled on x86_64/amd64) 

#### Enables
- `WOLFSSL_BASE64_ENCODE`

### `--disable-base64encode`

 

### `--enable-base16`

Enable Base16 encoding/decoding (default: disabled) 

#### Enables
- `WOLFSSL_BASE16`

### `--disable-base16`

 

### `--enable-md4`

Enable MD4 (default: disabled) 

#### Removes
- `NO_MD4`

### `--disable-md4`

 

### `--enable-des3`

Enable DES3 (default: disabled) 

#### Removes
- `NO_DES3`

### `--disable-des3`

 

### `--enable-des3-tls-suites`

Enable DES3 TLS cipher suites (default: disabled) 

### `--disable-des3-tls-suites`

 

### `--enable-arc4`

Enable ARC4 (default: disabled) 

#### Enables
- `WOLFSSL_ALLOW_RC4`

#### Removes
- `NO_RC4`

### `--disable-arc4`

 

### `--enable-md5`

Enable MD5 (default: enabled) 

### `--disable-md5`

 

#### Enables
- `NO_MD5`

### `--enable-sha`

Enable SHA (default: enabled) 

### `--disable-sha`

 

#### Enables
- `NO_SHA`

### `--enable-siphash`

Enable SipHash (default: disabled) 

#### Enables
- `WOLFSSL_SIPHASH`

### `--disable-siphash`

 

### `--enable-cmac`

Enable CMAC (default: disabled) 

#### Enables
- `WOLFSSL_CMAC`
- `WOLFSSL_AES_DIRECT`

### `--disable-cmac`

 

### `--enable-aesxts`

Enable AES XTS (default: disabled) 

#### Enables
- `WOLFSSL_AES_DIRECT`
- `WOLFSSL_AESXTS_STREAM`
- `WOLFSSL_AES_XTS`

### `--disable-aesxts`

 

### `--enable-aesxts-stream`

Enable wolfSSL AES-XTS support with streaming APIs (default: disabled) 

### `--disable-aesxts-stream`

 

### `--enable-xts`

Please use --enable-aesxts 

#### Enables
- `WOLFSSL_AES_DIRECT`
- `WOLFSSL_AES_XTS`

### `--disable-xts`

 

### `--enable-webserver`

Enable Web Server (default: disabled) 

#### Enables
- `WOLFSSL_ENCRYPTED_KEYS`
- `HAVE_WEBSERVER`

### `--disable-webserver`

 

### `--enable-webclient`

Enable Web Client (HTTP) (default: disabled) 

#### Enables
- `HAVE_HTTP_CLIENT`

### `--disable-webclient`

 

### `--enable-rc2`

Enable RC2 encryption (default: disabled) 

#### Enables
- `WC_RC2`

### `--disable-rc2`

 

### `--enable-cuda`

Enable NVidia CUDA support (default: disabled) 

### `--disable-cuda`

 

### `--enable-certservice`

Enable cert service (default: disabled) 

#### Enables
- `WOLFSSL_HAVE_CERT_SERVICE`
- `WOLFSSL_CERT_GEN`
- `WOLFSSL_ENCRYPTED_KEYS`
- `OPENSSL_EXTRA`

### `--disable-certservice`

 

### `--enable-pwdbased`

Enable PWDBASED (default: disabled) 

### `--disable-pwdbased`

 

### `--enable-wolfEntropy`

Enable memuse entropy support (default: disabled) 

### `--disable-wolfEntropy`

 

### `--enable-entropy-memuse`

Enable memuse entropy support (default: disabled) 

#### Enables
- `HAVE_ENTROPY_MEMUSE`

### `--disable-entropy-memuse`

 

### `--enable-aeskeywrap`

Enable AES key wrap support (default: disabled) 

#### Enables
- `WOLFSSL_AES_DIRECT`
- `HAVE_AES_KEYWRAP`

### `--disable-aeskeywrap`

 

### `--enable-selftest`

Enable selftest, Will NOT work w/o CAVP selftest license (default: disabled) 

#### Enables
- `WOLFSSL_SP_INT_NEGATIVE`
- `HAVE_SELFTEST`
- `HAVE_PUBLIC_FFDHE`

### `--disable-selftest`

 

### `--enable-poly1305`

Enable wolfSSL POLY1305 support (default: enabled) 

### `--disable-poly1305`

 

#### Removes
- `HAVE_POLY1305`

### `--enable-chacha`

Enable CHACHA (default: enabled). Use `=noasm` to disable ASM AVX/AVX2 speedups 

### `--disable-chacha`

 

#### Removes
- `HAVE_CHACHA`

### `--enable-xchacha`

Enable XCHACHA (default: disabled). 

#### Enables
- `HAVE_XCHACHA`

### `--disable-xchacha`

 

### `--enable-hashdrbg`

Enable Hash DRBG support (default: enabled) 

### `--disable-hashdrbg`

 

#### Enables
- `WC_NO_HASHDRBG`

#### Removes
- `HAVE_HASHDRBG`

### `--enable-filesystem`

Enable Filesystem support (default: enabled) 

### `--disable-filesystem`

 

#### Enables
- `NO_FILESYSTEM`

#### Removes
- `WOLFSSL_SYS_CA_CERTS`

### `--enable-c89`

Build with C89 toolchain (default: disabled) 

#### Enables
- `WOLF_C89`
- `NO_INLINE`

### `--disable-c89`

 

### `--enable-inline`

Enable inline functions (default: enabled) 

### `--disable-inline`

 

#### Enables
- `NO_INLINE`

### `--enable-ocsp`

Enable OCSP (default: disabled) 

#### Enables
- `HAVE_OCSP`
- `HAVE_OPENSSL_CMD`

### `--disable-ocsp`

 

### `--enable-ocspstapling`

Enable OCSP Stapling ((options: yes, no-multi, no, disabled default: disabled) 

#### Enables
- `HAVE_OCSP`
- `WOLFSSL_TLS_OCSP_MULTI`
- `HAVE_CERTIFICATE_STATUS_REQUEST`

### `--disable-ocspstapling`

 

### `--enable-ocspstapling2`

Enable OCSP Stapling v2 (default: disabled) 

#### Enables
- `HAVE_OCSP`
- `HAVE_CERTIFICATE_STATUS_REQUEST_V2`

### `--disable-ocspstapling2`

 

### `--enable-crl`

Enable CRL (Use =io for inline CRL HTTP GET) (default: disabled) 

#### Enables
- `HAVE_CRL`

### `--disable-crl`

 

### `--enable-crl-monitor`

Enable CRL Monitor (default: disabled) 

#### Enables
- `HAVE_CRL_MONITOR`

### `--disable-crl-monitor`

 

### `--enable-sni`

Enable SNI (default: enabled on x86_64/x86/aarch64/amd64) 

### `--disable-sni`

 

#### Removes
- `HAVE_SNI`

### `--enable-maxfragment`

Enable Maximum Fragment Length (default: disabled) 

#### Enables
- `HAVE_MAX_FRAGMENT`

### `--disable-maxfragment`

 

### `--enable-alpn`

Enable ALPN (default: disabled) 

#### Enables
- `HAVE_ALPN`

### `--disable-alpn`

 

### `--enable-trustedca`

Enable Trusted CA Indication (default: disabled) 

#### Enables
- `HAVE_TRUSTED_CA`

### `--disable-trustedca`

 

### `--enable-truncatedhmac`

Enable Truncated HMAC (default: disabled) 

#### Enables
- `HAVE_TRUNCATED_HMAC`

### `--disable-truncatedhmac`

 

### `--enable-renegotiation-indication`

Enable Renegotiation Indication for client via empty cipher (default: disabled) 

#### Enables
- `HAVE_RENEGOTIATION_INDICATION`

#### Removes
- `HAVE_SERVER_RENEGOTIATION_INFO`

### `--disable-renegotiation-indication`

 

### `--enable-secure-renegotiation`

Enable Secure Renegotiation (default: disabled) 

#### Enables
- `HAVE_SECURE_RENEGOTIATION`

### `--disable-secure-renegotiation`

 

### `--enable-secure-renegotiation-info`

Enable Secure Renegotiation info extension (default: enabled) 

### `--disable-secure-renegotiation-info`

 

#### Removes
- `HAVE_SERVER_RENEGOTIATION_INFO`

### `--enable-fallback-scsv`

Enable Fallback SCSV (default: disabled) 

#### Enables
- `HAVE_FALLBACK_SCSV`

### `--disable-fallback-scsv`

 

### `--enable-keying-material`

Enable Keying Material Exporters (default: disabled) 

#### Enables
- `HAVE_KEYING_MATERIAL`

### `--disable-keying-material`

 

### `--enable-supportedcurves`

Enable Supported Elliptic Curves (default: enabled) 

### `--disable-supportedcurves`

 

### `--enable-ffdhe-only`

Enable using only FFDHE in client (default: disabled) 

#### Enables
- `WOLFSSL_REQUIRE_FFDHE`

### `--disable-ffdhe-only`

 

### `--enable-session-ticket`

Enable Session Ticket (default: disabled) 

#### Enables
- `HAVE_SESSION_TICKET`

### `--disable-session-ticket`

 

### `--enable-ticket-nonce-malloc`

Enable dynamic allocation of ticket nonces (default: disabled) 

#### Enables
- `WOLFSSL_TICKET_NONCE_MALLOC`

### `--disable-ticket-nonce-malloc`

 

### `--enable-extended-master`

Enable Extended Master Secret (default: enabled) 

### `--disable-extended-master`

 

#### Removes
- `HAVE_EXTENDED_MASTER`

### `--enable-tlsx`

Enable all TLS Extensions (default: disabled) 

#### Enables
- `HAVE_ALPN`
- `HAVE_TRUSTED_CA`
- `HAVE_TRUNCATED_HMAC`
- `HAVE_MAX_FRAGMENT`

### `--disable-tlsx`

 

### `--enable-earlydata`

Enable Early Data handshake with wolfSSL TLS v1.3 (default: disabled) 

### `--disable-earlydata`

 

### `--enable-pkcs7`

Enable PKCS7 (default: disabled) 

#### Enables
- `HAVE_AES_KEYWRAP`
- `WOLFSSL_AES_DIRECT`
- `HAVE_PKCS7`
- `HAVE_X963_KDF`

### `--disable-pkcs7`

 

### `--enable-wolfssh`

Enable wolfSSH options (default: disabled) 

#### Enables
- `WOLFSSL_PUBLIC_MP`
- `WOLFSSL_WOLFSSH`

### `--disable-wolfssh`

 

### `--enable-ssh`

Enable wolfSSH options (default: disabled) 

#### Enables
- `WOLFSSL_PUBLIC_MP`
- `WOLFSSL_WOLFSSH`

### `--disable-ssh`

 

### `--enable-wolftpm`

Enable wolfTPM options (default: disabled) 

#### Enables
- `HAVE_AES_KEYWRAP`
- `WOLFSSL_AES_CFB`
- `HAVE_PKCS7`
- `WOLFSSL_PUBLIC_MP`
- `HAVE_X963_KDF`
- `WOLF_CRYPTO_CB`
- `WOLFSSL_CERT_EXT`
- `WOLFSSL_CERT_REQ`
- `WOLFSSL_CERT_GEN`
- `WOLFSSL_AES_DIRECT`

### `--disable-wolftpm`

 

### `--enable-wolfclu`

Enable wolfCLU options (default: disabled) 

#### Enables
- `HAVE_OID_ENCODING`
- `HAVE_ED25519`
- `WC_RSA_NO_PADDING`
- `WOLFSSL_CERT_NAME_ALL`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_AES_DIRECT`
- `WOLFSSL_CERT_EXT`
- `HAVE_X963_KDF`
- `WOLFSSL_NO_ASN_STRICT`
- `OPENSSL_EXTRA`
- `WOLFSSL_KEY_GEN`
- `HAVE_PKCS7`
- `WOLFSSL_CERT_GEN`
- `WOLFSSL_EITHER_SIDE`
- `WOLFSSL_CERT_REQ`
- `HAVE_AES_KEYWRAP`
- `WOLFSSL_ALT_NAMES`
- `WOLFSSL_AES_COUNTER`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `OPENSSL_ALL`

#### Removes
- `NO_DES3`

### `--disable-wolfclu`

 

### `--enable-scep`

Enable wolfSCEP (default: disabled) 

#### Enables
- `HAVE_X963_KDF`
- `WOLFSSL_CERT_GEN`
- `HAVE_AES_KEYWRAP`
- `WOLFSSL_CERT_REQ`
- `WOLFSSL_AES_DIRECT`
- `HAVE_PKCS7`
- `WOLFSSL_HAVE_WOLFSCEP`
- `WOLFSSL_CERT_EXT`
- `WOLFSSL_KEY_GEN`

### `--disable-scep`

 

### `--enable-srp`

Enable Secure Remote Password (default: disabled) 

#### Enables
- `WOLFCRYPT_HAVE_SRP`

### `--disable-srp`

 

### `--enable-indef`

Enable parsing of indefinite length encoded msgs (default: disabled) 

#### Enables
- `ASN_BER_TO_DER`

### `--disable-indef`

 

### `--enable-altcertchains`

Enable using alternative certificate chains, only require leaf certificate to validate to trust root (default: disabled) 

#### Enables
- `WOLFSSL_ALT_CERT_CHAINS`

### `--disable-altcertchains`

 

### `--enable-smallstackcache`

Enable Small Stack Usage Caching (default: disabled) 

#### Enables
- `WOLFSSL_SMALL_STACK`
- `WOLFSSL_SMALL_STACK_CACHE`

### `--disable-smallstackcache`

 

### `--enable-smallstack`

Enable Small Stack Usage (default: disabled) 

#### Enables
- `WOLFSSL_SMALL_STACK`

### `--disable-smallstack`

 

### `--enable-valgrind`

Enable valgrind for unit tests (default: disabled) 

### `--disable-valgrind`

 

### `--enable-testcert`

Enable Test Cert (default: disabled) 

#### Enables
- `WOLFSSL_TEST_CERT`

### `--disable-testcert`

 

### `--enable-iopool`

Enable I/O Pool example (default: disabled) 

#### Enables
- `XMALLOC_USER`
- `HAVE_IO_POOL`

### `--disable-iopool`

 

### `--enable-jni`

Enable wolfSSL JNI (default: disabled) 

#### Enables
- `ATOMIC_USER`
- `PERSIST_CERT_CACHE`
- `WOLFSSL_CERT_REQ`
- `SESSION_CERTS`
- `WOLFSSL_CERT_EXT`
- `WOLFSSL_CERT_NAME_ALL`
- `WOLFSSL_EITHER_SIDE`
- `HAVE_PK_CALLBACKS`
- `WOLFSSL_ALT_NAMES`
- `WOLFSSL_ALT_CERT_CHAINS`
- `HAVE_CRL_MONITOR`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_ALWAYS_VERIFY_CB`
- `WOLFSSL_ENCRYPTED_KEYS`
- `HAVE_OCSP`
- `HAVE_EX_DATA`
- `KEEP_PEER_CERT`
- `PERSIST_SESSION_CACHE`
- `HAVE_ALPN`
- `OPENSSL_ALL`
- `WOLFSSL_DTLS`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `HAVE_CRL`
- `WOLFSSL_JNI`
- `WOLFSSL_KEY_GEN`
- `OPENSSL_EXTRA`
- `WOLFSSL_CERT_GEN`
- `NO_ERROR_QUEUE`
- `WC_RSA_NO_PADDING`

#### Removes
- `NO_PSK`

### `--disable-jni`

 

### `--enable-asio`

Enable asio (default: disabled) 

#### Enables
- `WOLFSSL_CERT_NAME_ALL`
- `OPENSSL_ALL`
- `BOOST_ASIO_USE_WOLFSSL`
- `OPENSSL_EXTRA`
- `WC_RSA_NO_PADDING`
- `WOLFSSL_ASIO`
- `ASIO_USE_WOLFSSL`
- `OPENSSL_NO_SSL3`
- `HAVE_OCSP`
- `HAVE_EX_DATA`
- `WOLFSSL_ENCRYPTED_KEYS`
- `WOLFSSL_KEY_GEN`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `OPENSSL_NO_SSL2`
- `WOLFSSL_EITHER_SIDE`
- `SSL_TXT_TLSV1_2`

### `--disable-asio`

 

### `--enable-apachehttpd`

Enable Apache httpd (default: disabled) 

#### Enables
- `OPENSSL_EXTRA`
- `WOLFSSL_TRUST_PEER_CERT`
- `WC_RSA_NO_PADDING`
- `WOLFSSL_PRIORITIZE_PSK`
- `WOLFSSL_TLS13_NO_PEEK_HANDSHAKE_DONE`
- `WOLFSSL_CERT_REQ`
- `HAVE_EX_DATA`
- `WOLFSSL_NO_OCSP_ISSUER_CHECK`
- `WOLFSSL_CERT_EXT`
- `WOLFSSL_ALT_CERT_CHAINS`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `WOLFSSL_ALWAYS_KEEP_SNI`
- `OPENSSL_NO_SSL3`
- `HAVE_ALPN`
- `WOLFSSL_CERT_GEN`
- `WOLFSSL_SIGNER_DER_CERT`
- `SESSION_CERTS`
- `OPENSSL_COMPATIBLE_DEFAULTS`
- `WOLFSSL_EITHER_SIDE`
- `WOLFSSL_CHECK_ALERT_ON_ERR`
- `OPENSSL_ALL`
- `OPENSSL_NO_COMP`
- `WOLFSSL_ENCRYPTED_KEYS`
- `NO_SESSION_CACHE_REF`
- `HAVE_SECURE_RENEGOTIATION`
- `HAVE_OCSP`
- `HAVE_CRL`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_CERT_NAME_ALL`
- `WOLFSSL_APACHE_HTTPD`
- `OPENSSL_NO_SSL2`

### `--disable-apachehttpd`

 

### `--enable-enc-then-mac`

Enable Encrypt-Then-Mac extension (default: enabled) 

### `--disable-enc-then-mac`

 

#### Removes
- `HAVE_ENCRYPT_THEN_MAC`

### `--enable-stunnel`

Enable stunnel (default: disabled) 

#### Enables
- `HAVE_SESSION_TICKET`
- `WOLFSSL_TRUST_PEER_CERT`
- `NO_SESSION_CACHE_REF`
- `WOLFSSL_DES_ECB`
- `SESSION_CERTS`
- `WOLFSSL_TLS13_NO_PEEK_HANDSHAKE_DONE`
- `WOLFSSL_CERT_EXT`
- `OPENSSL_EXTRA`
- `WOLFSSL_SIGNER_DER_CERT`
- `HAVE_EX_DATA`
- `WOLFSSL_CERT_GEN`
- `HAVE_STUNNEL`
- `OPENSSL_COMPATIBLE_DEFAULTS`
- `HAVE_TRUNCATED_HMAC`
- `WOLFSSL_TICKET_HAVE_ID`
- `WOLFSSL_ALWAYS_VERIFY_CB`
- `WOLFSSL_ALT_CERT_CHAINS`
- `WOLFSSL_CHECK_ALERT_ON_ERR`
- `HAVE_OCSP`
- `WOLFSSL_ALWAYS_KEEP_SNI`
- `WOLFSSL_PRIORITIZE_PSK`
- `HAVE_CRL`
- `HAVE_MAX_FRAGMENT`
- `WOLFSSL_NO_OCSP_ISSUER_CHECK`
- `WOLFSSL_ENCRYPTED_KEYS`
- `WOLFSSL_KEY_GEN`

#### Removes
- `NO_MD4`
- `NO_DES3`
- `NO_PSK`

### `--disable-stunnel`

 

### `--enable-curl`

Enable curl (default: disabled) 

#### Enables
- `WOLFSSL_WOLFSSH`
- `NO_SESSION_CACHE_REF`
- `OPENSSL_EXTRA`
- `HAVE_CRL`
- `WOLFSSL_DES_ECB`
- `WOLFSSL_ENCRYPTED_KEYS`
- `HAVE_SESSION_TICKET`
- `WOLFSSL_IP_ALT_NAME`
- `HAVE_CERTIFICATE_STATUS_REQUEST_V2`
- `WOLFSSL_ALT_CERT_CHAINS`
- `WOLFSSL_TICKET_NONCE_MALLOC`
- `HAVE_OCSP`
- `WOLFSSL_PUBLIC_MP`
- `HAVE_CERTIFICATE_STATUS_REQUEST`

#### Removes
- `NO_MD4`
- `NO_DES3`

### `--disable-curl`

 

### `--enable-tcpdump`

Enable tcpdump (default: disabled) 

#### Enables
- `WOLFSSL_ENCRYPTED_KEYS`
- `OPENSSL_EXTRA`

#### Removes
- `NO_DES3`

### `--disable-tcpdump`

 

### `--enable-sblim-sfcb`

Enable sblim-sfcb support (default: disabled) 

#### Enables
- `HAVE_SBLIM_SFCB`
- `WOLFSSL_ENCRYPTED_KEYS`
- `WOLFSSL_CERT_GEN`
- `OPENSSL_EXTRA`
- `WOLFSSL_SIGNER_DER_CERT`

### `--disable-sblim-sfcb`

 

### `--enable-libest`

Enable libest (default: disabled) 

#### Enables
- `WOLFSSL_KEY_GEN`
- `WC_RSA_NO_PADDING`
- `WOLFSSL_CERT_EXT`
- `WOLFSSL_CERT_NAME_ALL`
- `WOLFSSL_ALT_NAMES`
- `WOLFSSL_ENCRYPTED_KEYS`
- `HAVE_X963_KDF`
- `WOLFCRYPT_HAVE_SRP`
- `WOLFSSL_EITHER_SIDE`
- `HAVE_AES_KEYWRAP`
- `HAVE_EX_DATA`
- `WOLFSSL_ERROR_CODE_OPENSSL`
- `OPENSSL_EXTRA`
- `WOLFSSL_TICKET_HAVE_ID`
- `OPENSSL_ALL`
- `SESSION_CERTS`
- `HAVE_CRL`
- `HAVE_PKCS7`
- `HAVE_OCSP`
- `WOLFSSL_CERT_REQ`
- `WOLFSSL_AES_DIRECT`
- `WOLFSSL_PSS_SALT_LEN_DISCOVER`
- `HAVE_LIBEST`
- `WOLFSSL_CERT_GEN`

### `--disable-libest`

 

### `--enable-enckeys`

Enable PEM encrypted private key support (default: disabled) 

#### Enables
- `WOLFSSL_ENCRYPTED_KEYS`

### `--disable-enckeys`

 

### `--enable-pkcs12`

Enable pkcs12 (default: enabled) 

### `--disable-pkcs12`

 

#### Enables
- `NO_PKCS12`
- `NO_PWDBASED`

### `--enable-scrypt`

Enable SCRYPT (default: disabled) 

#### Enables
- `HAVE_SCRYPT`

### `--disable-scrypt`

 

### `--enable-examples`

Enable Examples (default: enabled) 

### `--disable-examples`

 

### `--enable-crypttests`

Enable Crypt Bench/Test (default: enabled) 

### `--disable-crypttests`

 

### `--enable-crypttests-libs`

Enable wolfcrypt test and benchmark libraries (default: disabled) 

### `--disable-crypttests-libs`

 

### `--enable-pkcs11`

Enable pkcs11 access (default: disabled) 

#### Enables
- `HAVE_WOLF_BIGINT`
- `WOLF_CRYPTO_CB`
- `HAVE_PKCS11`

### `--disable-pkcs11`

 

### `--enable-pkcs8`

Enable PKCS #8 key packages (default: enabled) 

### `--disable-pkcs8`

 

#### Enables
- `NO_PKCS8`

### `--enable-staticmemory`

Enable static memory use (default: disabled) 

#### Enables
- `WOLFSSL_STATIC_MEMORY`

### `--disable-staticmemory`

 

### `--enable-mcapi`

Enable Microchip API (default: disabled) 

### `--disable-mcapi`

 

### `--enable-cryptodev`

DEPRECATED, use cryptocb instead 

### `--disable-cryptodev`

 

### `--enable-cryptocb`

 

#### Enables
- `WOLF_CRYPTO_CB`

### `--disable-cryptocb`

 

### `--disable-cryptocb-sw-test`

Disable wolfCrypt crypto callback tests using software crypto (default: enabled). Only valid with 

### `--enable-cryptocb-sw-test`

 

### `--enable-asynccrypt`

Enable Asynchronous Crypto (default: disabled) 

#### Enables
- `_GNU_SOURCE`
- `HAVE_WOLF_EVENT`
- `WOLFSSL_ASYNC_CRYPT_SW`
- `HAVE_WOLF_BIGINT`
- `WOLFSSL_ASYNC_CRYPT`
- `WOLFSSL_NO_HASH_RAW`

#### Removes
- `WC_NO_ASYNC_THREADING`

### `--disable-asynccrypt`

 

### `--enable-asynccrypt-sw`

Enable asynchronous software-based crypto (default: disabled) 

#### Enables
- `_GNU_SOURCE`
- `WOLFSSL_NO_HASH_RAW`
- `HAVE_WOLF_EVENT`
- `WOLFSSL_ASYNC_CRYPT_SW`
- `HAVE_WOLF_BIGINT`
- `WOLFSSL_ASYNC_CRYPT`

#### Removes
- `WC_NO_ASYNC_THREADING`

### `--disable-asynccrypt-sw`

 

### `--enable-asyncthreads`

Enable Asynchronous Threading (default: enabled) 

### `--disable-asyncthreads`

 

### `--enable-autosar`

Enable AutoSAR support (default: disabled) 

#### Enables
- `WOLFSSL_AUTOSAR`

### `--disable-autosar`

 

### `--enable-sessionexport`

Enable export and import of sessions (default: disabled) 

#### Enables
- `WOLFSSL_SESSION_EXPORT`

### `--disable-sessionexport`

 

### `--enable-oldnames`

Keep backwards compat with old names (default: enabled) 

### `--disable-oldnames`

 

#### Enables
- `NO_OLD_SSL_NAMES`
- `NO_OLD_RNGNAME`
- `NO_OLD_WC_NAMES`
- `NO_OLD_SHA_NAMES`
- `NO_OLD_MD5_NAME`

### `--enable-memtest`

Memory testing option, for internal use (default: disabled) 

#### Enables
- `WOLFSSL_TRACK_MEMORY`
- `WOLFSSL_DEBUG_MEMORY`

### `--disable-memtest`

 

### `--enable-hashflags`

Enable support for hash flags (default: disabled) 

#### Enables
- `WOLFSSL_HASH_FLAGS`

### `--disable-hashflags`

 

### `--enable-defaultdhparams`

Enables option for default dh parameters (default: disabled) 

### `--disable-defaultdhparams`

 

#### Removes
- `HAVE_DH_DEFAULT_PARAMS`

### `--enable-linuxkm-lkcapi-register`

Register wolfCrypt implementations with the Linux Kernel Crypto API backplane. Possible values are "none", "all", "cbc(aes)", "cfb(aes)", "gcm(aes)", and "xts(aes)", or a comma-separate combination. (default: none) 

#### Removes
- `HAVE_DH_DEFAULT_PARAMS`

### `--disable-linuxkm-lkcapi-register`

 

#### Removes
- `HAVE_DH_DEFAULT_PARAMS`

### `--enable-context-extra-user-data`

Enables option for storing user-defined data in TLS API contexts, with optional argument the number of slots to allocate (default: disabled) 

#### Enables
- `HAVE_EX_DATA`

### `--disable-context-extra-user-data`

 

### `--enable-iotsafe`

Enables support for IoT-Safe secure applet (default: disabled) 

#### Enables
- `WOLFSSL_IOTSAFE`

### `--disable-iotsafe`

 

### `--enable-iotsafe-hwrng`

Enables support for IoT-Safe RNG (default: disabled) 

#### Enables
- `HAVE_IOTSAFE_HWRNG`

### `--disable-iotsafe-hwrng`

 

### `--enable-makeclean`

Enables forced "make clean" at the end of configure (default: enabled) 

### `--disable-makeclean`

 

### `--enable-usersettings`

Use your own user_settings.h and do not add Makefile CFLAGS (default: disabled) 

### `--disable-usersettings`

 

### `--enable-optflags`

Enable default optimization CFLAGS for the compiler (default: enabled) 

### `--disable-optflags`

 

### `--enable-sys-ca-certs`

Enable ability to load CA certs from OS (default: enabled) 

### `--disable-sys-ca-certs`

 

#### Removes
- `WOLFSSL_SYS_CA_CERTS`

### `--enable-dual-alg-certs`

Enable support for dual key/signature certificates in TLS 1.3 as defined in X9.146 (requires --enalbe-experimental) (default: disabled)

#### Removes
- `WOLFSSL_SYS_CA_CERTS`

### `--disable-dual-alg-certs`

 

### `--enable-rpk`

Enable support for Raw Public Key (RPK) RFC7250 (default: disabled) 

#### Enables
- `HAVE_RPK`

### `--disable-rpk`

 

### `--disable-openssl-compatible-defaults`

Disable OpenSSL compatible defaults when enabled by other options (default: enabled) 

### `--enable-openssl-compatible-defaults`

 

### `--enable-jobserver`

default=yes Enable up to # make jobs yes: enable one more than CPU count 

### `--disable-jobserver`

 

