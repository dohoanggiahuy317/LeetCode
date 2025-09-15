# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [(nestedList, 0)]
        
    
    def next(self) -> int:
        nested_li, idx = self.stack.pop()
        return nested_li[idx].getInteger()
    
    def hasNext(self) -> bool:

        if not self.stack:
            return False
        
        while self.stack:
            nested_li, idx = self.stack.pop()
            sub_elem = nested_li[idx]
            if idx + 1 < len(nested_li):
                self.stack.append((nested_li, idx + 1))

            if not sub_elem.isInteger():
                self.stack.append((sub_elem.getList(), 0))
            else:
                self.stack.append((nested_li, idx))
                break
        # print(len(self.stack))
        # print()
        return True

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())