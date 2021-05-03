a='abcde'
rslt = list()
if len(a) > 0:
    if len(a) % 2 == 0:
        ntms = len(a)
        for i in range(0, ntms, 2):
            rslt.append(a[i:i+2])
    else:
        ntms = len(a) - 1
        for i in range(0, ntms, 2):
            rslt.append(a[i:i+2])
        rslt.append(a[ntms]+'_')
print(rslt)
