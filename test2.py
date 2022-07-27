# dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}


# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
    print(status)

# Strategy:  Create a new collection
active_users = {}
print(active_users)
for user, status in users.items():
    print(active_users)
    if status == 'active':
        active_users[user] = status