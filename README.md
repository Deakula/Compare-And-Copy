# Compare-And-Copy

A standalone script that compares the shallow contents of two directories, then copies or moves files unique to the first directory into a unique
subdirectory within the first directory.

## Usage
  compareandcopy.py [**-h**] [**-m**] [**-v**] **dir1** **dir2**

## Positional arguments
  ### **dir1**
    The first directory from which unique files, if any, are taken.
  ### **dir2**
    The second directory which the files of the first directory are compared against.

## Options
  ### **-h**, **--help**
    Shows the help message and exits
  ### **-m**, **--move**
    If this flag is set, any unique files found in the first directory will be moved instead of copied. (default: False)
  ### **-v**, **--verbose**
    If this flag is set, the script will be more verbose. (default: False)
