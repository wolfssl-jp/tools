# Programs to analyze wolfssl
## configureOptionsComparator.py
For each configure option, get the difference from the default for the macro name to be defined.

"--options-file" must be a TXT file with one option name per line.

If there are any options skipped due to configure errors, "failed_options.txt" will be generated.

### options
```
  -h, --help            show this help message and exit
  --wolfssl-path WOLFSSL_PATH
                        wolfSSL home dir path.
  --options-file OPTIONS_FILE
                        Text file with options to be executed.
                        If not provided, all options will be
                        executed
  --txtformat           Output data format. Enable to TXT,
                        disable to JSON. Default: Disable(JSON)
  --output OUTPUT       Output file to save the results.
                        Default: stdout
```

### example
```
python3 configureOptionsComparator.py --wolfssl-path <<wolfssl home directory>> --output result.json
```

## configureOptionsExtractor.py
Get the list of valid options from the output of wolfssl/configure.

### options
```
  -h, --help            show this help message and exit
  --wolfssl-path WOLFSSL_PATH
                        Path to wolfssl source code
  --output OUTPUT       Output file to save the configure options. Defaults: stdout
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