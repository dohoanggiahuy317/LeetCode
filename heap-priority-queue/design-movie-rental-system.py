class Movie:
    def __init__(self, movie, shop, price):
        self.movie = movie
        self.shop = shop
        self.price = price
        self.avail = True

    def __lt__(self, other):
        return (self.price, self.shop, self.movie) < (other.price, other.shop, other.movie)
    
    def __eq__(self, other):
        return (self.price, self.shop, self.movie) == (other.price, other.shop, other.movie)

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
            temp.append(movie_obj)
            if movie_obj.avail:
                ans.append(movie_obj.shop)

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
        seen = set()
        
        while len(ans) < 5 and self.rented_tracker:
            movie_obj = heapq.heappop(self.rented_tracker)
            temp.append(movie_obj)
            
            if not movie_obj.avail and (movie_obj.shop, movie_obj.movie) not in seen:
                ans.append([movie_obj.shop, movie_obj.movie])
                seen.add((movie_obj.shop, movie_obj.movie))
        
        for movie_obj in temp:
            heapq.heappush(self.rented_tracker, movie_obj)
            
        return ans

        return ans


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()