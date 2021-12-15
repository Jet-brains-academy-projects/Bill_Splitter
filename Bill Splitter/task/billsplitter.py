# write your code here
import random

print('Enter the number of friends joining (including you):')
guests_number = int(input())
guests_dic = {}

# Check number of friends
if guests_number <= 0:
    print("No one is joining for the party")
elif guests_number > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    # Add friends to dictionary guests_dic
    for i in range(0, guests_number):
        name = input()
        guests_dic.update({name: 0})

    # Count bill value
    print('Enter the total bill value')
    total_bill_value = int(input())
    bill_value = round((total_bill_value / guests_number), 2)
    for name in guests_dic:
        guests_dic[name] = bill_value
    # Lucky person feature
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer == "Yes":
        # Select random person from dictionary
        random_person = random.choice(list(guests_dic))
        # Recalculate the split value
        guests_number = guests_number - 1
        del guests_dic[random_person]
        bill_value = round((total_bill_value / guests_number), 2)
        for name in guests_dic:
            guests_dic[name] = bill_value
        # Add lucky person to bill value
        guests_dic.update({random_person: 0})
        print(f"{random_person} is the lucky one!")
    else:
        print('No one is going to be lucky')

    print("")
    print(guests_dic)
