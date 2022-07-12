"""
    problem: We need to create a data structer which can store 100 million records and perform insertion, search, update and list operations efficiently.
"""

"""
    Input:
    The key inputs to our data structure are user profiles, which contain the username, name and email of a user.
"""

"""
    1. Insert: 
            A. Inserting into an empty database of users
            B. Trying to insert a user with a username that already exists
            C. Inserting a user with a username that does not exist
            D. ??? 
"""

"""
    The various functions can be implemented as follows:
    1. Insert: Loop through the list and add the new user at a position that keeps the list sorted.
    2. Find: Loop through the list and find the user object with the username matchinge the query.
    3. Update: Loop through the list, find the user object matching the query and update the details
    4. List: Return the list of usr objects
"""

class User:
    def __init__(self, username, name, email):
        self.username = username;
        self.name = name;
        self.email = email;
    
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email);

    def __str__(self):
        return self.__repr__();
    
    def introduce_yourself(self, guest_name):
        print(f"Hi {guest_name}, I'm {self.name}! Contact me at {self.email}");


class UserDatabase:
    def __init__(self):
        self.users = [];

    def insert(self, user):
        i = 0;
        while i < len(self.users):
            if self.users[i].username > user.username:
                break;
            i += 1;
        self.users.insert(i, user);

    def find(self, username):
        for user in  self.users:
            if user.username == username:
                return user;

    def update(self, user):
        target = self.find(user.username);
        target.name, target.email = user.name, user.email;

    def list_all(self):
        return self.users;

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com');
biraj = User('biraj', 'Biraj Das', 'biraj@example.com');
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com');
jadesh = User('jadesh', 'Jadesh Verma', 'jadesh@example.com');
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com');
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com');
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com');

users = [aakash, biraj, hemanth, jadesh, siddhant, sonaksh, vishal];

database = UserDatabase();
database.insert(hemanth);
database.insert(aakash);
database.insert(siddhant);
database.insert(biraj);

all_user = database.list_all();
database.update(User('siddhant', 'Rajib Hasan', 'hasan@example.com'));
user = database.find('siddhant');

print(user);



