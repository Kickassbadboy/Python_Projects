#
import random

Alpha = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
lengthpass = 12
password =  "".join(random.sample(Alpha,lengthpass))
print password