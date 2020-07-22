# Launching the enumeration of logins and passwords by selected parameters
# User may choose parameters according to his/her needs

import logic
import generators
import queries

logic.try_many_passwords_limited(
    login_generator=generators.popular_logins,
    password_generator=generators.popular_password,
    query=queries.request_local
)
