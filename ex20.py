from sys import  argv
script,input_file = argv

def print_all(f):
    print(f.read())


def rewing(f):
    f.seek(0)
def print_a_line(line_cont,f):
    print(line_count, f.readline())

cureen_file = open(input_file)
print("First, Let's print the whole file:\n ")
print_all(cureen_file)

print("Now, Let's rewind, kind of like  a tape. ")
rewing(cureen_file)



