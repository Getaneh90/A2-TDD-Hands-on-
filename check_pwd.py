import random
import string

def check_pwd(pwd):
    if len(pwd) < 8 or len(pwd) > 20:
        return False

    if not any(char.islower() for char in pwd):
        return False


