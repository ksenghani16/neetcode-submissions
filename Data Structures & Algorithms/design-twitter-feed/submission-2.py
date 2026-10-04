class Twitter:

    def __init__(self):
        self.timer=0
        self.following=defaultdict(set)
        self.user_tweets=defaultdict(list)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.timer,tweetId))
        self.timer+=1
    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        heap=[]
        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            tweets=self.user_tweets[followeeId]
            if tweets:
                last_idx=len(tweets)-1
                time,tweetId=tweets[last_idx]
                heapq.heappush(heap,(-time,tweetId,followeeId,last_idx))
        while heap and len(res)<10:
            neg_time,tweetId,followeeId,idx=heapq.heappop(heap)
            res.append(tweetId)
            if idx>0:
                next_time,next_tweetId=self.user_tweets[followeeId][idx-1]
                heapq.heappush(heap,(-next_time,next_tweetId,followeeId,idx-1))
        return res

            
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId!=followerId and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

        
