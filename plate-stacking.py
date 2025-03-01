plate_stack = []


def read_required_string(prompt):
    stringInput = ""
    while len(stringInput) == 0:
        stringInput = input(f"{prompt}").strip()
        if len(stringInput) == 0:
            print("Value is required.")
            #return read_required_string(prompt)
        #else:
    
    return stringInput

def menu():
    main_menu = """
    Menu
    =======================
    0. [Exit]
    1. Add a plate
    2. Print plates
    3. Remove plates
    Select [0 - 3]: """

    choice = read_required_string(main_menu).strip()
    match choice:
        case "0":
            return True
        case "1":
            add_plate()
        case "2":
            print_plates()
        case "3":
            remove_plates()
        case _:
            print("Invalid choice.")
            menu()
    
    return False

def add_plate():
    add_menu = """
    Add a plate
    ===================
    Enter a plate size: """

    stack_size = len(plate_stack)
    

    plate_size = read_required_string(add_menu)
    if plate_size.isdigit() is False or plate_size == "0":
        print("Invalid Plate Size")
        return add_plate()
    elif stack_size == 0:
        plate_stack.append(int(plate_size))
        print("Success!")
    elif stack_size > 0:
        real_plate_size = int(plate_size)
        last_size = int(plate_stack[stack_size - 1])
        if real_plate_size > last_size:
            print(f"Cannot place a plate of size {real_plate_size} on top of another plate of size {last_size}. ")
        else:
            plate_stack.append(real_plate_size)
            print("Success!")
    

def print_plates():
    plate_stack_size = len(plate_stack)

    print("""
    Print Plates
    ===================
    """)

    if plate_stack_size == 0:
        print("\n There are no plates.")
    else:
        print(" \n Let's print the plate sizes \n")
        
        for plate in range(plate_stack_size - 1, -1, -1):
            print(plate_stack[plate])

        print(" \n Let's print a physical representation of the plates \n")
        justify = int(plate_stack[0])
        for plate in range(plate_stack_size - 1, -1, -1):
            text = "#" * plate_stack[plate]
            print(f"{text:^{justify}}")

def remove_plates():
    

    if len(plate_stack) == 0:
        print("\n There are no plates.")
    else:
        amount = read_required_string("How many plates would you like to remove? (Starting from the top of the stack): ")
        if amount.isdigit() is False or amount == "0":
            print("Invalid Quantity")
            return remove_plates()
            
        quantity = int(amount)
        start_index = len(plate_stack) - quantity

        if quantity > len(plate_stack):
            print("Error: Chosen number is too big.")
        if quantity > 0 and quantity <= len(plate_stack):
            del plate_stack[start_index:]
            print("Plates Removed")

def run():
    terminate = False
    while terminate is not True:
        terminate = menu()
    
    print("Goodbye")


run()