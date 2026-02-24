class contactManagement():
    def __init__(self):
        self.contact={}
    def add(self):
        name=input("Enter name:")
        if name in self.contact:
            print("contact already exits!!!")
            return
        mobile=int(input("Enter mobile number:"))
        mail=input("Enter mail:")
        self.contact[name]={"mobile":mobile,"mail":mail}
        print("Contact added successfully!!!")
    def update(self):
        name=input("Enter a name to update:")
        if name not in self.contact:
            print("Contact not found")
            return
        print("Old number:",self.contact[name]["mobile"])
        new_number=int(input("Enter new number:"))
        self.contact[name]["mobile"]=new_number
        print("Mobile number Updated successfull!!!")
    def list_contact(self):
        if not self.contact:
            print("No contacts available.")
            return
        for name,details in self.contact.items():
            print("Name:",name)
            print("Mobile:",details["mobile"])
            print("Email:",details["mail"])
    def delete(self):
        name=input("Enter name to delete:")
        if name in self.contact:
            del self.contact[name]
            print("Contact deleted successfull!!!")
        else:
            print("Contact not found")
        
    def main(self):
        while True:
            print('''
            1.Add contact
            2.Update contact
            3.list of contact
            4.Delete contact
            5.Exit''')
            option=int(input("Choose the option:"))        
            if option==1:
                self.add()
            elif option==2:
                self.update()
            elif option==3:
                self.list_contact()
            elif option==4:
                self.delete()
            elif option==5:
                print("Exiting program!!!!!!!!!")
                break
            else:
                print("Invaild options! Try again")
c=contactManagement()
c.main()
