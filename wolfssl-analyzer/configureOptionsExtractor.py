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

import re
import argparse
import subprocess

def OptionsExtractor(configure_output:str) -> list[str]:
    """
    Extract configure options from the given configure output.
    """
    options = []
    for line in configure_output.splitlines():
        if line.startswith('  --'):
            option = line.split()[0]
            words = line.strip().split()
            option = re.split(r'[=\[]', words[0])[0]
            options.append(option)
    return options

def main():
    parser = argparse.ArgumentParser(description='List all the configure options from wolfssl/configure')
    parser.add_argument('--wolfssl-path', required=True, help='Path to wolfssl source code')
    parser.add_argument('--output', help='Output file to save the configure options')
    parser.add_argument('--print-error', action='store_true', help='Print error message while running configure command')
    args = parser.parse_args()

    configure_command = ['sh', '-c', f'cd {args.wolfssl_path} && ./configure --help=short']
    result = subprocess.run(configure_command, capture_output=True, text=True)
    if result.returncode != 0:
        print('Error has occurred while running configure command')
        if args.print_error:
            print(result.stderr)
    output_configure = str(result.stdout)
    options = OptionsExtractor(output_configure)
    
    if args.output:
        with open(args.output, 'w') as f:
            for option in options:
                f.write(option + '\n')
    else:
        for option in options:
            print(option)

if __name__ == '__main__':
    main()
