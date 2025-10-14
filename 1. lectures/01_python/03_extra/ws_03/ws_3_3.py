from sns import SNS

# SNS 인스턴스 생성
sns = SNS()

# 사용자 생성
user1 = sns.add_user("john_doe", "john@example.com")
user2 = sns.add_user("jane_doe", "jane@example.com")

# 게시물 작성
post1 = sns.add_post(user1, "Hello, this is my first post!")
post2 = sns.add_post(user2, "Hi everyone, glad to be here!")

# 게시물 조회
posts = sns.get_posts()
for post in posts:
    print(post)