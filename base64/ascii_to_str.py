str = "GUYDIMZVGQ2DMN3CGRQTONJXGM3TINLGG42DGMZXGM3TINLGGY4DGNBXGYZTGNLGGY3DGNBWMU3WI==="
import base64
str = base64.b32decode(str)
lenth = len(str)
one = 0
string = ""
while True :
    if one + 2  <= lenth : 
        letter = str[one : one + 2]
        base0x = "0x" + letter
        string += chr( int( base0x, 16 ) )
        one += 2
    else :
        break
print (string)
