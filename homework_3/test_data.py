import random

def generate_login():
    return "User_" + str(random.randint(1,999))

def generate_age():
    return random.randint(18, 65)

def generate_status():
    return random.choice(['ACTIVE', 'BLOCKED', 'INACTIVE'])

def generate_user():
    return {
        'username': generate_login(),
        'age': generate_age(),
        'status': generate_status()
    }
