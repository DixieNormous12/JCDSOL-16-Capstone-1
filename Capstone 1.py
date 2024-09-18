Contact_Name = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo']
Contact_Phone = ['012', '345', '678', '910', '112']

def intro(username):
    print('Hello, {}'.format(username))
    print('How can I help you today?')

while True:
    intro('Bei')
    
    userinput = input('Answer (Add, Change, Find, Delete or Exit): ')
    
    if userinput == 'Add':
        name = input('Insert Name: ')
        number = input('Insert Number: ')
        Contact_Name.append(name)
        Contact_Phone.append(number)
        print('Roger that, added {} and their phone number {} into the list.'.format(name, number))

    elif userinput == 'Change':
        change = input('Enter Name or Number to change: ')
        if change in Contact_Name:
            change_Q1 = input('What do you want to change them into? ')
            index1 = Contact_Name.index(change)
            Contact_Name[index1] = change_Q1
            print('Changed {} as {} in the list'.format(change, change_Q1))
        elif change in Contact_Phone:
            index2 = Contact_Phone.index(change)
            new_number = input('Enter the new number for {}: '.format(Contact_Name[index2]))
            Contact_Phone[index2] = new_number
            print("Changed {}'s number to {}".format(Contact_Name[index2], new_number))
        else:
            print('The name or number is not in the library')

    elif userinput == 'Find':
        search = input('Enter Name or Number to find: ')
        if search in Contact_Name:
            index = Contact_Name.index(search)
            print('Name and Number: {} - {}'.format(Contact_Name[index], Contact_Phone[index]))
        elif search in Contact_Phone:
            index = Contact_Phone.index(search)
            print('Name and Number: {} - {}'.format(Contact_Name[index], Contact_Phone[index]))
        else:
            print('Contact not found. Please check again.')

    elif userinput == 'Delete':
        delete_name = input('Enter Name to delete: ')
        if delete_name in Contact_Name:
            index = Contact_Name.index(delete_name)
            Contact_Name.pop(index)
            Contact_Phone.pop(index)
            print('Contact deleted. Sad to see them go :(')
        else:
            print('Nope, not found. Check the list again.')

    elif userinput == 'Exit':
        print('Why you gotta leave me like that bro :(')
        break  # Exit the loop

    else:
        print('Sorry, I can only understand "Add", "Change", "Find", "Delete" or "Exit". Pick one please.')