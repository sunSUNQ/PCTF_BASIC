secret_str = "jeihjiiklwjnk{ljj{kflghhj{ilk{k{kij{ihlgkfkhkwhhjgly"
result = ""
for one in secret_str :
    v = ord(one)
    if v > 100 & v <= 149 :
        v -= 53
        result += chr(v)
    elif v < 53 : 
        result += " " 
print result.decode("hex")

# other people's code
import string
cipher = 'jeihjiiklwjnk{ljj{kflghhj{ilk{k{kij{ihlgkfkhkwhhjgly'
l = map(ord, cipher)
dic = string.printable
f1 = lambda x: chr(x - 53)
def f2(x):
    for i in dic:
        if ord(i) + ord(i) % 11 == x:
            return chr(i)

def f3(x):
    for i in dic:
        if ord(i) - ord(i) % 61 == x:
            return chr(i)

def crack():
    ans = ''
    for i in l:
        try:
            ans += f1(i)
        except:
            pass
         
        try:
            ans += f2(i)
        except:
            pass
             
        try:
            ans += f3(i)
        except:
            pass
    return ans
# print crack()
print crack().decode('hex')


