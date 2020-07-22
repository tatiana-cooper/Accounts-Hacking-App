import json
from flask import Flask, request, Response

app = Flask(__name__)

# Statistics of attacks, will be dropped to zero after server restart
# 'attempts' - all attempts
# 'success' - successful attempts
stats = {
    'attempts': 0,
    'success': 0,
}

# Loads user's logins and passwords to compare with requests
with open('users.json') as users_file:
    users = json.load(users_file)


@app.route('/')
def hello():
    """ Returns the stats of cracking passwords and usernames """
    return f'Hello, user! stats={stats}'


@app.route('/auth', methods=['POST'])
def auth():
    """ Getting the username and password from request and returns the response with status code """

    stats['attempts'] += 1
    login = request.json['login']
    password = request.json['password']
    print(login, password)

    # if we found the existing username and password
    if login in users and users[login] == password:
        status_code = 200
        stats['success'] += 1
    else:
        status_code = 401

    return Response(status=status_code)


if __name__ == '__main__':
    app.run()
