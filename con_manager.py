import json
import os



class ContactManager:
    def __init__(self,filename='contacts2.json'):
        self.filename=filename
        self.contacts=self.load_data()

    def clear(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename,'r')as file:
                return json.load(file)
        return {}
    def save_data(self):
        with open(self.filename,'w')as file:
            json.dump(self.contacts,file)
    def create_contacts(self):
        name=input('Enter the name: ').strip().title()
        number=input('Enter the number: ').strip()
        if not number.isdigit():
            print('Type number only in digits ')
        else:
            self.contacts[name]=number
            self.save_data()
            print('Contact saved successfully.')

    def show_contacts(self):
        for i,(name,number) in enumerate(self.contacts.items(),start=1):
            print(f'{i}. {name} : {number}')
    def search_contact(self):
        name=input('Enter the name: ').strip().title()
        if name not in self.contacts:
            print('Contact not found. ')
        else:
            print(self.contacts[name])
    def update_contact(self):
        name=input('Enter the name: ').strip().title()
        if name not in self.contacts:
            print('Contact not found. ')
        else:
            new_number=input('Enter the number: ')
            if not new_number.isdigit():
                print('Type number only in digits.')
            else:
                self.contacts[name]=new_number
                self.save_data()
                print('Number is updated successfully. ')
    def delete_contacts(self):
        name=input('Enter the name: ').strip().title()
        if name not in self.contacts:
            print('Name not found...')
        else:
            del self.contacts[name]
            self.save_data()
            print('Contact deleted successfully')



    def menu(self):
        while True:
            self.clear()
            print('\n--- Contacts Menu ---')
            print('1. Create Contact')
            print('2. Show all Contacts')
            print('3. Search Contacts')
            print('4. Update Contact')
            print('5. Delete Contact')
            print('6. Exit')
            choice = input('Enter your choice: ')

            if choice == '1':
                self.create_contacts()
            elif choice=='2':
                self.show_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contacts()
            elif choice == '6':
                print('Exiting......')
                break
            else:
                print('Invalid choice...')
if __name__ == '__main__':
    cm=ContactManager()
    cm.menu()