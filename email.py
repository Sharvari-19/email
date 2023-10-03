name=input("Enter your name: ")
email=input("Enter your email: ")
password=input("Enter your password: ")
if not name:
        print("Error Name cannot be empty.")
if '@' not in email:
        print("Error Missing '@' symbol.")

if len(password) < 8:
        print("Error: Password length must be at least 8 characters.")
   print("Name:", name)
    print("Email:", email)
    print("Password:", password)
