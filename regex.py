email = input("what's your email").strip()

username, domain = email.split("@")

if username and domain.endswith(".com"):
    print("valid")
else:
    print("Invalid")
