# Kth smallest element 
class Solution:
    def kthSmallest(self,arr, k):
        arr1=sorted(arr)
        return arr1[k-1]