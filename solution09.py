for i in range(1,333):
    for j in range(i,i+333):
        a,b,c=i,j,1000-i-j
        if (a*a + b*b == c*c):
            print(a,b,c,a*b*c)