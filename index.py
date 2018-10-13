from flask import Flask
import pymongo
import user

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["blog_database"]

app = Flask(__name__)

@app.route('/')
def index():
    #get 10 published blogs and display
    return '10 published user blogs'

@app.route('/register')
def register():
    #read form data using post and redirect to home page if registered, else show error
    return 'register'

@app.route('/login')
def login():
    #read form data and login, send to home page, else thorow error
    return 'login'

@app.route('/users')
def users():
    #display list of users in sorted order with hyperlink
    return 'users'

@app.route('/user/<username>')
def user_blogs(username):
    #get published blogs by that user and display, give edit options if logged in with that username
    return 'user_blogs'

@app.route('/user/<username>/<int:id>')
def user_blog(id):
    #check if published blog, display the blog
    return 'single_blog'


user.login(db,{'username' : 'lo23432l', 'password' : '1234'}) 

if __name__ == '__main__':
    app.run(debug = True)

#give like and comment features as well

