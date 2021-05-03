values = {-1, 2, 3}
one = 0
if one in values:
    print(one)
else:
    estmd = 1000000
    while len(values) > 0:
        trl = values.pop()
        if abs(one-trl) < abs(one-estmd):
            estmd = trl
        elif abs(one-trl) == abs(one-estmd):
            if estmd > trl:
                estmd = trl
    print(estmd)