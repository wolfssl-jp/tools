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

"""
The program takes the input from two header files and outputs the difference 
between the macros defined in those files.
"""

import re
import argparse
import sys

def ExtractMacros(header_file:str) -> set[str]:
    """
    Extract macro names from the given header file.
    """
    try:
        with open(header_file, 'r') as f:
            txt = f.read()
        return set(re.findall(r'#define\s+(\w+).*\n', txt))
    except FileNotFoundError as e:
        raise e

def main():
    parser = argparse.ArgumentParser(description='Compare the macros defined in two header files')
    parser.add_argument('-s', '--source', type=str, required=True, help='Source header file')
    parser.add_argument('-t', '--target', type=str, required=True, help='Target header file')
    parser.add_argument('-i', '--incremental-output', type=str, default="increment.txt", help='Incremental output file. Default : increment.txt')
    parser.add_argument('-d', '--decremental-output', type=str, default="decrement.txt", help='Decremental output file. Default : decrement.txt')
    args = parser.parse_args()

    try:
        source_macros = ExtractMacros(args.source)
        target_macros = ExtractMacros(args.target)

        with open(args.incremental_output, 'w') as f:
            for macro in target_macros - source_macros:
                f.write(macro + '\n')
        with open(args.decremental_output, 'w') as f:
            for macro in source_macros - target_macros:
                f.write(macro + '\n')
    except FileNotFoundError as e:
        print(f'{e.filename} : No such file exists', file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
