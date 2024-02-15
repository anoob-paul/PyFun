
class ArrayMerge:
    
    def merge(nums1, m: int, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length =m+n-1
        p= m-1
        q=n-1

        while (p>=0 and q>=0):
            if (nums1[p] > nums2[q]):
                nums1[length] = nums1[p]
                p-=1
            else:
                 nums1[length]= nums2[q]
                 q-=1
            length-=1

        while (q>=0):
            nums1[length]  =  nums2[q]
            q-=1
            length-=1

    nums1=[1,2,3,0,0,0]
    m=3
    nums2=[2,5,6]
    n=3

    merge(nums1,m,nums2,n)              

        