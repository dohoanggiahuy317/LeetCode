class Twitter:

    def __init__(self):
        self.graph = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for follower_id in self.graph[userId]:
            if self.posts[follower_id]:
                idx = len(self.posts[follower_id]) - 1
                tweet_id, tweet_time = self.posts[follower_id][idx]
                heapq.heappush(heap, (-tweet_time, idx, tweet_id, follower_id))
        
        if self.posts[userId]:
            idx = len(self.posts[userId]) - 1
            tweet_id, tweet_time = self.posts[userId][idx]
            heapq.heappush(heap, (-tweet_time, idx, tweet_id, userId))


        ans = []
        while len(ans) < 10 and heap:
            _, idx, tweet_id, follower_id = heapq.heappop(heap)
            ans.append(tweet_id)

            idx -= 1
            if idx >= 0:
                tweet_id, tweet_time = self.posts[follower_id][idx]
                heapq.heappush(heap, (-tweet_time, idx, tweet_id, follower_id))

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.graph[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.graph[followerId]:
            self.graph[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)