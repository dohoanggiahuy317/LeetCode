class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for i, (recipe, ingres) in enumerate(zip(recipes, ingredients)):
            for ingre in ingres:
                graph[ingre].append(recipe)
                
                indegree[ingre] = 0 if ingre not in indegree else indegree[ingre]
                indegree[recipe] += 1

        queue = deque([ingre for ingre in supplies if indegree[ingre] == 0])
        
        while queue:
            ingre = queue.popleft()

            for recipe in graph[ingre]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    queue.append(recipe)

        return [recipe for recipe in recipes if indegree[recipe] == 0]