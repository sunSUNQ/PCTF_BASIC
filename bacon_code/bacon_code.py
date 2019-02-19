s = "bacoN is one of aMerICa'S sWEethEartS. it's A dARlinG, SuCCulEnt fOoD tHAt PaIRs FlawLE"
m = ''
for x in s:
    if 'a' <= x <= 'z':
        m += 'a'
    elif 'A' <= x <= 'Z':
        m += 'b'
    else:
        pass
print m
