name=input("Enter Name:")
email=input("Enter Email:")
password=input("Enter Password:")
if not name:
    print("Error Name cannot be empty")
    if not '@'in email:
        print("Error Enter a valid email,@ missing")
        if len(password)<8:
            print("Error Password length less than 8 characters")