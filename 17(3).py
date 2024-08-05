f = open('17.txt')
m = [int(i) for i in f]
arr = sorted(set(m))
n = len(arr)
mxSum,kx=0,0

for i in range(n):
    for j in range(i + 1, n):
        a = arr[i]
        b = arr[j]
        c = (a**2 + b**2)**0.5
        if c in arr:
            for z in range(2,int(c)):
                if c % z==0:
                    if (a%5 and b%5) or (a%5 and c%5) or (b%5 and c%5):
                        kx+=1
                        
                        ans=a+b+c
                        mxSum=int(max(mxSum,ans))
                    break
            
print(kx,mxSum)
