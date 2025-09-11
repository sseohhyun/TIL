# sns.py
from user import User
from post import Post

class SNS:
    def __init__(self):
        self.users = []
        self.posts = []

    def add_user(self, username, email):
        user = User(username, email)
        self.users.append(user)
        return user

    def add_post(self, user, content):
        post = Post(user, content)
        self.posts.append(post)
        return post

    def get_posts(self):
        return self.posts