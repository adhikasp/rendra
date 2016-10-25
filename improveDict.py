#!/usr/bin/python3

import sys
import os.path

if (len(sys.argv)!=3):
    print("Usage :")
    print("{} <src> <dst>".format(sys.argv[0]))
    exit()
elif (sys.argv[1]==sys.argv[2]):
    print("Because it is an experimental feature, you must output the result in the different file.")
    exit()

if (not(os.path.exists(sys.argv[1]))):
    print("File {} doesn't exists.".format(sys.argv[1]))
    exit()

dictList = []

for element in open(sys.argv[1]).readlines():
    element = element.split("|")

    if (len(element)!=2):
        print("Wrong input file format.")
        exit

    element[0] = element[0].strip().lower()
    element[1] = element[1].strip().lower()

    if (not(element in dictList)):
        dictList.append(element)

f = open(sys.argv[2],"w")

for element in dictList:
    f.write(element[0]+"|"+element[1]+"\n")

f.close()

print("Done!")
