import argparse
from click import secho
import filecmp
import os
from os import listdir, mkdir, path
from os.path import isfile, join
import shutil
import uuid


dir1, dir2, move, verbose = None, None, False, False


def parse():
    global dir1, dir2, move, verbose

    parser = argparse.ArgumentParser(
        description="A standalone script that compares the shallow contents of"
        " two directories, then copies or moves files unique to the first"
        " directory into a unique subdirectory within the first directory.",

        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "dir1",
        help="The first directory from which unique files, if any, are taken."
    )
    parser.add_argument(
        "dir2",
        help="The second directory which the files of the first"
        " directory are compared against."
    )
    parser.add_argument(
        "-m", "--move",
        help="If this flag is set, any unique files found in the first"
        " directory will be moved instead of copied.",
        action="store_true",
        default=False
    )
    parser.add_argument(
        "-v", "--verbose",
        help="If this flag is set, the script will be more verbose.",
        action="store_true",
        default=False
    )

    args = parser.parse_args()

    if not path.isdir(args.dir1):
        secho(
            "Value provided for Directory 1 is not a valid directory!\n",
            fg="red"
        )

    if not path.isdir(args.dir2):
        secho(
            "Value provided for Directory 2 is not a valid directory!",
            fg="red"
        )

    if not path.isdir(args.dir1) or not path.isdir(args.dir2):
        exit(1)

    dir1, dir2, move, verbose = args.dir1, args.dir2, args.move, args.verbose


def main():
    global dir1, dir2, move, verbose

    unique = join(dir1, f"Unique_{uuid.uuid4()}")

    secho("Creating directory comparison...\n" if verbose else "", fg="blue")
    common = [fi for fi in listdir(dir1) if isfile(join(dir1, fi))]
    cmp = filecmp.cmpfiles(dir1, dir2, common, shallow=True)

    secho(
        f"Creating unique directory \"{unique}\"...\n" if verbose else "",
        fg="blue"
    )

    mkdir(unique)

    for fi in cmp[2]:
        if fi not in cmp[1]:
            secho(f"{'Moving' if move else 'Copying'} {join(unique, fi)}...\n"
                  if verbose else "", fg="blue")
            b4Aft = (join(dir1, fi), join(unique, fi))

            if move:
                os.rename(*b4Aft)
            else:
                shutil.copyfile(*b4Aft)

            secho(
                f"{b4Aft[1]} {'moved' if move else 'copied'}!\n" if verbose else "",
                fg="green"
            )


if __name__ == '__main__':
    parse()
    main()
