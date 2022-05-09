import filecmp
import os
from os import listdir, mkdir
from os.path import isfile, join
import shutil
import sys
import uuid


def main():
    dir1, dir2, move = None, None, False

    try:
        if sys.argv[1] == "-help":
            # Display Help Text
            return

        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
        move = sys.argv[3]
    except:
        if dir1 is None:
            dir1 = input("Enter the path for directory 1: ")
        if dir2 is None:
            dir2 = input("Enter the path for directory 2: ")

    unique = join(dir1, f"Unique_{uuid.uuid4()}")
    common = [fi for fi in listdir(dir1) if isfile(join(dir1, fi))]
    cmp = filecmp.cmpfiles(dir1, dir2, common, shallow=True)

    mkdir(unique)

    for fi in cmp[2]:
        if fi not in cmp[1]:
            print(f"{'Moving' if move else 'Copying'} {join(unique, fi)}...")
            b4Aft = (join(dir1, fi), join(unique, fi))

            if move:
                os.rename(*b4Aft)
            else:
                shutil.copyfile(*b4Aft)

            print(f"{b4Aft[1]} {'moved' if move else 'copied'}!")


if __name__ == '__main__':
    main()
