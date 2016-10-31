#!/usr/bin/python3

# Author    : Turfa Auliarachman
# Date      : October 23, 2016

from checker.BakuChecker import *
import sys
import os.path
import polib
import argparse

dictFile = os.path.dirname(os.path.realpath(__file__))+"/dict.txt"
checkerList = []

print("#"*70)
print("# Indonesian Kata Baku Checker" + " "*39 + "#")
print("# Author   : Turfa Auliarachman" + " "*38 + "#")
print("# Date     : October 23, 2016" + " "*40 + "#")
print("#"*70)
print()


parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type')
parser.add_argument('-i', '--input')

args = parser.parse_args()

if (len(sys.argv)<2):
    print("Usage:")
    print("{} <path-to-file>".format(sys.argv[0]))
else:
    checkerList.append(BakuChecker(dictFile))
    if (not(os.path.exists(args.input))):
        print("File {} not found.".format(args.input))
    else:
        f = open(args.input).readlines()
        if (len(sys.argv)==2):
            for i in range(0, len(f)):
                errList = []
                if (f[i][len(f[i])-1]=="\n"):
                    f[i] = f[i][:-1]

                for checker in checkerList:
                    errList += checker.check(f[i])

                for err in errList:
                    print("Checker       : {}".format(err.checkerDescription))
                    print("Line          : {}".format(i+1))
                    print("Original text : {}".format(err.original))
                    print("Message       : {}".format(err.message))
                    print()
        else:
            
            type = args.type
            if (type == 'po'):
                po = polib.pofile(args.input)
                for entry in po:
                    errList = []
                    for checker in checkerList:
                        errList += checker.check(entry.msgstr)

                    for err in errList:
                        print("Checker       : {}".format(err.checkerDescription))
                        print("Original text : {}".format(err.original))
                        print("Message       : {}".format(err.message))
                        print()		
            else:
                for i in range(0, len(f)):
                    errList = []
                    if (f[i][len(f[i])-1]=="\n"):
                        f[i] = f[i][:-1]
                    for checker in checkerList:
                        errList += checker.check(f[i])
                    for err in errList:
                        print("Checker       : {}".format(err.checkerDescription))
                        print("Line          : {}".format(i+1))
                        print("Original text : {}".format(err.original))
                        print("Message       : {}".format(err.message))
                        print()
				
					
