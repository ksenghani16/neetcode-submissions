class Solution:
    def generateParenthesis(self,n):
        bracket=[""]*n*2
        result=[]
        self.solve(0,0,bracket,result)
        return result
    def solve(self,ind,total,bracket,result):
        if ind >=len(bracket):
            if total==0:
                result.append("".join(bracket))
            return
        if total>len(bracket)//2:
            return
        if total <0:
            return
        bracket[ind]="("
        s=total+1
        self.solve(ind+1,s,bracket,result)
        bracket[ind]=")"
        s=total-1
        self.solve(ind+1,s,bracket,result)
      
        
        