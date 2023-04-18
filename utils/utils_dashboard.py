# function that increment number of visits
def increment_visit(user):
    user["visits"] = user["visits"] + 1
    return user


