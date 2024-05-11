# make -f wolfssh.mk

WOLFSSH_ROOT=./wolfssh
WOLFSSL_ROOT=./wolfssl
LIBWOLFSSL = $(WOLFSSL_ROOT)/libwolfssl.a
LIBWOLFSSH = $(WOLFSSH_ROOT)/libwolfssh.a

OPT_FLAGS = -Os -g
INC_PATHS = -I$(WOLFSSH_ROOT) -I$(WOLFSSL_ROOT)
USER_SETTINGS = -DWOLFSSL_USER_SETTINGS -I.
#INC_OPTIONS   = -include $(WOLFSSL_ROOT)/wolfssl/options.h

OPT_APPLE = -framework CoreFoundation -framework Security

CFLAGS = $(OPT_FLAGS) $(INC_PATHS) $(WOLFSSH_FUNC) $(USER_SETTINGS) $(INC_OPTIONS)

SRC = $(WOLFSSH_ROOT)/src/agent.c \
	$(WOLFSSH_ROOT)/src/certman.c \
	$(WOLFSSH_ROOT)/src/internal.c \
	$(WOLFSSH_ROOT)/src/io.c \
	$(WOLFSSH_ROOT)/src/keygen.c \
	$(WOLFSSH_ROOT)/src/log.c \
	$(WOLFSSH_ROOT)/src/port.c \
	$(WOLFSSH_ROOT)/src/ssh.c \
	$(WOLFSSH_ROOT)/src/wolfscp.c \
	$(WOLFSSH_ROOT)/src/wolfsftp.c \
	$(WOLFSSH_ROOT)/src/wolfterm.c
OBJECT = $(SRC:.c=.o)

PROGRAM = $(WOLFSSH_ROOT)/examples/echoserver/echoserver

all: library program

library: $(LIBWOLFSSH)
$(LIBWOLFSSH): $(OBJECT)
	ar r $@ $(OBJECT)

$(OBJECT): %.o : %.c
	gcc -o $@ -c $^ $(CFLAGS)

program: $(PROGRAM)
$(PROGRAM): % : %.c
	gcc -o $@ $^ $(LIBWOLFSSH) $(LIBWOLFSSL) $(CFLAGS) $(OPT_APPLE)

clean:
	rm -f $(OBJECT)
	rm -f $(LIBWOLFSSH)
	rm -f $(PROGRAM)