from passlib.hash import sha256_crypt

def exists(db,username):
    user = db["user"]
    x = user.find_one({ 'username' : username})
    print(x)
    return x

def register(db,data):
    user = db["user"]
    username = data['username']
    password = data['password']
    if exists(db,username) != None:
        print('User already exists')
        return
    hashed_password = sha256_crypt.encrypt(password)
    x = user.insert_one({'username' : username, 'password' : hashed_password})
    print('Registered with id : ' + str(x.inserted_id))

def login(db,data):
    username = data['username']
    password = data['password']
    x = exists(db,username)
    if x == None:
        print('User doesn\'t exist')
        return
    hashed_password = x['password']
    if sha256_crypt.verify(password, hashed_password) == True:
        print('Succesfully logged in')

def all_users(db):
    user = db['user']
    return user.find()


