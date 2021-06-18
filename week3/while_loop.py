f = open("C:\learn-automation\learn-python-kirk\week2\show_version.txt")
i=0

while i<=5:
    print("Hello")
    print("world")
    print(f.readline())
    i+=1
f.close
f.seek(0)
print("-"*80)
j=0
while j<=5:
    line = f.readline()
    line = line.strip()
    print(line)
    j+=1
