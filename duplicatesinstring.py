# Write a python function, remove_duplicates() which accepts a string and removes all duplicate characters from the given string and returns it

def remove_duplicates(value):

    # Write your code here
    remove = ""
    for i in value:
        if i not in value:
            remove += i


print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))

# expected output 12345abz@#*
