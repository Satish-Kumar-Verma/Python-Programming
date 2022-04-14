
input_chr = ''

while True:
    input_chr = input("Enter a character : ")
    if input_chr.isalpha():
        break
input_chr = input_chr.lower()
print(input_chr)
if input_chr == 'a' or input_chr == 'e' or input_chr == 'i' or input_chr == 'o' or input_chr == 'u':
    print("It is a vowel!")

# if input_chr.__eq__('a'):
#     print("Vowel")

else:
    print("It is a consonant!")


