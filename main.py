class User:
    def __init__(self, user_id, username):
        self.username = username
        self.id = user_id
        self.followers=0
        self.following=0

    def follow(self,user):
        user.followers+=1
        self.following+=1

user_1 = User("Angela","001")
user_2 = User("Jack","002")
print(user_1.id)
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)



