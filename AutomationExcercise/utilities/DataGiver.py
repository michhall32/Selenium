import random
import string

USERNAME = 'geralto'
PASSWORD = 'witcher'
CORRECT_EMAIL = 'geralto@ofRivia.com'
INCORRECT_EMAIL = 'geraltof@rivia'
NEW_EMAIL = 'geralto2@ofRivia.com'


INCORRECT_LOGIN_MESSAGE = 'Your email or password is incorrect!'
EMAIL_ALREADY_EXIST_MESSAGE = 'Email Address already exist!'
CONTACT_US_SUCCESS_MESSAGE = "Success! Your details have been submitted successfully."
FILE_PATH = 'C:\\Users\\Z6GLD\\Desktop\\Additional\\Skillsy\\Selenium\\AutomationExcercise\\utilities\\automationexcercise.png'


def getRandomData(length):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


