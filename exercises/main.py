class User:
    def __init__(self,name,surname,email):
        self.name = name
        self.surname = surname
        self.email = email
        self.followers = 0
user1 = User(name='Muhammed Hasan',surname='Karaaslan',email='mhkaraaslan05@gmail.com')
print(user1.name)
print(user1.surname)
print(user1.email)
user1.followers = 5
print(user1.followers)
user1.followers += 832107
print(user1.followers)