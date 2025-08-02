import csv
import json

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"User(id={self.user_id}, name={self.name}, email={self.email})"

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['user_id', 'name', 'email'])
            for user in self.users:
                writer.writerow([user.user_id, user.name, user.email])

    def load_from_csv(self, filename):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            self.users = [User(row[0], row[1], row[2]) for row in reader]

    def save_to_json(self, filename):
        with open(filename, mode='w') as file:
            json.dump([user.__dict__ for user in self.users], file)

    def load_from_json(self, filename):
        with open(filename, mode='r') as file:
            users_data = json.load(file)
            self.users = [User(**data) for data in users_data]