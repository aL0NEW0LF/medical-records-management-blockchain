from web3 import Web3


def connect():
    # Localhost
    w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
