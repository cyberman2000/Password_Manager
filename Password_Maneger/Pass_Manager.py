import random as rn
#pip install random2
import pyfiglet as pyfig
#pip install pyfiglet
import sys
#pip install os-sys
from colorama import *
#pip install colorama
print(Fore.BLUE + pyfig.figlet_format("Pass Manager"))
print(Fore.YELLOW + """                    Created by CyberMan                      """)
print("""                          Welcome                                   """)

print(Fore.GREEN + "1.Create a password for Email or Gmail ")
print("2.Create a password for Public WebSite ")
print("3.Create a password for Private WebSite")
print("4.Create a password for Vip Account")
print("5.Create a password for Bank Account")
print("6.Help")
print("7.About us")
print("8.Exit")
options=int(input(Fore.CYAN + "Please select one of the following options >>> "))
if options==1:
    print(Fore.BLUE + pyfig.figlet_format("Password Generator "))
    print(Fore.RED + "Example: example@Gmail.com ")
    mail_Name=input(Fore.CYAN + "Please enter your Email or Gmail name >>> ")
    print (Fore.BLUE + "1.Automatic")
    print (Fore.RED + "2.Manual ")
    choice=int(input(Fore.YELLOW + "Please select one of the options >>> "))
    if choice==1:
        Rand=rn.random()
        your_pass=str(Rand)
        finaly_pass=your_pass[2:5] + mail_Name[0:11]+your_pass[5:10]+"@&$$%*"
        print("Your powerful password >> ",finaly_pass)
        file_txt=open("REPORT_PASS.txt","a")
        file_txt.write(mail_Name)
        file_txt.write('\n')
        file_txt.write("Your powerful password >> ")
        file_txt.write(finaly_pass)
        file_txt.write('\n')
        file_txt.write("======================================================================================")
        file_txt.write('\n')
        file_txt.close()
    elif choice==2:
        save_pass=input("Please enter your password manually >>> ")
        save_pass+="$8@777%!+12%"
        print(Fore.GREEN + "We've added a few characters to the end of your password for your added security ====> ",Fore.BLUE + save_pass)
        file_txt=open("REPORT_PASS.txt","a")
        file_txt.write(mail_Name)
        file_txt.write('\n')
        file_txt.write("Your powerful password >> ")
        file_txt.write(save_pass)
        file_txt.write('\n')
        file_txt.write("======================================================================================")
        file_txt.write('\n')
        file_txt.close()
elif options==2:
    print(Fore.BLUE + pyfig.figlet_format("Password Generator "))
    print(Fore.RED + "Example: www.google.com")
    options_web=input(Fore.CYAN + "Please enter your Public WebSite name >>> ")
    print (Fore.BLUE + "1.Automatic")
    print (Fore.RED + "2.Manual ")
    choice=int(input(Fore.YELLOW + "Please select one of the options >>> "))
    if choice==1:
        Rand=rn.random()
        your_pass=str(Rand)
        finaly_pass=your_pass[3:5] + options_web[4:11]+your_pass[5:10]+"124578098"
        print("Your powerful password >> ",finaly_pass)
        file_txt=open("REPORT_PASS.txt","a")
        file_txt.write(options_web)
        file_txt.write('\n')
        file_txt.write("Your powerful password >> ")
        file_txt.write(finaly_pass)
        file_txt.write('\n')
        file_txt.write("======================================================================================")
        file_txt.write('\n')
        file_txt.close()
    elif choice==2:
        save_pass=input("Please enter your password manually >>> ")
        save_pass+="124578098"
        print(Fore.GREEN + "We've added a few characters to the end of your password for your added security ====> ",Fore.BLUE + save_pass)
        file_txt=open("REPORT_PASS.txt","a")
        file_txt.write(options_web)
        file_txt.write('\n')
        file_txt.write("Your powerful password >> ")
        file_txt.write(save_pass)
        file_txt.write('\n')
        file_txt.write("======================================================================================")
        file_txt.write('\n')
        file_txt.close()
elif options==3:
    print(Fore.BLUE + pyfig.figlet_format("Password Generator "))
    print(Fore.RED + "Example: youtube.com ")
    options_webPri=input(Fore.CYAN + "Please enter your Private WebSite name >>> ")
    Rand=rn.random()
    your_pass=str(Rand)
    finaly_pass=your_pass[0:5] + options_webPri[1:11]+your_pass[5:10]+"H%#!POmz$$t7"
    print("Your powerful password >> ",finaly_pass)
    file_txt=open("REPORT_PASS.txt","a")
    file_txt.write(options_webPri)
    file_txt.write('\n')
    file_txt.write("Your powerful password >> ")
    file_txt.write(finaly_pass)
    file_txt.write('\n')
    file_txt.write("======================================================================================")
    file_txt.write('\n')
    file_txt.close()
elif options==4:
    print(Fore.BLUE + pyfig.figlet_format("Password Generator "))
    print(Fore.RED + "Example: mybestbio.com")
    options_VIP=input(Fore.CYAN + "Please enter your Vip Account name >>> ")
    Rand=rn.random()
    your_pass=str(Rand)
    finaly_pass=your_pass[0:5] + options_VIP[0:11]+your_pass[5:10]+"Vi%@TPxcPQznBA$$$!782039781215"
    print("Your powerful password >> ",finaly_pass)
    file_txt=open("REPORT_PASS.txt","a")
    file_txt.write(options_VIP)
    file_txt.write('\n')
    file_txt.write("Your powerful password >> ")
    file_txt.write(finaly_pass)
    file_txt.write('\n')
    file_txt.write("======================================================================================")
    file_txt.write('\n')
    file_txt.close()
elif options==5:
    print(Fore.BLUE + pyfig.figlet_format("Password Generator "))
    print(Fore.RED + "Example: paypal")
    options_Bank=input(Fore.CYAN + "Please enter your Bank Account name >>> ")
    Rand=rn.random()
    your_pass=str(Rand)
    finaly_pass= your_pass[4:5] + options_Bank[2:11]+your_pass[5:10]+options_Bank[2:4].upper()+"y@o4u#r&11ank_ForM6ney&$$$710@$"
    print("Your powerful password >> ",finaly_pass)
    file_txt=open("REPORT_PASS.txt","a")
    file_txt.write(options_Bank)
    file_txt.write('\n')
    file_txt.write("Your powerful password >> ")
    file_txt.write(finaly_pass)
    file_txt.write('\n')
    file_txt.write("======================================================================================")
    file_txt.write('\n')
    file_txt.close()
elif options==6:
    print(Fore.BLUE + pyfig.figlet_format("HELP :) "))
    print(Fore.YELLOW + """This script helps you to generate a strong password and manage your password.
     All your passwords will be stored in a text file.""")
elif options==7:
    print(Fore.BLUE + pyfig.figlet_format("About us "))
    print(Fore.RED + "We are CyberMan, wait for our surprises")
elif options==8:
    print(Fore.RED + "Hope to see ")
    print("Thank you for your choice :)")
    sys.exit(0)
