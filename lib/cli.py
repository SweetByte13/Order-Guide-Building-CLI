# lib/cli.py
#!/usr/bin/env python3

from helpers import (
    exit_program,
    list_proveyers,
    list_items,
    list_catagories,
    list_items_by_proveyer,
    search_proveyer_by_id,
    create_new_proveyer,
    update_new_proveyer,
    delete_new_proveyer,
    create_new_item_and_par,
    update_item,
    delete_new_item,
    search_item_by_name,
    update_new_par,
    delete_new_par,
    create_new_catagory,
    update_new_catagory,
    list_departments,
    create_new_department,
    update_new_department,
    delete_new_department,
    get_full_order_guide,
    get_order_guide_based_on_pars,
    get_order_guide_items_stock_amounts
)


def main():
    while True:
        print_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_proveyers()
        elif choice == "2":
            list_items()
        elif choice == "3":
            list_catagories()
        elif choice == "4":
            list_items_by_proveyer()
        elif choice == "5":
            get_full_order_guide()
        elif choice == "6":
            get_order_guide_based_on_pars()
        elif choice == "7":
            get_order_guide_items_stock_amounts()
        elif choice == "8": 
            search_item_by_name()
        elif choice == "9":   
            search_proveyer_by_id()
        elif choice == "10":
            manage_proveyer_menu()
        elif choice == "11":
            manage_item_menu()
        elif choice == "12":
            manage_par_menu()
        elif choice == "13":
            manage_catagory_menu()
        elif choice == "14":
            manage_department_menu()         
        else:
            print("Invalid choice")

def manage_proveyer_menu():
    while True:
        print_manage_proveyer_menu()
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            create_new_proveyer() 
        elif choice == "2":
            update_new_proveyer()
        elif choice == "3":
            delete_new_proveyer()
            
def manage_item_menu():
    while True:
        print_manage_item_menu()
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            create_new_item_and_par() 
        elif choice == "2":
            update_item()
        elif choice == "3":
            delete_new_item()

def manage_par_menu():
    while True:
        print_manage_par_menu()
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            create_new_item_and_par() 
        elif choice == "2":
            update_new_par()
        elif choice == "3":
            delete_new_par()
            
def manage_catagory_menu():
    while True:
        print_manage_catagory_menu()
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            create_new_catagory() 
        elif choice == "2":
            update_new_catagory()
        
def manage_department_menu():
    while True:
        print_manage_department_menu()
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            list_departments()
        elif choice == "2":
            create_new_department() 
        elif choice == "3":
            update_new_department()
        elif choice == "4":
            delete_new_department()
                

def print_menu():
    print("-------------------------------")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List Proveyers")
    print("2. List Items")
    print("3. List Catagories")
    print("4. List Items by proveyer")
    print("5. List full order guide")
    print("6. List order guide based on items near or below par amounts")
    print("7. List all items current stock amounts")
    print("8. Search for item by name")
    print("9. Search for proveyer by id")
    print("10. Manage Proveyers")
    print("11. Manage Items")
    print("12. Manage Pars")
    print("13. Manage Catagories")
    print("14. Manage Departments")
    print("-------------------------------")

def print_manage_proveyer_menu():
    print("-------------------------------")
    print("Please select an option:")
    print("0. Return to previous menu")
    print("1. Create proveyer")
    print("2. Edit proveyer")
    print("3. Delete proveyer")
    print("-------------------------------")

def print_manage_item_menu():
    print("-------------------------------")
    print("Please select an option:")
    print("0. Return to previous menu")
    print("1. Create item")
    print("2. Edit item")
    print("3. Delete item")
    print("-------------------------------")
    
def print_manage_par_menu():
    print("-------------------------------")
    print("Please select an option:")
    print("0. Return to previous menu")
    print("1. Create par")
    print("2. Edit par")
    print("3. Delete par")
    print("-------------------------------")

def print_manage_catagory_menu():
    print("-------------------------------")
    print("Please select an option:")
    print("0. Return to previous menu")
    print("1. Create catagory")
    print("2. Edit catagory")
    print("-------------------------------")
    
def print_manage_department_menu():
    print("-------------------------------")
    print("Please select an option:")
    print("0. Return to previous menu")
    print("1. List departments")
    print("2. Create department")
    print("3. Edit department")
    print("4. Delete department")
    print("-------------------------------")

if __name__ == "__main__":
    main()
