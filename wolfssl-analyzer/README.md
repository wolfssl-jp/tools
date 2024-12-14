# Programs to analyze wolfssl
## configureOptionsComparator.py
For each configure option, get the difference from the default for the macro name to be defined.

"--options-file" must be a TXT file with one option name per line.

If there are any options skipped due to configure errors, "failed_options.txt" will be generated.

The output is generated in Markdown format.  
An example of the output can be found in `outputExample.md`.

### options
```
  -h, --help            show this help message and exit
  --wolfssl-path WOLFSSL_PATH
                        wolfSSL home dir path.
  --options-file OPTIONS_FILE
                        Text file with options to be executed. Cannot be used with --single-option or --opposite-option. If neither --options-file nor
                        --single-option is specified, all options will be executed.
  --single-option SINGLE_OPTION
                        Specify a single option to execute. Cannot be used with --options-file or --opposite-option.
  --opposite-option     If an option name contains "enable" or "disable," opposite option will automatically be executed. Cannot be used with --options-file or
                        --single-option.
  --output OUTPUT       Output file to save the results. Default: stdout
  --diff-only           Skips output for options that have no differences.
  --exclude-options EXCLUDE_OPTIONS
                        Text file with options to be excluded from execution.If you use --opposite-option, you should exclude both "enable" and "disable"
                        options.
```

### example
```
python3 configureOptionsComparator.py --wolfssl-path <<wolfssl home directory>> --output result.md
```

If you want to apply only some limited options, 
you can use `--options-file` or `--single-option`.  
When you use `--single-option` to specify a single option name, 
you should remove "--" at the beginning of the option name.
```
python3 configureOptionsComparator.py --wolfssl-path <<wolfssl home directory>> --output result.md --options-file options.txt

python3 configureOptionsComparator.py --wolfssl-path <<wolfssl home directory>> --output result.md --single-option enable-all
```

## configureOptionsExtractor.py
Get the list of valid options from the output of wolfssl/configure.

### options
```
  -h, --help            show this help message and exit
  --wolfssl-path WOLFSSL_PATH
                        Path to wolfssl source code
  --output OUTPUT       Output file to save the configure options. Default: stdout
  --description-output DESCRIPTION_OUTPUT
                        Output file to save the configure options with description. Default: None
  --output-opposite     If an option name contains "enable" or "disable," the program will automatically output the opposite option ("disable" or "enable").
                        Default: Disabled
  --print-error         Print error message while running configure command
```

### example
```
python3 configureOptionsExtractor.py --wolfssl-path <<wolfssl home directory>> --output output.txt
```
## headerComparator.py
Program that takes two headerfals as arguments and outputs the difference between the macros defined in the file.
Only the syntax "#define" is used to determine this.

### options
```
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Source header file
  -t TARGET, --target TARGET
                        Target header file
  -i INCREMENTAL_OUTPUT, --incremental-output INCREMENTAL_OUTPUT
                        Incremental output file. Default : increment.txt
  -d DECREMENTAL_OUTPUT, --decremental-output DECREMENTAL_OUTPUT
                        Decremental output file. Default : decrement.txt
```

### example
```
python3 -s source.h -t target.h
```

## macrosExtractor.py
Program that outputs a list of macros defined in a given file or directory.

### options
```
  -h, --help            show this help message and exit
  -f FILES [FILES ...], --files FILES [FILES ...]
                        Source files to extract macros from.
  -d DIRECTORIES [DIRECTORIES ...], --directories DIRECTORIES [DIRECTORIES ...]
                        Directories to search for source files.
  -e EXTENSIONS [EXTENSIONS ...], --extensions EXTENSIONS [EXTENSIONS ...]
                        File extension(s) to search for.
  -r, --recursive       Recursively search for source files in the given directory.
  -i, --include-guards  Exclude include guards(ends with "_H") from the result.
```

### example
targetfiles : All .h files under wolfssl directory (recursively)
```
python3 macrosExtractor.py -d <<wolfssl home directory>> -e .h -r
```