class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {} # food -> cuisine
        self.food_to_rating = {} # food -> rating
        self.cuisine_to_heap = {} # cuisine -> max heap [(-rating, food)]

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating

            if cuisine not in self.cuisine_to_heap:
                self.cuisine_to_heap[cuisine] = []

            # push to heap
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        # push new record
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_to_heap[cuisine]

        # lazy deletion: ensure top is correct
        while heap:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            else:
                heapq.heappop(heap) # remove outdated


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)