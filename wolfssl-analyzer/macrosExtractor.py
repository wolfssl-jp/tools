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
import argparse

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
    matched = re.findall(r'defined\s*\((\w+)\)', txt)
    return matched

def Search(txt) -> set[str]:
    """
    returns a list of macro names found in the given text.
    """
    macros = set()
    macros.update(SearchIfdef(txt))
    macros.update(SearchIfndef(txt))
    macros.update(SearchDefined(txt))
    return macros

def ExtractMacrosFromFiles(files:list[str]) -> set[str]:
    """
    Extract macros from source files.
    """
    macros = set()
    for file in files:
        try:
            with open(file, 'r') as f:
                txt = f.read()
                macros.update(Search(txt))
        except FileNotFoundError as e:
            e.filename = file
            raise e
    return macros

def ExcludeIncludeGuard(macros:set[str]) -> set[str]:
    """
    Exclude include guards from the given set of macros.
    """
    include_guards = set()
    for macro in macros:
        if re.match(r'^\w+_H$', macro):
            include_guards.add(macro)
    return macros - include_guards

def main():
    parser = argparse.ArgumentParser(description='Extract macros from source files.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--files', nargs='+', help='Source files to extract macros from.')
    group.add_argument('-d', '--directories', nargs='+', help='Directories to search for source files.')

    parser.add_argument('-e', '--extensions', nargs='+', help='File extension(s) to search for.')
    parser.add_argument('-r', '--recursive', action='store_false', help='Recursively search for source files in the given directory.')

    parser.add_argument('-i', '--include-guards', action='store_true', help='Exclude include guards(ends with "_H") from the result.')
    
    args = parser.parse_args()

    macros = set()
    if args.files:
        try:
            macros = ExtractMacrosFromFiles(args.files)
        except FileNotFoundError as e:
            print(f'{e.filename} : No such file exists.', file=sys.stderr)
            sys.exit(1)
        if not macros:
            print('No macros found.', file=sys.stderr)
    elif args.directories:
        if not args.extensions:
            print('You need to specify file extensions to search for.([-e, --extensions])', file=sys.stderr)
            sys.exit(1)
        for directory in args.directories:
            if os.path.isdir(directory):
                if args.recursive:
                    files = [filename for filename in os.listdir(directory) if os.path.isfile(os.path.join(directory, filename)) and filename.endswith(tuple(args.extensions))]
                    for file in files:
                        macros.update(ExtractMacrosFromFiles([os.path.join(directory, file)]))
                else:
                    for root, _, files in os.walk(directory):
                        for file in files:
                            if file.endswith(tuple(args.extensions)):
                                macros.update(ExtractMacrosFromFiles([os.path.join(root, file)]))
            else:
                print(f'{directory} : No such directory exists.', file=sys.stderr)
                sys.exit(1)
    else:
        print('You need to specify either files or directories.', file=sys.stderr)
        sys.exit(1)
    if args.include_guards:
        macros = ExcludeIncludeGuard(macros)
    for macro in sorted(macros):
        print(macro)
    return

if __name__ == '__main__':
    main()
