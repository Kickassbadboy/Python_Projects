#
import random

s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
lengthpass = 12
password =  "".join(random.sample(s,lengthpass))
print password