class Solution:
   def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
       destination = max(x[2] for x in trips)
       pax_count = [0] * (destination + 1)
       for num_passenger, from_km, to_km in trips:
           for i in range(from_km, to_km):
               pax_count[i] += num_passenger
       return all(x <= capacity for x in pax_count)