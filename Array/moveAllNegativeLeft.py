n=int(input())
a=list(map(int,input().split()))
low=0
high=n-1
while(low<=high):
    if(a[low]<0):
        low=low+1
    else:
        a[low],a[high]=a[high],a[low]
        high=high-1
print(a)