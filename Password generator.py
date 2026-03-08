import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

n = int(input("Enter length: "))

password = "".join(random.sample(chars,n))

print("Generated Password:", password)