# Author & Source code details

# Author - Ajay A Naik
# About code - the code can generate n number of strong passwords as per the user desired length.
# If you enjoyed using the code & want to DM me just drop a message @ Linkedin (available in my git hub profile section)🙂
# Total modules required -1


import random
print("Welcome to AJAY's random password generator, go ahead & try yoursel")
charac = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.;',?:|+_*&^%$#@!=-"

requirement = int(input ("How much passwords do you want  "))                                                                                  

length = int(input ("What should your password lenght  ")) 


for i in range(requirement):
    passwords = " "
    for j in range (length):
        passwords += random.choice(charac)
    print (passwords)

print ("\n Thank you for using the random password generator \n Have a awesome day")





    
















