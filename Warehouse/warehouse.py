"""
    Program: Warehouse management system
     Author: Trevor Dotzler
Description: 
    1 - Register new item
            id (auto generated)
            title (str)
            category (str)
            price (float)
            stock (int)
    2 - Display catalog
    3 - Update stock
    4 - Remove item from catalog
    5 - Print Total stock value
    6 - Report - out of stock

"""
# imports
from menu import clear, print_menu, print_header, print_item
from item import Item
import pickle

#global vars
catalog = []
data_file = 'warehouse.data'

def serialize_catalog():
    writer = open('warehouse.data', 'wb') # create/open a file to Write Binary
    pickle.dump(catalog, writer)
    writer.close() #close stream, release the file
    print("*** Data serialized! ")

def deserialize_catalog():
    try:
        global data_file
        reader = open('warehouse.data', 'rb') # open file to read binary
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        print("*** Deserialized! " + str(len(catalog)) + " items")

    except:
        print("Error, could not load data.")

#fn
def register_item():
    try:
        print_header("Register New Item")
        title = input("Please provide the Title: ")
        cat = input("Please provide the Category: ")
        price = float(input("Please provide the Price: "))
        stock = int(input("Please provide the Stock: "))

        id = 1
        item = Item(id, title, cat, price, stock)
        catalog.append(item)

        how_many = len(catalog)
        print("You now have " + str(how_many) +" item(s) on the catalog")
    except ValueError:
        print('Error, incorrect value. Try again.')
    except:
        print("Error, could not load data.")

def update_stock():
    display_catalog()
    id = input("Please provide the item id: ")
    found = False
    for item in catalog:
        if(str(item.id == id)):
            found = True
            val = input("Please provide new stock value: ")

    if(not found):
        print("**Error: Invalid id, verify and try again.")

def display_catalog():
    print_header("Your Current Catalog")
    for item in catalog:
        print_item(item)
 


def display_out_of_stock():
    print_header("Items currently out of stock")
    for item in catalog:
        if (item.stock == 0):
            print_item(item)

def total_stock_value():
    total = 0.0
    for item in catalog:
        total += item.price * item.stock

    print("Total value: " + str(total))




# instructions

deserialize_catalog()
input("Press Enter to continue")

opc = ''
while(opc != 'x'):
    clear()
    print_menu()

    opc = input('Please choose an option: ')

    # if comparisons
    if(opc == '1'):
        register_item()
        serialize_catalog()
    elif(opc == '2'):
        display_catalog()
    elif(opc == '3'):
        display_out_of_stock()
    elif(opc == '7'):
        total_stock_value()



    input('Enter to continue')

