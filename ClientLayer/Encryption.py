import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Usage
if __name__ == "__main__":
    password = "mySecurePassword123"
    hashed_password = hash_password(password)
    print(hashed_password)
    is_valid = verify_password(password, hashed_password)