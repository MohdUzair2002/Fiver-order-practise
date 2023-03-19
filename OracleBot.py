# import regex module
import re
# finalize email regex pattern
pattern = "^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$"

def verify_email(email: str):
    """function to verify email patterns"""
    verify = re.search(pattern, email)
    
    # check if verify object returns 
    # Match object or None
    if verify:
        print("Email verified")
    else:
        print("Email not verified")


email1 = "mohammad.uzair361@gmail.com"
verify_email(email1)