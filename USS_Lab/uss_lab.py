string = "Ubiquitous System Security".lower()
string_ = string.split(" ")
string_fin = ""
num = 0
for one in string_ :
    string_fin += one
    num += 1
    if num != len(string_) :
        string_fin += "_"
string_finnal = "PCTF{" + string_fin + "}"
print (string_finnal)
    
