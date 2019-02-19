num = 10000000
total = 0
now_num = 0
list_num = []
while True :
    if now_num <= num :
        if now_num % 3 == 0 or now_num % 5 == 0 :
            total += now_num
            list_num.append(now_num)
    else :
        break
    now_num += 1
#print (list_num)
print (total)

