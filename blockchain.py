blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The block's last transaction. """

    if last_transaction == None:
        last_transaction = [1]

    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    return float(input("Enter the amount you want to transaction: "))


def get_user_choice():
    user_input = input("Make a choice:\t")
    return user_input


def print_menu_instructions():
    print("Please choose:\n\n\t1: Add new transaction value.\n\t2: Output the blockchain blocks\n\tq: To quit\n")

def print_blockchain_elements():
    """ Output blockchain elements to the console """
    for block in blockchain:
            print("Outputting block: ")
            print(block)

while True:
    print_menu_instructions()
    user_choice = get_user_choice()

    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_transaction(last_transaction=get_last_blockchain_value(),
                  transaction_amount=tx_amount)

    elif user_choice == "2":
        print_blockchain_elements()

    elif user_choice.lower() == "q":
        break

    else:
        print("Invalid choice!")
    print("Choice registered!")

print("Done!")
