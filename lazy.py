import os
import sys
if len(sys.argv) == 1:
    # you can even change the size here
    size = "123345"
else:
    size = sys.argv[1]
SIZE = int(size)
if SIZE>100000000:
    print("Size must be smaller than 100000000")
    exit()
else:
    print("Timing the sort of an array with {} elements".format(size))
    print("\nJulia")
    os.system('cmd /c "julia cmd.jl {}"'.format(SIZE))
    print("\nJava")
    os.system('cmd /c"java cmd.java {}"'.format(SIZE))
    print("\nPython")
    os.system('cmd /c"python cmd1.py {}"'.format(SIZE))