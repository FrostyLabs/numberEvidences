# Number Evidences

The pupose of this script is to rename files (typically evidences) based on some options provided in the command-line. 

For example, `file1.txt, file2.txt` could turn into `E-01_file1.txt, E-02_file2.txt` and so on. 

See the example options below! 

These are the options: 

- -p (--prefix): Will be the prefix before the numbers (e.g. 'E-')
- -c (--currhighest): If there are already existing files and you want to start the numbering from a higher number, you write the highest number. 
- -v (--verbose): Will give you verbose output in the terminal. 

```bash
$ ls 
README.md		evidences		numberEvidences.py	tmp

$ ls evidences/
file1.txt	file2.txt
```

```
$ python3 numberEvidences.py --help

usage: numberEvidences.py [-h] [-p PREFIX] [-c CURRENTHIGHEST] [-v]

options:
  -h, --help            show this help message and exit
  -p PREFIX, --prefix PREFIX
                        The prefix to be used -- e.g. E-
  -c CURRENTHIGHEST, --currhighest CURRENTHIGHEST
                        The currently highest number.
  -v, --verbose         Verbose output
```

```bash 

$ python3 numberEvidences.py --prefix 'E-' --currhighest 10 --verbose 

[INFO] Info to start
	Prefix to use: {prefix}
	Current Highest Number: {currHighest}
	Verbuse output: {verbose}
[+] Beginning!

[+] Listing folders!

	1 | tmp
	2 | evidences

[!] Which folder contains the evidence? 2

[+] Using folder:	evidences

[+] Checking files in:	/Users/oliver/Dropbox/University/20 KPMG/code/numberEvidences/evidences

[+] Found 2 files. Printing (up to) 5 files,
	- file1.txt
	- file2.txt
[+] Received 2 to rename

[+] Will rename followig 2 files. Printing (up to) 5 files,
	- E-011_file1.txt
	- E-012_file2.txt

```
Done 

```
$ ls evidences/ 
E-011_file1.txt	E-012_file2.txt
```
