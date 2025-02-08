class Solution:
    def find_minimum_sum_hitting_set(self, people):
        """
        Given a list of lists 'people', where each inner list contains numbers for a person,
        this function finds a subset of numbers (the hitting set) such that every person's list
        contains at least one number from the subset and the sum of the numbers in the subset is minimized.
        
        Returns:
            A tuple (hitting_set, total_sum) where 'hitting_set' is a set of numbers and 
            'total_sum' is the sum of those numbers.
        """
        # Get the unique numbers from all people
        numbers = sorted({num for person in people for num in person})
        best_sum = float('inf')
        best_set = None
        
        # Iterate over all possible subsets of numbers
        for r in range(1, len(numbers) + 1):
            for subset in itertools.combinations(numbers, r):
                subset_set = set(subset)
                # Check that each person's list has at least one number in the subset.
                if all(subset_set.intersection(person) for person in people):
                    current_sum = sum(subset)
                    if current_sum < best_sum:
                        best_sum = current_sum
                        best_set = subset_set
        return best_sum


    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        
        k = defaultdict(list)

        for tar in target:
            k[tar] = [float("INF")] * len(target)

        
        for j in range(len(target)):
            for i in range(len(nums)):
                tar = target[j]
                num = nums[i]

                needed = ((nums[i]//tar) + 1) * tar - nums[i] if nums[i] % tar != 0 else 0
                if needed < k[tar][-1]:
                    k[tar][-1] = needed
                    k[tar].sort()

        print(k)

        return self.find_minimum_sum_hitting_set(list(k.values()))