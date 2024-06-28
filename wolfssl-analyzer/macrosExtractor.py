#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2006-2024 wolfSSL Inc.
#
# This file is part of wolfSSL. (formerly known as CyaSSL)
#
# wolfSSL is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# wolfSSL is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

import os
import sys
import re
import json

def SearchIfdef(txt):
    """
    Extract macro names matching '#ifdef MACRO_NAME'.
    """
    matched = re.findall(r'#ifdef\s+(\w+).*\n', txt)
    matched = [macro.split()[0] for macro in matched]  # Remove the commented-out text following the macro name.
    return matched

def SearchIfndef(txt):
    """
    Extract macro names matching '#ifndef MACRO_NAME'.
    """
    matched = re.findall(r'#ifndef\s+(\w+).*\n', txt)
    matched = [macro.split()[0] for macro in matched]  # Remove the commented-out text following the macro name.
    return matched

def SearchDefined(txt):
    """
    Extract macro names matching 'defined(MACRO_NAME)'.
    '!defined(MACRO_NAME)' also matches.
    """
    return re.findall(r'defined\s*\((\w+)\)', txt)

def Search(txt):
    """
    returns a list of macro names found in the given text.
    """
    macros = []
    macros += SearchIfdef(txt)
    macros += SearchIfndef(txt)
    macros += SearchDefined(txt)
    macros = list(set(macros))  # Remove duplicates
    macros.sort()  # Sort the list by MACRO_NAME
    return macros

def wolfSSLSearch():
    """
    Search for macro names in the wolfSSL source code.
    This function should be called from the wolfssl directory.
    The result is saved in a JSON file named 'macros.json'.
    """

    # wolfssl/src
    srcdir = os.getcwd() + "/src"
    if not os.path.isdir(srcdir):
        print("src directory does not exist.")
        sys.exit(1)
    srcfiles = ["src/" + file for file in os.listdir(srcdir) if file.endswith(".c")]
    macros = dict()
    for srcfile in srcfiles:
        with open(srcfile, 'r') as f:
            txt = f.read()
        macros[srcfile] = Search(txt)

    # wolfcrypt/src
    cryptsrcdir = os.getcwd() + "/wolfcrypt/src"
    cryptsrcfiles = ["wolfcrypt/src/" + file for file in os.listdir(cryptsrcdir) if file.endswith(".c")]
    for cryptsrcfile in cryptsrcfiles:
        with open(cryptsrcfile, 'r') as f:
            txt = f.read()
        macros[cryptsrcfile] = Search(txt)

    with open("macros.json", 'w') as f:
        json.dump(macros, f)
    return

def main():
    wolfSSLSearch()

if __name__ == '__main__':
    main()
