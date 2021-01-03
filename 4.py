class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 == 0:
            if l2 % 2 == 1:
                return nums2[int(l2/2)]
            else:
                return (nums2[int(l2/2)-1]+nums2[int(l2/2)])/2
        if l2 == 0:
            if l1 % 2 == 1:
                return nums1[int(l1/2)]
            else:
                return (nums1[int(l1/2)-1]+nums1[int(l1/2)])/2
        
        p1 = p2 = 0
        rl = list()
        mid = int((l1+l2)/2)
        while p1 + p2 < mid+1:
            if (p1 >= l1):
                rl.append(nums2[p2])
                p2 += 1
                continue
            if (p2 >= l2):
                rl.append(nums1[p1])
                p1 += 1
                continue
            if (nums1[p1] <= nums2[p2]):
                rl.append(nums1[p1])
                p1 += 1
            else:
                rl.append(nums2[p2])
                p2 += 1
        
        if (l1+l2) % 2 == 1:
            return rl[mid]
        else:
            return (rl[mid-1]+rl[mid])/2
