"""
author: Sunil K B

description:
Develop a python application for implementing an contact address book similar to the address book in a mail account.
Choose appropriate data structure to store the data of each contact. Methods to be supported are:
Insert_NewContact()
Delete_Contact()
Search_Contact()
Update_Contact()


usage:
python3 DSA_4.py
"""

from __future__ import print_function
import re
import json
import sys
import os.path

if sys.version_info < (3, 0, 0):
    print(__file__ + ' requires Python 3, while Python ' + str(sys.version[0] + ' was detected. Terminating. Run - python3 '+__file__))
    sys.exit(1)

addr_file='address.json'


def clear_all():
    if os.path.exists(addr_file):
        os.remove(addr_file)


def write_json(new_data, filename='address.json'):
    if os.path.exists(addr_file):
        with open(filename, "r+") as file:
            try:
                file_data = json.load(file)
                file_data.update(new_data)
            except:
                file_data = new_data
            file.seek(0)
            json.dump(file_data, file, indent=4)

    else:
        with open(filename, "w") as file:
            json.dump(new_data, file, indent=4)
    return 1


def insert_new_contact():
    aadhaar = ''
    while not re.match(r'^[0-9]+$', aadhaar):
        aadhaar = input('Enter Aadhaar Number: ')

    first_name = ''
    while not re.match(r'^[a-zA-Z]+$', first_name):
        first_name = input('Enter First Name: ')

    last_name = ''
    while not re.match(r'^[a-zA-Z]+$', last_name):
        last_name = input('Enter Last Name: ')

    phone_number = ''
    while not re.match(r'^[0-9]+$', phone_number):
        phone_number = input('Enter Phone Number: ')

    email = ''
    while not re.match(r'^[\w\@\.]+$', email):
        email = input('Enter Email: ')

    data = dict()
    data[aadhaar] = dict()
    data[aadhaar]['FirstName'] = first_name
    data[aadhaar]['LastName'] = last_name
    data[aadhaar]['Phone'] = phone_number
    data[aadhaar]['Mail'] = email
    write_json(data)


def display_all():
    if os.path.exists(addr_file):
        print("\n All Stored Contacts:\n")
        with open(addr_file, 'r') as openfile:
            json_object = json.load(openfile)
        print("\n--------------------------------------\n")
        print(json.dumps(json_object, indent=1))
        print("\n--------------------------------------\n\n")
    else:
        print("\n--------------------------------------\n")
        print("\nNo Contacts Present\n")
        print("\n--------------------------------------\n\n")


def delete_contact(filename='address.json'):
    if os.path.exists(addr_file):
        aadhaar = ''
        while not re.match(r'^[0-9]+$', aadhaar):
            aadhaar = input('Enter Aadhaar Number of contact to delete: ')
        if search_contact(aadhaar=aadhaar):
            with open(filename, "r+") as file:
                file_data = json.load(file)
                del file_data[aadhaar]['FirstName']
                del file_data[aadhaar]['LastName']
                del file_data[aadhaar]['Phone']
                del file_data[aadhaar]['Mail']
                del file_data[aadhaar]
                file.seek(0)
                clear_all()
                write_json(file_data)
                print("\n--------------------------------------\n")
                print("\nDelete Success\n")
                print("\n--------------------------------------\n\n")
        else:
            return 0
    else:
        print("\n--------------------------------------\n")
        print("\nNo Contacts Present\n")
        print("\n--------------------------------------\n\n")
        return 1


def search_contact(filename='address.json', aadhaar=None):
    if os.path.exists(addr_file):
        if aadhaar is None:
            aadhaar = ''
            while not re.match(r'^[0-9]+$', aadhaar):
                aadhaar = input('Enter Aadhaar Number to search: ')
        with open(filename, "r") as file:
            file_data = json.load(file)
            if aadhaar in file_data.keys():
                print("\n--------------------------------------\n")
                print("\n Found Contact\n")
                print(file_data[aadhaar])
                print("\n--------------------------------------\n\n")
                return 1
            else:
                print("\n--------------------------------------\n")
                print("\n Contacts Not Found\n")
                print("\n--------------------------------------\n\n")
                return 0

    else:
        print("\n--------------------------------------\n")
        print("\nNo Contacts Present\n")
        print("\n--------------------------------------\n\n")
    return 1


def update_contact(filename='address.json'):
    if os.path.exists(addr_file):
        aadhaar = ''
        while not re.match(r'^[0-9]+$', aadhaar):
            aadhaar = input('Enter Aadhaar Number of contact to update: ')
        if search_contact(aadhaar=aadhaar):
            with open(filename, "r+") as file:
                file_data = json.load(file)
                response = None
                while response not in {'1', '2', '3', '4', }:
                    input_msg = """
Which Field do you want to update. Select option from the below list (1/2/3/4)
1. First Name 
2. LastName
3. Phone
4. Mail
Your Choice: """
                    response = input(input_msg)

                if response == '1':
                    first_name = ''
                    while not re.match(r'^[a-zA-Z]+$', first_name):
                        first_name = input('Enter First Name: ')
                        file_data[aadhaar]['FirstName'] = first_name
                elif response == '2':
                    last_name = ''
                    while not re.match(r'^[a-zA-Z]+$', last_name):
                        last_name = input('Enter Last Name: ')
                        file_data[aadhaar]['LastName'] = last_name
                elif response == '3':
                    phone_number = ''
                    while not re.match(r'^[0-9]+$', phone_number):
                        phone_number = input('Enter Phone Number: ')
                        file_data[aadhaar]['Phone'] = phone_number
                elif response == '4':
                    email = ''
                    while not re.match(r'^[\w\@\.]+$', email):
                        email = input('Enter Email: ')
                        file_data[aadhaar]['Mail'] = email

                file.seek(0)
                clear_all()
                write_json(file_data)
                print("\n--------------------------------------\n")
                print("\nUpdate Success\n")
                print("\n--------------------------------------\n\n")
        else:
            return 0
    else:
        print("\n--------------------------------------\n")
        print("\nNo Contacts Present\n")
        print("\n--------------------------------------\n\n")
        return 1


# Main
if __name__ == '__main__':
    while True:
        response = None
        while response not in {'1', '2', '3', '4', '5', '6', '7'}:
            input_msg = """
Enter your option from the below list of permitted options(1/2/3/4/5/6/7)
1. Insert_NewContact 
2. Delete_Contact
3. Search_Contact
4. Update_Contact
5. Display_All_Contacts
6. Clear All Contacts
7. Quit
Your Choice: """
            response = input(input_msg)
        print("Response is {}".format(response))

        if response == "1":
            insert_new_contact()
        if response == "2":
            delete_contact()
        if response == "3":
            search_contact()
        if response == "4":
            update_contact()
        if response == "5":
            display_all()
        if response == "6":
            clear_all()
        if response == "7":
            break
