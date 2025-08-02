from user_module import User, UserManager

# Create UserManager instance
user_manager = UserManager()

# Add users
user_manager.add_user(User('1', 'Alice', 'alice@example.com'))
user_manager.add_user(User('2', 'Bob', 'bob@example.com'))

# Save users to CSV
user_manager.save_to_csv('users.csv')

# Load users from CSV
user_manager.load_from_csv('users.csv')
for user in user_manager.users:
    print(user)

# Save users to JSON
user_manager.save_to_json('users.json')

# Load users from JSON
user_manager.load_from_json('users.json')
for user in user_manager.users:
    print(user)