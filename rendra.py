#!/usr/bin/python3

from checker.BakuChecker import *
from checker.PadananChecker import *
import sys
import os.path
import polib
import argparse

baku_dict_file = os.path.dirname(os.path.realpath(__file__))+"/dictionary/kata-baku.txt"
padanan_dict_file = os.path.dirname(os.path.realpath(__file__))+"/dictionary/padanan-kata.txt"
checkerList = []

print("#"*70)
print("# Indonesian Kata Baku Checker" + " "*39 + "#")
print("# Author   : Turfa Auliarachman" + " "*38 + "#")
print("# Date     : October 23, 2016" + " "*40 + "#")
print("#"*70)
print()


parser = argparse.ArgumentParser()
parser.add_argument('-t', '--file-type')
parser.add_argument('-i', '--input')
parser.add_argument(
    "--check-padanan-only",
    action="store_true",
    help="only check for padanan kata mistake")

args = parser.parse_args()

if (len(sys.argv)<2):
    print("Usage:")
    print("{} <path-to-file>".format(sys.argv[0]))
else:
    checkerList.append(PadananChecker(padanan_dict_file))
    if not args.check_padanan_only:
        checkerList.append(BakuChecker(baku_dict_file))

    if (not(os.path.exists(args.input))):
        print("File {} not found.".format(args.input))
    file_type = args.file_type
    if (file_type == 'po'):
        po = polib.pofile(args.input)
        for entry in po:
            errList = []
            for checker in checkerList:
                errList += checker.check(entry.msgid, entry.msgstr)

            [err.show() for err in errList]
