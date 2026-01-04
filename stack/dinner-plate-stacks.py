class PlateStack:
    def __init__(self, idx):
        self.idx = idx
        self.li = []
        self.store = 0

class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left_avail_stack = []
        self.right_avail_stack = []
        self.curr_idx = -1
        self.idx2plate = {}

    def push(self, val: int) -> None:
        while self.left_avail_stack:
            idx = self.left_avail_stack[0]

            if self.idx2plate[idx].store < self.capacity:
                break
            
            heapq.heappop(self.left_avail_stack)
        
        if not self.left_avail_stack:
            self.curr_idx += 1
            plate_stack = PlateStack(self.curr_idx)
            heapq.heappush(self.left_avail_stack, self.curr_idx)
            self.idx2plate[self.curr_idx] = plate_stack

        left_idx = heapq.heappop(self.left_avail_stack)
        plate_stack = self.idx2plate[left_idx]
        plate_stack.li.append(val)
        plate_stack.store += 1

        heapq.heappush(self.right_avail_stack, -left_idx)

        if plate_stack.store < self.capacity:
            heapq.heappush(self.left_avail_stack, left_idx)


    def pop(self) -> int:
        while self.right_avail_stack and self.idx2plate[-self.right_avail_stack[0]].store == 0:
            heapq.heappop(self.right_avail_stack)

        if not self.right_avail_stack:
            return -1
        
        right_idx = -heapq.heappop(self.right_avail_stack)
        plate_stack = self.idx2plate[right_idx]
        ans = plate_stack.li.pop()
        plate_stack.store -= 1

        if plate_stack.store > 0:
            heapq.heappush(self.right_avail_stack, -right_idx)
        if plate_stack.store == self.capacity - 1:
            heapq.heappush(self.left_avail_stack, right_idx)

        return ans 
        

    def popAtStack(self, index: int) -> int:

        if index not in self.idx2plate:
            return -1
        
        plate_stack = self.idx2plate[index]
        if plate_stack.store == 0:
            return -1

        ans = plate_stack.li.pop()
        plate_stack.store -= 1

        if plate_stack.store == self.capacity - 1:
            heapq.heappush(self.left_avail_stack, index)

        if plate_stack.store > 0:
            heapq.heappush(self.right_avail_stack, -index)

        return ans 


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)