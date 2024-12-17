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
import json

def OptionsExtractor(configure_output:str, opposite:bool = False) -> dict[str, str]:
    """
    Extract configure options from the given configure output.
    """
    options = dict()
    valid_row = False
    option_buf = ""
    description_buf = []
    for line in configure_output.splitlines():
        words = line.strip().split()
        
        if words == ['Optional', 'Features:']:
            valid_row = True
        if not valid_row or not words:
            continue
        if words == ['Optional', 'Packages:']:
            if option_buf:
                if option_buf in options.keys():
                    if opposite and ('enable' in option_buf or 'disable' in option_buf):
                        options[option_buf]['Description'] = ' '.join(description_buf)
                else:
                    options[option_buf] = {'Description':' '.join(description_buf)}
                    if opposite and ('enable' in option_buf or 'disable' in option_buf):
                        if 'enable' in option_buf:
                            opposite_option = option_buf.replace('enable', 'disable')
                        else:
                            opposite_option = option_buf.replace('disable', 'enable')
                        options[opposite_option] = {'Description':''}
            break
        if words[0].startswith('--'):
            if option_buf:
                if option_buf in options.keys():
                    if opposite and ('enable' in option_buf or 'disable' in option_buf):
                        options[option_buf]['Description'] = ' '.join(description_buf)
                else:
                    options[option_buf] = {'Description':' '.join(description_buf)}
                    if opposite and ('enable' in option_buf or 'disable' in option_buf):
                        if 'enable' in option_buf:
                            opposite_option = option_buf.replace('enable', 'disable')
                        else:
                            opposite_option = option_buf.replace('disable', 'enable')
                        options[opposite_option] = {'Description':''}
            option_buf = re.split(r'[=\[\]()]', words[0])[0]
            description_buf = words[1:]
        else:
            description_buf += words

    return options

def main():
    parser = argparse.ArgumentParser(description='List all the configure options from wolfssl/configure')
    parser.add_argument('--wolfssl-path', required=True, help='Path to wolfssl source code')
    parser.add_argument('--output', help='Output file to save the configure options. Default: stdout')
    parser.add_argument('--description-output', help='Output file to save the configure options with description. Default: None')
    parser.add_argument('--both-enable-disable', action='store_true', help='If an option name contains "enable" or "disable," the program will automatically output the opposite option ("disable" or "enable"). Default: Disabled')
    parser.add_argument('--print-error', action='store_true', help='Print error message while running configure command')
    args = parser.parse_args()

    configure_command = ['sh', '-c', f'cd {args.wolfssl_path} && ./configure --help=short']
    result = subprocess.run(configure_command, capture_output=True, text=True)
    if result.returncode != 0:
        print('Error has occurred while running configure command')
        if args.print_error:
            print(result.stderr)
    output_configure = str(result.stdout)
    options = OptionsExtractor(output_configure, args.both_enable_disable)
    
    if args.output:
        with open(args.output, 'w') as f:
            for option in options.keys():
                f.write(option + '\n')
    else:
        for option in options.keys():
            print(option)
    
    if args.description_output:
        with open(args.description_output, 'w') as f:
            json.dump(options, f, indent=4)

if __name__ == '__main__':
    main()
