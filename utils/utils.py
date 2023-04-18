import json


# define the username of the user whose visits we want to increment
def update_user_in_file(username):

    # read the data from the file
    with open('./data/users.json', 'r') as f:
        users = json.load(f)

    # find the user in the list
    for user in users:
        if user["username"] == username:
            # increment the user's visits
            user["visits"] += 1
            break

    # write the updated data back to the file
    with open('./data/users.json', 'w') as f:
        json.dump(users, f)

    # print a message to confirm that the file has been updated
    print("File has been updated!")
