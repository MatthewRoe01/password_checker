import string
password = list(input('Enter a password: '))
count = 0
qualifications = ["lowercase", "uppercase", "digit", "special"]
lowercase = 0
uppercase = 0
digit = 0
special = 0
for char in password:
    count = count+1
    if char in string.ascii_lowercase:
        lowercase+= 1
        if 'lowercase' in qualifications:
            qualifications.remove("lowercase")
    elif char in string.ascii_uppercase:
        uppercase += 1 
        if 'uppercase' in qualifications:
            qualifications.remove("uppercase")
    elif char in string.digits:
        digit += 1
        if 'digit' in qualifications:
            qualifications.remove("digit")
    else:
        special += 1
        if 'special' in qualifications:
            qualifications.remove("special")
if count < 9:
        print('Your password must be at least 9 characters.')
if qualifications == []:
    print('Success, you have a strong password')
else:
    qualneeded = ", ".join(qualifications)
    print('Error: Enter a stronger password. You must include the following characters: ', qualneeded)
print('<------------------->')
print('Amount of lowercase letters:', lowercase)
print('Amount of uppercase letters:', uppercase)
print('Amount of digits:', digit)
print('Amount of special characters:', special)


    

