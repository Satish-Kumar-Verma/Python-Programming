

def check_anagram(input_str1, input_str2):
    if len(input_str1) == len(input_str2):
        for i in range(len(input_str1)):
            if input_str1.count(input_str1[i]) != input_str2.count(input_str1[i]):
                return False
        return True
    else:
        return False

input_str1, input_str2 = tuple(input("Enter two strings : ").split())
if check_anagram(input_str1, input_str2):
    print("They are anagram!")

else:
    print("They are not anagram!")