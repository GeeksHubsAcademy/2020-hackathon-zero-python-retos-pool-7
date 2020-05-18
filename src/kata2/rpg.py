#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    alphabet = string.ascii_letters + string.digits
    generatePass = ''.join(random.choice(alphabet) for i in range(passLen))

    return generatePass
