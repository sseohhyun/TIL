class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content

    def __str__(self):
        return f"Post(user={self.user.username}, content={self.content})"