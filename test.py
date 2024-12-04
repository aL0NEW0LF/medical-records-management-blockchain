from web3 import Web3


def test():
    # Localhost
    w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
    print(w3.is_connected())
    # Print accounts
    print(w3.eth.accounts)
    # Print block number


test()
