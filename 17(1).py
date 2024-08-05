f = open('17.txt')
m = [int(i) for i in f]
arr = sorted(set(m))
n = len(arr)
mx,k=0,0
for i in range(n):
    for j in range(i + 1, n):
        a = arr[i]
        b = arr[j]
        c = (a**2 + b**2)**0.5
        if c in arr:
            ans=a+b+c
            k+=1
            mx=int(max(mx,ans))
print(k,mx)

