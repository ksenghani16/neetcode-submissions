class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        left=0
        right=len(nums)-1
        mid=len(nums)//2
        left_array=self.sortArray(nums[:mid])
        right_array=self.sortArray(nums[mid:])
        return self.merge_array(left_array,right_array)
    def merge_array(self,left_array,right_array):
        n=len(left_array)
        m=len(right_array)
        i,j=0,0
        res=[]
        while i<n and j<m:
            if left_array[i]<=right_array[j]:
                res.append(left_array[i])
                i+=1
            else:
                res.append(right_array[j])
                j+=1
        while i<n:
            res.append(left_array[i])
            i+=1
        while j<m:
            res.append(right_array[j])
            j+=1
        return res
