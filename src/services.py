from flask import request
import random


def add_number():
    if request.get_json()["number"].isdigit() : #handling of the edge case where a user types a string
        number  = int(request.get_json()["number"])
        # Declaring filename
        filename = 'numbers.txt'
        file_object = open(filename, 'a')
        file_object.write(str(number) + '\n')
        file_object.close()
        return {}
    else:
        return {}

def sample_10():
    lines = open('numbers.txt').read().splitlines()
    if len(lines)==0: #handling of the edge case where a user dosen't add a number and wants to sample 10 numbers
        pass
        return []
    else:
        myline =random.choices(lines, k=10)
        return myline
