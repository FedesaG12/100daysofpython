class User:
    def  __init__(self,user_id,user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow (self, user):
        user.followers +=1
        self.following += 1

user1 = User("001","Fedesa")
user2 = User("002","Angelina")

user2.follow(user1)
print(user1.followers)