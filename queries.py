import requests


def request_local(login, password):
    """
    This function sends requests to the server with password and login.
    :param login: user's username.
    :param password: user's password.
    :return: True if response status code - 200, otherwise returns False.
    """
    # Depends on which web-site account User wants to crack. The request format may be changed.
    # For current server format is shown below.

    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': login, 'password': password})
    return response.status_code == 200

