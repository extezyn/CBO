from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, adress

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

print(w3.eth.get_balance("0x154ba0a03d72995317bc27C4C9C3127F27F3cba0"))
print(w3.eth.get_balance("0xac97a1f5bAa104f09Ee21ECA783138937C10f65A"))
print(w3.eth.get_balance("0xB71d2E02cD351A4ACBC135fc3f8B5a03BEfa8521"))
print(w3.eth.get_balance("0x7cE5c6629f09B12bAdBBE1D0f30b13592A97E6c3"))
print(w3.eth.get_balance("0x3e1dF3405684D18E68F785D1DCB84ba4c20B8538"))
