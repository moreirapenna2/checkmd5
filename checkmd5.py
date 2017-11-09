#!/usr/bin/env python

#this program check the MD5 SUM in the especified file and compares with a expected hash given by the user, saying if the file is corrupted or
#altered

import os
import hashlib

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    ERROR = '\033[31m'

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

arq = raw_input("File name\n> ")

hashmd5 = raw_input("Expected MD5 hash\n> ")

nhash = md5(arq)

if hashmd5 == nhash:
    print(bcolors.OKGREEN+"Correct hash"+bcolors.ENDC)
else:
    print(bcolors.ERROR +"Incorrect hash"+ bcolors.ENDC)
    print(bcolors.ERROR+"Current file hash:"+bcolors.ENDC)
    print nhash
