import string
password = list(input('Enter a password: '))
count = 0
qualifications = ["lowercase", "uppercase", "digit", "special"]
for char in password:
    count = count+1
    if char in string.ascii_lowercase:
        if 'lowercase' in qualifications:
            qualifications.remove("lowercase")
    elif char in string.ascii_uppercase:
        if 'uppercase' in qualifications:
            qualifications.remove("uppercase")
    elif char in string.digits:
        if 'digit' in qualifications:
            qualifications.remove("digit")
    else:
        if 'special' in qualifications:
            qualifications.remove("special")
if count < 9:
        print('Your password must be at least 9 characters.')
if qualifications == []:
    print('Success, you have a strong password')
else:
    qualneeded = ", ".join(qualifications)
    print('Error: Enter a stronger password. You must include the following characters: ', qualneeded)


    

