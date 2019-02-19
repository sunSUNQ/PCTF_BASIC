old_code = "XYYY YXXX XYXX XXY XYY X XYY YX YYXX"

code_X = old_code.replace("X", ".").replace("Y", "-")
print "moose_code_X: " + code_X
code_Y = old_code.replace("X", "-").replace("Y", ".")
print "moose_code_Y: " + code_Y

code_moose_X = "JBLUWEWNZ"
print "moose_trans_X : " + code_moose_X
code_moose_Y = "BJYGDTDA#"
print "moose_trans_Y : " + code_moose_Y

for i in range(0, 9) :
    Caesar_code_X = ""
    for one in code_moose_X :
        #ord("A") = 65 ord("Z") = 90
        if (ord(one) + i) > 90 :
            Caesar_code_X += chr(ord(one) + i - 26)
        else :
            Caesar_code_X += chr(ord(one) + i)

    print Caesar_code_X




