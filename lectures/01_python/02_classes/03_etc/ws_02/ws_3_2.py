from user import User

def main():
    user1 = User('Alice', 'alice@example.com')
    user2 = User('Bob', 'bob@example.com')
    
    user1.display_info()
    user2.display_info()

if __name__ == "__main__":
    main()