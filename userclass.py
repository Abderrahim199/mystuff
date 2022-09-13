def binarySearch(target , nums):
    if nums == []:
        return 0
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low + high)//2
        if low == high:
            return mid
        elif nums[mid].username > target:
            high = mid -1
        elif nums[mid].username < target:
            low = mid +1
        
    return mid






# class for the user.
class User():
    def __init__(self,name,username,email):
        self.name = name
        self.username = username
        self.email = email
    def __repr__(self):
        return "User(name = {} , username = {} , email = {} ".format(self.name,self.username,self.email)

    def __str__(self):
        return self.__repr__()





class DataBase():
    def __init__(self):
        self.users = []


    def insert(self, user):
        i = binarySearch(user.username,self.users)
        self.users.insert(int(i), user)
        
    def find(self, username):
        i = binarySearch(username, self.users)
        if self.users[i].username == username:
            return self.users[i]
    

    
    def update(self,user):
        target = self.find(user.username)
        if target != None:
            target.name,target.email = user.name,user.email

    def listall(self):
        return self.users









akash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')


users = [akash,biraj,hemanth,jadhesh,siddhant,sonaksh,vishal]
# -----------------------------------------------:



mydata = DataBase()
for user in users:
    mydata.insert(user) # inserting the users!!

print(mydata.listall())
print(mydata.find('Biraj Das'))

