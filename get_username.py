with open('data/user_urls.txt', 'r') as f:
    usernames = []
    for line in f:
        username = line.split('/')[5]
        usernames.append(username)

