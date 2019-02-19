strs = ""
for i in range(0,254) :
    f = open(str("mnt/"+ str(i)))
    s = f.readline()
    strs += s
    f.close()
print strs

