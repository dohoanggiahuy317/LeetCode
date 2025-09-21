class Movie:
    def __init__(self, id, shop, price):
        self.id = id
        self.shop = shop
        self.price = price
        self.avail = True

    def __lt__(self, other):
        return (self.price, self.shop) < (other.price, other.shop)
    
    def __eq__(self, other):
        return s(self.price, self.shop) == (other.price, other.shop)

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        # movie: shop, price, avail
        self.movies_tracker = defaultdict(list) # -> 
        self.inventory = defaultdict(dict)

        self.rented_tracker = [] # -> [movie_obj, ...j

        for shop, movie, price in entries:
            movie_obj = Movie(movie, shop, price)
            heapq.heappush(self.movies_tracker[movie], movie_obj)
            self.inventory[movie][shop] = movie_obj

    def search(self, movie: int) -> List[int]:
        temp = []
        ans = []
        while len(ans) < 5 and self.movies_tracker[movie]:
            movie_obj = heapq.heappop(self.movies_tracker[movie])
            
            if movie_obj.avail:
                ans.append(movie_obj.shop)
            else:
                temp.append(movie_obj)

        for movie_obj in temp:
            heapq.heappush(self.movies_tracker[movie], movie_obj)

        return ans

    def rent(self, shop: int, movie: int) -> None:
        movie_obj = self.inventory[movie][shop]
        movie_obj.avail = False
        heapq.heappush(self.rented_tracker, movie_obj) 

    def drop(self, shop: int, movie: int) -> None:
        self.inventory[movie][shop].avail = True

    def report(self) -> List[List[int]]:
        temp = []
        ans = []
        while len(ans) < 5 and self.rented_tracker:
            movie_obj = heapq.heappop(self.rented_tracker)
            
            if not movie_obj.avail:
                ans.append([movie_obj.shop, movie_obj.id])
            else:
                temp.append(movie_obj)

        for movie_obj in temp:
            heapq.heappush(self.rented_tracker, movie_obj)

        return ans


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()