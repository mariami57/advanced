import os

file_name = "text.txt"

try:
    file = open(file_name, "r")
    print("File found")

except FileNotFoundError:
    print("File is not found")