import random
import string
import os

 




# password genertor function
def generate_password(length):

 letter= string.ascii_letters
 digit= string.digits
 special_char=string.punctuation

 combined_characters = letter + digit + special_char

 password="".join(random.choices(combined_characters,k=length))
 return password



#password saving function
def save_password(website,password):
 with open("password.txt","a") as file:
  file.write(f"{website} : {password}\n")


  #view password function
def view_savedpassword():
 with open("password.txt") as file:
  line = file.readlines()
 if len(line)==0:
  print("no password saved yet")
 else:
  print("========== Saved Passwords ==========")
  for line in line:
      print(line.strip()) #removes \n from the file
  print("=====================================")


#search the password function
def search_password(website):
 with open("password.txt","r") as file:
  content=file.readlines()

  found = False
  for line in content:
   if website in line:
    print(f"Found..!{line.strip()}")
    found=True
    break
  if not found:
    print(f"no result found.!{website}")
  
  # delete the password function
def delete_password(website):
   with open("password.txt","r") as file:
    content = file.readlines()

    remaining=[]
    for line in content:
       if website not in line:
        remaining.append(line)

    with open("password.txt","w") as file:
     file.writelines(remaining)

    if len(content)== len(remaining):
     print(f"No password found..!{website}")
    else:
     print(f"password deleted..{website}")    
      
  

#Menu for choices
while(True):
 
 print("==========  Passwords Manager ==========")
 print("1.Generate Password")
 print("2.view Password")
 print("3.Search Password")
 print("4.Delete Password")
 print("5.Exit")
 print("======================================")
 choice=input("Enter your choice 1-5:")

 if choice=="1":
   #validation check for password  length
   while (True):
     length =int(input("Enter the length of password:"))
     if (8<=length<=12):
       break
     else:
       print("Please enter valid input..!")



    #validation check for website length
   while(True):
       website = input("Enter name of website:")
       if len(website) <=50:
         break
       else:
         print("please enter website name between 1-50 characters..!")
   



   password=generate_password(length)
   print(f"generated password:{password}")
   save_password(website,password)
   print("passsword saved succesfully...")
   
 elif choice == "2":
    print(f"saved passwords")
    view_savedpassword()

 elif choice == "3":
   website=input("Enter name of website to search:")
   search_password(website)

 elif choice == "4":
    website=input("Enter name of website to delete:")
    delete_password(website)

 elif choice == "5":
    print("Thank you..!")
    break

 else:
    print("Invalid Choice..Please try again..!")





