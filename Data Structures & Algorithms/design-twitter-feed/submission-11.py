import heapq
class Twitter:

    def __init__(self):
        self.twitter = {}
        self.time = 0
        # userid: { follows:[], tweet: maxHeap}
        # maxheap - for posts [timestamp, tweet]
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.twitter:
            self.twitter[userId] = {'follows':set(), 'tweet':[]}
        self.twitter[userId]['tweet'].append([self.time, tweetId])

    def return_tweets(self, maxHeap):
        tweet = []
        k=0
        while maxHeap:
            if k == 10:
                return tweet
            _,tweets = heapq.heappop(maxHeap)
            tweet.append(tweets)
            k+= 1
        return tweet
        

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        for tweets in self.twitter[userId]['tweet']:
           heapq.heappush(maxHeap, [-tweets[0], tweets[1]])
        for users in self.twitter[userId]['follows']:
            tweets = self.twitter[users]['tweet']
            for t in tweets:
                heapq.heappush(maxHeap, [-t[0], t[1]])
        return self.return_tweets(maxHeap)

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followeeId not in self.twitter:
                self.twitter[followeeId] = {'follows':set(), 'tweet':[]}
            if followerId not in self.twitter:
                self.twitter[followerId] = {'follows':set(), 'tweet':[]}
            self.twitter[followerId]['follows'].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.twitter[followerId]['follows'].discard(followeeId)
        
