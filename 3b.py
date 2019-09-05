import string
import random

def randompassword():
    password=random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)

    chars=string.ascii_uppercase+string.ascii_lowercase+string.digits+'!@#$%^&*()_+'
    size=random.randint(4,8)
    rest=''.join(random.choice(chars) for x in range(size))
    password+=rest


    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)

    return password

print(randompassword())
