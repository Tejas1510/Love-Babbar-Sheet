# Dutch National Flag Problem
# https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/

# For segeratting 0,1,2,3
# https://github.com/ShikharSahu/AlgorithmsExperiments/blob/main/ForColorDNFlag/ExplainationDNF.md 
n=int(input())
a=list(map(int,input().split()))
low=0
high=n-1
mid=0
while(mid<=high):
    if(a[mid]==0):
        a[low],a[mid]=a[mid],a[low]
        low=low+1
        mid=mid+1
    elif(a[mid]==1):
        mid=mid+1
    else:
        a[mid],a[high]=a[high],a[mid]
        high=high-1
print(a)