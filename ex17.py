from sys import argv
from os.path import exists
script,fromfile,tofile = argv
print(f"Coping from {fromfile} to {tofile}")
in_file = open(fromfile)
indate = in_file.read()
print(f"The  input file is {len(indate)} bytes long")

print(f"Does the output file exist?  {exists(tofile)}")
print("Ready ,hit RETURN to continue, CTRL-C to abort.")
input()
out_file = open(tofile,'w')
out_file.write(indate)
print("ALright, all done.")
out_file.close()
in_file.close()

