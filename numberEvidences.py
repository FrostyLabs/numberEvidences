#/usr/bin/python3

# Script:   numberEvidences.py
# Desc:     Enumerates and renames files based on inputs
# Author:   othornewill

import sys, os, re
import argparse

def list_files(path, verbose=False):
    """List files in directory"""
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break

    files = sorting_func(files)
    if verbose: 
        print(f"\n[+] Found {len(files)} files. Printing (up to) 5 files,")
        for i in files[:5]: 
            print(f"\t- {i}")
    
    return files


def sorting_func( l ): 
    """ Sort the given iterable in the way that humans expect.""" 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)


def rename_files(files, prefix, currHighest, path, verbose=False):
    """
    Takes the list of files and prepends the prefix
    The number is also used. 
    """ 
    renameFiles = []
    
    for i,j in enumerate(range(currHighest+1, currHighest+len(files)+1)):
        newID = str(j).zfill(3)
        newName = prefix + newID + "_" + files[i]
        renameFiles.append(newName)

    pathOriginal = [path + "/" + item for item in files]
    pathNew = [path + "/" + item for item in renameFiles]
    
    if verbose: 
        print(f"[+] Received {len(files)} to rename")
        print(f"\n[+] Will rename followig {len(files)} files. Printing (up to) 5 files,")
        for i in renameFiles[:5]: 
            print(f"\t- {i}")
        
    if len(files) != len(renameFiles):
        print("Something is wrong. Two dictionaries are not correct.")
        sys.exit()
    
    for i,_ in enumerate(renameFiles): 
        os.rename(pathOriginal[i], pathNew[i])


def print_info(prefix, currHighest, verbose):
    print("""[INFO] Info to start
\tPrefix to use: {prefix}
\tCurrent Highest Number: {currHighest}
\tVerbuse output: {verbose}
[+] Beginning!\n
[+] Listing folders!\n""")


def main(args):
    """Main Function"""
    prefix = args.prefix
    currHighest = args.currentHighest
    verbose = args.verbose
    directories = next(os.walk('.'))[1]

    print_info(prefix, currHighest, verbose)

    for i,j in enumerate(next(os.walk('.'))[1]): 
        print(f"\t{i+1} | {j}")

    folderNum = int(input(f"\n[!] Which folder contains the evidence? ")) - 1
    selectedFolder = directories[folderNum]
    renamePath = os.getcwd()+"/"+selectedFolder
    print(f"\n[+] Using folder:\t{selectedFolder}")
    
    if args.verbose: 
        print(f"\n[+] Checking files in:\t{renamePath}")

    files = list_files(renamePath, verbose)
    rename_files(files, prefix, currHighest, renamePath, verbose)

if __name__ == "__main__":
    """ This is executed when run from the command line """

    if not len(sys.argv) > 1:
        print("Usage: {} --help".format(sys.argv[0]))
        sys.exit()

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--prefix", type=str,  help="The prefix to be used -- e.g. E-", dest="prefix")
    parser.add_argument("-c", "--currhighest", type=int,  help="The currently highest number.", dest="currentHighest")
    parser.add_argument("-v", "--verbose", help="Verbose output", action="store_true")

    args = parser.parse_args()
    main(args)
