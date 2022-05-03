# Write a program to display all the common characters between two strings
# Return -1 if there are no matching characters


def find_common_characters(msg1, msg2):
    # Write your logic here
    result = ""
    for char in msg1:
        if char in msg2 and char not in result and char != " ":
            result += char
            if len(result) > 0:
                return result
            return -1


msg1 = "I like python"
msg2 = "Java is a very popular language"
# returns lieyon


common_characters = find_common_characters(msg1, msg2)
print(common_characters)
