class Twitter:

    def __init__(self):
        self.followed = defaultdict(set) # dict<Set>
        self.tweets = defaultdict(list) # dict<List>
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feeds = list(self.tweets[userId])
        for entry in self.followed[userId]:
            feeds.extend(self.tweets[entry])
        feeds.sort(reverse=True, key=lambda x: x[0])
        return [entry[1] for entry in feeds[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followed[followerId]:
            self.followed[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)