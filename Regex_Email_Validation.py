import re

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

email = input("Enter your email address : ")

if re.search(email_condition, email):
    print("Valid Email Address.")
else:
    print("Invalid Email Address.")