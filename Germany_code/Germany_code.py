dic = {"A": 0b1000001, "B": 0b1000010, "C": 0b1000011, "D":0b1000100, "E": 0b1000101, "F": 0b1000110, "G": 0b1000111, "H": 0b1001000, "I": 0b1001001, "J": 0b1001010, "K": 0b1001011, "L":  0b1001100, "M": 0b1001101, "N": 0b1001110, "O":  0b1001111, "P": 0b1010000, "Q": 0b1010001, "R": 0b1010010,"S": 0b1010011, "T": 0b1010100, "U": 0b1010101, "V": 0b1010110, "W": 0b1010111, "X": 0b1011000, "Y": 0b1011001, "Z": 0b1011010}
sec_message = "000000000000000000000000000000000000000000000000000101110000110001000000101000000001"
#0000001 0010100 0010000 0000110 0010111
sec_key = "WELCOMETOCFF"
b = []
for i in range(0, len(sec_message)/ 7) :
    big_num = -7 - i*7
    small_num = -i*7
    if i == 0 :
        b.append(sec_message[-7:])
    else :
        b.append(sec_message[big_num: small_num])
#print b 
a = []
for one in sec_key:
    a.append(bin(dic[one]))
a.reverse()
#print a

len_a = len(a)
len_b = len(b)
if len_a > len_b : len_a = len_b
 
c = []
for one in range(0, len_a) :
    c.append(bin(int(a[one], 2) ^ int(b[one], 2)))
c.reverse()

result = ""
for one in c :
    for item in dic.keys() :
        if bin(dic[item]) == one :
            letter = item
            result += letter
print result
