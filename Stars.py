n = 9 
for i in range(1, n+1):
    #print(i)
    if i <= n/2:
        print('*' * i)
    else:
        print('*' * (n - i + 1))