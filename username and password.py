correct_user = "user"
correct_pass = "pass"
for i in range(3):
    user = input("Username: ")
    pwd = input("Password: ")
    if user == correct_user and pwd == correct_pass:
        print("Logged in!")
        break
    elif i < 2:
        print("Try again.")
    else:
        print("No more attempts.")
