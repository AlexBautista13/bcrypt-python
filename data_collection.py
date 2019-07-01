import bcrypt 
import sqlite3

user_name = input("Please enter a name: ")
user_password = input("Please enter a Password")
age = int(input("Please enter your age"))

hashed_passowrd = bcrypt.hashpw(user_password.encode("utf8"), bcrypt.gensalt)

print(hashed_passowrd)
