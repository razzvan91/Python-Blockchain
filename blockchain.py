blockchain = [[1]]


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(value):
    blockchain.append([get_last_blockchain_value(), value])

add_value(2)
add_value(0.9)
add_value(20.89)

print(blockchain)