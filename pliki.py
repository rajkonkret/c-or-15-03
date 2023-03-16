# print(open.__doc__)

# #'r'       open for reading (default)
# 'w'       open for writing, truncating the file first
# 'x'       create a new file and open it for writing
# 'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing)
with open('test.log', 'w', encoding='utf-8') as f:
    f.write("Radek\n")
    f.write("Daria\n")
    f.write("Michał\n")
a = 'a'
file = 'test.log'
with open(file, 'a', encoding='utf-8') as fh:
    fh.write("Dodane")

with open('test.log', 'r', encoding='utf-8') as fs:
    lines = fs.read()
    print(lines)
    print(type(lines))

with open('test.log', 'r') as files:
    for x in files:
        print(x)
# 15:00
