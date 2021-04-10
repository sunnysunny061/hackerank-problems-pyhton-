def kangaroo(x1, v1, x2, v2):
    if (x1<x2 and v1<v2):
        print ('NO')
    for i in range(0,10000):
        x1 = x1 + v1
        x2 = x2 + v2
        if (x1==x2):
            print ('YES')
            break
    if (x1 != x2):
        print ('NO')

x1,v1,x2,v2 = map(int,input().split())
kangaroo(x1, v1, x2, v2)