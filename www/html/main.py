import sys
import functions
import os

argument = sys.argv[1]

if argument == "-src":
    functions.waitFinger()
elif argument == "-add":
    functions.addFinger()
elif argument == "-del":
    functions.removeFinger(sys.argv[2])
elif argument == "-sqlSrc":
    functions.sqlSearch()
elif argument == "-sqlAdd":
    functions.sqlEnroll(sys.argv[2])
else:
    print argument
