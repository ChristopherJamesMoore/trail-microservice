import requests

AUTH_API = "https://web.socem.plymouth.ac.uk/COMP2001_CMoore/auth/api/users"

def get_user_role(email: str):
    """Fetch user role from Authenticator API. 
    Here we stub: Grace = admin, others = user.
    """
    if email == "grace@plymouth.ac.uk":
        return "admin"
    return "user"

