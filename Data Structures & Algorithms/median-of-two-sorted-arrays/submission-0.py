class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A,B = B, A
        total = len(A) + len(B)
        half = total // 2
        # smaller array
        low , high = 0, len(A)-1

        while True:
            # calculate mid first for finding the left partition
            mid_A = low + ((high-low)//2)
            mid_B = half - mid_A - 2

            # check for out of bounds
            ALeft = A[mid_A] if mid_A >=0 else float('-inf')
            ARight = A[mid_A+1] if mid_A + 1 < len(A) else float('inf')
            BLeft = B[mid_B] if mid_B >=0 else float('-inf')
            BRight = B[mid_B+1] if mid_B + 1 < len(B) else float('inf')

            if ALeft <= BRight and BLeft <= ARight:
                # we have found the left partition correctly
                # if odd
                if total % 2 != 0:
                    median = min(ARight, BRight)
                # if even
                else:
                    # Max of left + Min of Right
                    median = (max(ALeft, BLeft) + min(ARight,BRight))/2
                return median
            elif ALeft > BRight:
                high = mid_A - 1
            else:
                low = mid_A + 1

