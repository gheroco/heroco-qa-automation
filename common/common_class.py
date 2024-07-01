import string
import random

class Common_class():
    def __init__(self):
        pass

    def get_random_string(self, length):
    # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str 