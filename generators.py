def read_file(file):
    """
    Reads content of given file
    (.txt) -> (list)
    :param file: .txt file
    :return: content splitted by '\n'
    """
    with open(file) as f:
        content = f.read()
    return content.split('\n')


# list of the most popular passwords
passwords = read_file('10-million-password-list-top-1000000.txt')

# list of the most popular usernames
logins = read_file('top-10-million-usernames.txt')


def popular_password(state):
    """
    (int) -> (str, int)
    Returns current password and the next password's index
    :param state: current password's index
    :return: password with current index and next password's index
    """
    # if state is None then counting starts from the first password
    if state is None:
        state = 0

    # if state is >= length of passwords' list then password's index is None
    if state >= len(passwords) - 1:
        next_state = None

    # otherwise next password's index = current password's index + 1
    else:
        next_state = state + 1

    return passwords[state], next_state


def popular_logins(state):
    """
    (int) -> (str, int)
    Returns current login and the next login's index
    :param state: current login's index
    :return: login with current index and next login's index

    """

    # if state is None then counting starts from the first login
    if state is None:
        state = 0

    # if state is >= length of login' list then login's index is None
    if state >= len(logins) - 1:
        next_state = None

    # otherwise next login's index = current login's index + 1
    else:
        next_state = state + 1

    return logins[state], next_state


def brute_force(state):
    """
    Brute-force attack, enumeration of all possible passwords.
    :param state: digit which will be converted into password by algorithm
    :return: generated password from current digit and the next digit

    """

    # This algorithm takes digit (state) and generates password,
    # that will be a combination of characters from variable alphabet

    # possible password's characters
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'

    base = len(alphabet)

    if state is None:
        state = 0, 0

    i, length = state
    password = ''
    temp = i

    while temp > 0:
        c = temp // base
        r = temp % base
        password = alphabet[r] + password
        temp = c

    if len(password) < length:
        zeros_count = length - len(password)
        password = alphabet[0] * zeros_count + password

    if password.count(alphabet[-1]) == length:
        length += 1
        i = 0
    else:
        i += 1
    next_state = i, length

    return password, next_state
