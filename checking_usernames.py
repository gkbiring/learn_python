current_users = ['caleb', 'bob', 'mike', 'sally', 'karen']
new_users = ['tom', 'betty', 'rob', 'caleb', 'bob']
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user.title()} has been taken.")
    else:
        print(f"{new_user.title()} is available.")
