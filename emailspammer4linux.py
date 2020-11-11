
import smtplib
import os

os.system('clear')


print('''

 ####### #######    #    #     #    ####### ######   #####   #####  
    #    #         # #   ##   ##       #    #     # #     # #     # 
    #    #        #   #  # # # #       #    #     #       #       # 
    #    #####   #     # #  #  #       #    ######   #####   #####  
    #    #       ####### #     #       #    #   #         #       # 
    #    #       #     # #     #       #    #    #  #     # #     # 
    #    ####### #     # #     #       #    #     #  #####   #####  
                                                                    

                                                                    
''')


print('''

sign in with ur email account

''')

prot = input("Enter protocol (smtp.gmail.com for gmail): ")





uname = input("Enter Your Email: ")
upass = input("Enter Your password: ")
rmail = input("Enter victim\'s Email: ")
message = input("Enter the message you want to send: ")
threads1 = input("Enter The amount of threads you want to send: ")
s = smtplib.SMTP(prot, 587)

s.starttls()

s.login(uname, upass)

msg = message

for i in range(int(threads1)):
    s.sendmail(uname, upass, msg)
    print("spamming "+rmail)

s.quit()



