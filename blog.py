import pymongo

def find_top(db):
    blog = db['blog']
    count = 0
    result = []
    for i in blog.find():
        if count >= 10:
            break
        result.append(i)
    return result

def user_blogs(db,username):
    blog = db['blog']
    return blog.find({'username' : username})

def blog(db,username,title):
    blog = db['blog']
    return blog.find({'title' : title, 'username' : username})
        
