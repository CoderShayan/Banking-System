#===================
#  Banking System
#===================

import random as r
import math as m
 
account_list = {}

#---------------------------------------------------------------------

def getAccountDetail(account):
    if(account_list[account]):
        return account_list[account]
    else:
        print('A/c Details Not Found')
    print("========================================")
    return account_list
    
#----- Show Account Details --------------------------------------------------------------

def showAccountDetails():
    acc_no = int(input("Enter Your A/C number:"))
    if acc_no in account_list:
        print("A/c No.:", account_list[acc_no]['acount_no'])
        print("A/c holder name:", account_list[acc_no]['name'])
        print("Current balance:", account_list[acc_no]['bal'],"INR")
        #print("Your PIN: ",account_list[acc_no]['pin'])
    else:
        print("A/C no. Not Found")
    print("========================================")
    return account_list

#----- Account Balance Update -----------------------------------------------------------

def updateBal(account,data):
    account_list[account]['bal'] = data
    return account_list
    
#---------------------------------------------------------------------

def saveAccountDetail(account,data):
    options = input('Which data you want to save: \nLike : Name , Bal If Name type Name otherwise Bal: ')
    match options:
        case 'Name':
            account_list[account]['name'] = data
        case 'Bal':
            account_list[account]['bal'] = data
        case _:
            print('Invalid Input: Type any one hint')
            saveAccountDetail(account,data)
    return account_list

#---- Open New Account -----------------------------------------------------------------

def createAccount():
    name =  input('Enter Name to Create A/c: ')
    minimum_bal = 2000
    opening_amt = False
    while opening_amt < minimum_bal:
        opening_amt =  int(input('Deposit Amount to Create A/c: '))
        if opening_amt < minimum_bal :
            print('Insufficient Bal to open an A/C')
            option = input("Do you want to exit: (Yes/No)")
            match option:
                case 'Yes':
                    break
                case _:
                    continue
    else:
        rand_num =  r.random()
        rand_num = rand_num * (10 ** 10)
        acount_no = int(m.trunc(rand_num))
        account_list[acount_no] = {'acount_no' : acount_no, 'bal':opening_amt , 'name':name }
        print('Your A/c open successfully With A/c No.', acount_no ,' With Amt INR: ', opening_amt)
        length = 4
        pin = ''
        while len(pin) != length:
            pin = input("Create 4 digit PIN: ")
            match len(pin):
                case 4:
                    break
                case _:
                    print("Please enter only 4-Digit pin.")
                    continue
        account_list[acount_no] = {'acount_no' : acount_no, 'bal':opening_amt , 'name':name , 'pin':pin }
        print(account_list)
    print("========================================")
    return account_list

#----- Deposit Amount ----------------------------------------------------------------
 
def depositAmount():
    account_nu = int(input('Enter A/c number to deposit amount: '))
    if account_nu in account_list:
        data =  getAccountDetail(account_nu)
        bal = int(input('Enter deposit amount: '))
        min = 500

        if bal < min:
            print('Insufficient Bal to deposit.')
            print("========================================")

        else:
            current_bal  = int(data['bal']) + bal
            updateBal(account_nu,current_bal)
            print('Your', bal ,'INR deposit successfully on A/c No.', account_nu ,'\nNow current bal INR: ', current_bal)
            print("========================================")
    else:
        print('This A/c ', account_nu ,'Not Found')
        print("========================================")

#----- Amount Withdraw ----------------------------------------------------------------

def withDrawAmount():
    account_nu = int(input('Enter A/c number to withdraw amount:'))
    if account_nu in account_list:
        data =  getAccountDetail(account_nu)
        pin = input("Enter PIN:")

        if pin == account_list[account_nu]['pin']:
            bal = int(input('Enter withdraw amount: '))

            if bal <= account_list[account_nu]['bal']:
                min = 500

                if bal < min:
                    print('Insufficient Bal to withdraw.')

                else:
                    current_bal  = int(data['bal']) - bal
                    updateBal(account_nu,current_bal)
                    print('Your', bal ,'INR withdraw successfully on A/c No.', account_nu ,'\nNow current bal INR: ', current_bal)
            else:
                print("Insufficient Balance")
        else:
            print("ERROR: PIN not matched.")
    else:
        print('This A/c ', account_nu ,'Not Found')
    print("========================================")
        
#----- Transfer Amount from One A/C to another -----------------------

def amountTransfer():
    User_Acc = int(input("Enter Your A/C no. :"))
    if User_Acc in account_list:
        pin = input("Enter Your PIN:")
        
        if pin == account_list[User_Acc]['pin']:
            trans_acc = int(input("Enter A/C no. which you want to transfer :"))
            name = input("Enter A/C holder name:")
            
            if trans_acc in account_list and name == account_list[trans_acc]['name']:
                if User_Acc == trans_acc:
                    print("You can't Transfer Amount in your own A/C.")
                trans_amt = int(input("Enter amount to transfer:"))
                if trans_amt <= account_list[User_Acc]['bal']:
                    account_list[User_Acc]['bal'] = int(account_list[User_Acc]['bal']) - trans_amt
                    account_list[trans_acc]['bal'] = int(account_list[trans_acc]['bal']) + trans_amt
                    updateBal(User_Acc,account_list[User_Acc]['bal'])
                    updateBal(trans_acc,account_list[trans_acc]['bal'])
                else:
                    print("Insufficient Balance to transfer.")
            else:
                print("Invalid: Information Missmatch.")
        else:
            print("PIN not Matched")
    else:
        print("A/C not found.")
    print("========================================")
    return 0

#--------------------------------------------------------------------- 

#print(account_list)
print("--Welcome to our Bank--")
print("Press 1 to open new A/C.\nPress 2 to Check A/C Details.\nPress 3 to Deposit Ammount")
print("Press 4 to withdrw amount.\nPress 5 for Transfer Amount to another A/C\nPress 0 to Exit")
select = int(input("Enter your Option: "))

while select != 0:
    match select:
        case 1:
            createAccount()
            select = int(input("Enter your Option: "))
        case 2:
            showAccountDetails()
            select = int(input("Enter your Option: "))
        case 3:
            depositAmount()
            select = int(input("Enter your Option: "))
        case 4:
            withDrawAmount()
            select = int(input("Enter your Option: "))
        case 5:
            amountTransfer()
            select = int(input("Enter your Option: "))
        case _:
            print("Invalid Option... Pls Try Again")
            select = int(input("Enter Valid Option: "))

print("Thank You for Visiting....!")
print("\n==========================================")
print(account_list)
