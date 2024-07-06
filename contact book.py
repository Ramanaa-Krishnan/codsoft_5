#CONTACT BOOK - TASK 5 - CODSOFT
#Creating a Contact Book to Store,Add,View,Update,delete user's contact details


cbook={}    #dict initialization

#add contact

def addc(cbook,name,details):    #details as list

    if name not in cbook:
        cbook[name]=details
    else:
        print("The Entered Contact name already exists...!!")
        
#view entire contact book
        
def viewc(cbook):
    for val in cbook:
        print("Name : ",val)
        print("Phone Number : ",cbook[val][0])
        print("E-mail : ",cbook[val][1])
        print("Address : ",cbook[val][2])

        print("""

                 ---  NEXT CONTACT  --- """)        

#view particular conatct details

def searchc(cbook,name):

    if name in cbook:
        print("Contact Exists..!!")
        print("Name : ",name)
        print("Phone Number : ",cbook[name][0])
        print("E-mail : ",cbook[name][1])
        print("Address : ",cbook[name][2])
    else:
        print("Contact Do not exist...!!")

#update particular contact details

def updatec(cbook,name):

    if name in cbook:

        intr=int(input("Enter 0 to update phoneno / 1 to email / 2 to address"))
        if intr==0:
            ph=input("Enter updated phone number :")
            cbook[name][0]=ph
        elif intr==1:
            em=input("Enter updated email address :")
            cbook[name][1]=em
        elif intr==2:
            addr=input("Enter updated House Address :")
            cbook[name][1]=addr
        else:
            print("Enter appropriate response..!!")
    else:

        print("The Contact do not exist and hence it cannot be Updated..!!")
        
            
#delete particular contact details
    
def deletec(cbook,name):

    if name in cbook:
        del cbook[name]

    else:
        print("The Contact that are to be deleted, do not exist in Contact Book ")
        

while True:

    print("""

1 - ADD CONTACT
2 - VIEW CONTACT
3 - SEARCH CONTACT
4 - UPDATE CONTACT
5 - DELETE CONTACT """)


    ch=int(input("Enter a value to start operations on the contact book :"))
    if ch==1:
        name=input("Enter Person's Name :")
        phno=input("Enter Phone Number :")
        email=input("Enter Email :")
        address=input("Enter Address :")
        #details in form of list datatype
        addc(cbook,name,[phno,email,address])  #function call

    elif ch==2:
        viewc(cbook)
    elif ch==3:
        name=input("Enter Person's Name :")
        searchc(cbook,name)
    elif ch==4:
        name=input("Enter Person's Name :")
        updatec(cbook,name)
    elif ch==5:
        name=input("Enter Person's Name :")
        deletec(cbook,name)
        
    else:
        print("Entered Invalid Operation..Try Again..!!")


    con=int(input("Enter 1 to continue the process and 0 to end the process :"))
    if con:
        pass
    else:
        break


print("""

               ---- PROCESS COMPLETED ---- """)
        
