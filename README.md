Order guide Builder:

This program allows the user to build, edit, and sort an order guide based on the users input.

To begin the program, run python lib/cli.py in the terminal.
The CLI will start the program at the main menu. This menu allows for the user to select from a list of options, each with their own tasks. Some options have submenus which further allow for the user to manipulate the data. In each menu, there is a built in way to return to the next previous menu by entering in 0. In the main menu, 0 will exit the program. In submenus, 0 will bring the user back to the previous menu.

-------------------------------
Please select an option:
0. Exit the program
1. List Proveyers
2. List Items
3. List Catagories
4. List Items by proveyer
5. List full order guide
6. List order guide based on items near or below par amounts
7. List all items current stock amounts
8. Search for item by name
9. Search for proveyer by id
10. Manage Proveyers
11. Manage Items
12. Manage Pars
13. Manage Catagories
14. Manage Departments
-------------------------------

This is the menu the user sees upon entering the program. User will follow prompts to do tasks. 

Proveyer's are a class which have a many to many relationship with catagories and items. A proveyer may carry items from multiple catagories, such as dairy and produce. A proveyer should also carry many different items. Therefore, there are join tables between these classes. These join tables are using the classes called proveyer_catagories and proveyer_item. These join tabes are silent to the user, but are behind the scenes allowing for information from a many to many to be passed cleanly and swiftly. There a few other join table type classes within this program.

This program is to help build an order guide and maintain it. It allows for multiple data points regrading ordering to be kept in a single spot. The program allows for the user to print order guides based on varying selections. Users can do the following using the program:
> List items by proveyer 
> List a full order guide
> List an order guide based on low stock levels
    >>This allows the user to see only the items they need to order as they are low instead of having to see the whole guide. 
> List an order guide with an overview of current items in stock. 
    >>This gives the user a list of what the current stock level of each item is; which is helpful not only for ordering but also inventoy.
> create proveyers, items, catagories, pars, and departments for the guide
> update proveyers, items, catagories, pars, and departments from the guide
> delete proveyers, items, catagories, pars, and departments from the guide
> search items by name
> search proveyers by ID


This project was worked on by Tova Hillman as one of her projects at Flatiron School. 

Github linked here: https://github.com/SweetByte13




