class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result=[]
        if not digits:
            return []
        char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        self.solve(0,[],result,digits,char_map)
        return result
    def solve(self,index,subset,result,digits,char_map):
        if index>=len(digits):
            result.append("".join(subset))
            return
        for char in char_map[digits[index]]:
            subset.append(char)
            self.solve(index+1,subset,result,digits,char_map)
            subset.pop()

            