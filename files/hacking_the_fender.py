#codecademy challenge

import csv
import json

#create a new variable for compromised users

compromised_users = []

#open the csv file

with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)

    for password_row in password_csv:
        compromised_users.append(password_row['Username'])


with open('compromised_users.txt', 'w') as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user + '\n')


with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {'recipient' : 'The Boss', 'message': 'Mission Success'}
    json.dump(boss_message_dict, boss_message)

slash_null_sig = r''' 
_  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
'''

with open('new_password.csv', 'w') as new_password_obj:
    new_password_obj.write(slash_null_sig)


