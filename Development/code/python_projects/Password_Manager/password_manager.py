master_pwd = input("What is the master password? ")

def view():
    pass 

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:


while True:
    mode = input("Would you like to add a new password or view existing ones (view, or add), press 'q' to quit ? ")
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode")

#this is a comment