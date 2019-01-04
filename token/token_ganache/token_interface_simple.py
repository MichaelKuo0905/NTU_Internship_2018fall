from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
config={"abi": [
    {
      "constant": True,
      "inputs": [],
      "name": "name",
      "outputs": [
        {
          "name": "",
          "type": "string"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "totalSupply",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "name": "balances",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "decimals",
      "outputs": [
        {
          "name": "",
          "type": "uint8"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "",
          "type": "address"
        },
        {
          "name": "",
          "type": "address"
        }
      ],
      "name": "allowed",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "symbol",
      "outputs": [
        {
          "name": "",
          "type": "string"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "name": "_initialAmount",
          "type": "uint256"
        },
        {
          "name": "_tokenName",
          "type": "string"
        },
        {
          "name": "_decimalUnits",
          "type": "uint8"
        },
        {
          "name": "_tokenSymbol",
          "type": "string"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "_from",
          "type": "address"
        },
        {
          "indexed": True,
          "name": "_to",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "_value",
          "type": "uint256"
        }
      ],
      "name": "Transfer",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "_owner",
          "type": "address"
        },
        {
          "indexed": True,
          "name": "_spender",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "_value",
          "type": "uint256"
        }
      ],
      "name": "Approval",
      "type": "event"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_to",
          "type": "address"
        },
        {
          "name": "_value",
          "type": "uint256"
        }
      ],
      "name": "transfer",
      "outputs": [
        {
          "name": "success",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_from",
          "type": "address"
        },
        {
          "name": "_to",
          "type": "address"
        },
        {
          "name": "_value",
          "type": "uint256"
        }
      ],
      "name": "transferFrom",
      "outputs": [
        {
          "name": "success",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_owner",
          "type": "address"
        }
      ],
      "name": "balanceOf",
      "outputs": [
        {
          "name": "balance",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_spender",
          "type": "address"
        },
        {
          "name": "_value",
          "type": "uint256"
        }
      ],
      "name": "approve",
      "outputs": [
        {
          "name": "success",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_owner",
          "type": "address"
        },
        {
          "name": "_spender",
          "type": "address"
        }
      ],
      "name": "allowance",
      "outputs": [
        {
          "name": "remaining",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    }
  ],
	"address": "0xBFD2801B8AD5ba330888D0D8c0f99765973FF720"
}
web3 =Web3(HTTPProvider('http://localhost:8545'))
owner = web3.eth.accounts[0]
token = web3.eth.contract(address=config['address'], abi=config['abi'])


# This function could only be excuted by owner
# Object: transfer token to other accounts
def transfer(_to,_value):
	transact_hash = token.functions.transfer(_to,_value).transact({"from":owner})
	return transact_hash


# Object: Send token value address_from  => address_to 
def transferFrom(_from,_to,_value):
	transact_hash = token.functions.transferFrom(_from,_to,_value)
	return transact_hash

# excetute the function locally. not cost any gas
# Object: check the token balance of account 
def balanceOf(_owner):
	transact_hash=token.functions.balanceOf(_owner).call()
	
	return transact_hash

#Object: allow _spender to withdraw token from your account
def approve(_spender,_value):
	transact_hash=token.functions.approve(_spender,_value)
	return transact_hash

#Object: return the amount which _spender is still allowed to withdraw from _owner
def allowance(_owner,_spender):
	transact_hash=token.functions.allowance(_owner,_spender).call()
	return transact_hash

if __name__ == '__main__':
	'''
	a=transfer(web3.eth.accounts[1],1000)
 	a=token.functions.balanceOf(web3.eth.accounts[1]).call()
 	print(a)
 	tx_hash=token.functions.transfer(web3.eth.accounts[1],10).transact({'from':web3.eth.accounts[0]})
 	tx_receipt=web3.eth.waitForTransactionReceipt("0x07433f424e99b08ed3961229bc7bb9ffcace56a62c9088d6a5d8e2f40fd938fc")
 	event_logs=token.events.Transfer().processReceipt(tx_receipt)
 	print(event_logs)
 	print(event_logs[0]['args'])


 	print(a)
	'''
	a=transfer(web3.eth.accounts[1],10);
	print(a)
  
    






