class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        self.solve(0,[],candidates,target,result,len(candidates))
        return result
    def solve(self,index,subset,candidates,target,result,n):
        if target==0:
            result.append(subset.copy())
            return
        if target<0:
            return
        if index>=len(candidates):
            return
        for i in range(index,n):
            if i>index and candidates[i]==candidates[i-1]:
                continue
            subset.append(candidates[i])
            new_target=target-candidates[i]
            self.solve(i+1,subset,candidates,new_target,result,n)
            subset.pop()
            


            
            