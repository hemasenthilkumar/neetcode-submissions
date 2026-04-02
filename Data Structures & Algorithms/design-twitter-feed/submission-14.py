class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # push latest tweets from every user + follower
        # go through each follower and push the ids in heap if they are recent
        self.followers[userId].add(userId)
        maxHeap = []
        res = []

        for follower in self.followers[userId]:
            # get the latest tweet
            if follower in self.tweets:
                index = len(self.tweets[follower])-1
                count, tweetid = self.tweets[follower][index]
                heapq.heappush(maxHeap, [count, tweetid, follower, index-1])
        
        while maxHeap and len(res) < 10:
            count, tweetid, follower, index = heapq.heappop(maxHeap)
            res.append(tweetid)
            print(index)
            if index >= 0:
                count, tweetid = self.tweets[follower][index]
                heapq.heappush(maxHeap, [count, tweetid, follower, index-1])

        return res           

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)        
