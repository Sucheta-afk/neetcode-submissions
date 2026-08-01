class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for ele in operations:
            
            if ele=="C":
                stack.pop()
            elif ele=="D":
                stack.append(int(stack[-1])*2)
            elif ele=="+":
                x=int(stack[-1])
                y=int(stack[-2])
                
                stack.append(x+y)
            else :
                stack.append(ele)
                
        print(stack)
        sum=0
        for e in stack:
            sum+=int(e)
        return sum