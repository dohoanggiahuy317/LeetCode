class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cs = Counter(students)

        rem = len(sandwiches)
        for sand in sandwiches:
            if cs[sand] == 0:
                break
            cs[sand] -= 1
            rem -= 1
        
        return rem