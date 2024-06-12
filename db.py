import json
from pathlib import Path

USERS_PATH = Path('./database/users.json')
STUDENTS_PATH = Path('./database/students.json')


class Database:
    def __init__(self):
        self.users = json.loads(
            open(USERS_PATH, mode='r', encoding='utf-8').read())

        self.records = json.loads(
            open(STUDENTS_PATH, mode='r', encoding='utf-8').read())

    def check_login(self, username, password):
        for user in self.users:
            if username == user['username']:
                if password == user['password']:
                    return True, 'Login success'
                else:
                    return False, 'Wrong password'
        return False, 'Login fail, Username not found'

    def get_all(self):
        return self.records

    def insert(self, data):
        if data['name'] == '':
            return "Please type a name"

        for r in self.records:
            if r['name'] == data['name']:
                return f"{data['name']} is exist"

        self.records.append(data)
        self.upload_all()
        return f"Add {data['name']} successful"

    def delete_by_name(self, name):
        for r in self.records:
            if r['name'] == name:
                self.records.remove(r)
                print(self.records)
                self.upload_all()
                return True, f"Delete {name}'s data successful"
        return False, f'{name} is not exist'

    def search_by_name(self, name):
        for r in self.records:
            if r['name'] == name:
                return True, r
        return False, f'{name} is not exist'

    def update_data(self, data):
        for r in self.records:
            if r['name'] == data['name']:
                r.update(data)  # Dir update function
                self.upload_all()
                return True, f"{data['name']} was update"
        return False, f"{data['name']} is not exist"

    def upload_all(self):
        with open(STUDENTS_PATH, mode='w', encoding='utf-8') as file:
            json.dump(self.records, file, ensure_ascii=False, indent=4)


db = Database()
if __name__ == '__main__':
    with open(USERS_PATH, mode='r', encoding='utf-8') as file:
        print(json.load(file))

    with open(file=STUDENTS_PATH, mode='r', encoding='utf-8') as file:
        print(json.load(file))
