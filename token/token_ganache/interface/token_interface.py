from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from util import *
import argparse

# "address": "0x4e7bbbe813d98c2a3c513f28a71e155166f5b899"
#web3 = Web3(HTTPProvider('http://localhost:8545'))
#owner = web3.eth.accounts[0]
#contract_instance = web3.eth.contract(address=config['address'], abi=config['abi'],ContractFactoryClass=ConciseContract)
node =None;
Token=None;



# This function could only be excuted by owner
# Object: transfer token to other accounts
def transfer(_to,_value):
  transact_hash = Token.functions.transfer(_to,_value).transact({"from":from_account})
  return transact_hash


# Object: Send token value address_from  => address_to 
def transferFrom(_from,_to,_value):
  transact_hash = Token.functions.transferFrom(_from,_to,_value)
  return transact_hash

# excetute the function locally. not cost any gas
# Object: check the token balance of account 
def balanceOf(_owner):
  transact_hash=Token.functions.balanceOf(_owner).call()
  
  return transact_hash

#Object: allow _spender to withdraw token from your account
def approve(_spender,_value):
  transact_hash=Token.functions.approve(_spender,_value)
  return transact_hash

#Object: return the amount which _spender is still allowed to withdraw from _owner
def allowance(_owner,_spender):
  transact_hash=Token.functions.allowance(_owner,_spender).call()
  return transact_hash

def mintToken(_owner,mintedAmount):
	transact_hash=Token.functions.mintToken(_owner,mintedAmount).transact({"from":from_account})
	return transact_hash

def burn(_value):
	transact_hash=Token.functions.burn(_value).transact({"from":from_account})
	return transact_hash

def burnfrom(_from,_value):
	transact_hash=Token.functions.burnfrom(_from,_value)
	return transact_hash

	   

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--ip', type=str, default="127.0.0.1",
						help='the rpc ip address of the node')
  parser.add_argument('-p', '--port', type=int, default=8545,
						help='the rpc port number of the node')
  parser.add_argument('-a', '--account_idx', type=int, default=0,
						help='the account index of the transaction sender')
  args = parser.parse_args()

  socket_addr = 'http://%s:%d' % (args.ip,args.port)
  print('connecting to node at %s \n\n' % socket_addr)

  #connent to the node
  node=Web3(Web3.HTTPProvider(socket_addr))
  from_account=node.eth.accounts[args.account_idx]
  # node info
  display_node_info(node, from_account)
  Token = get_contract(node, 'Token')
  
  #b=burn(100)

  a=Token.functions.balanceOf(from_account).call()
  print(a);
  '''
  print("token_balance:",a)
  
  tx_receipt=node.eth.waitForTransactionReceipt("0x6dd0fdb83c91ef8e5b6cc0a088df3d78cff805ed3067ae3365ef5eefd4838299")
  event_logs=Token.events.Burn().processReceipt(tx_receipt)
  print(event_logs)
  #print(event_logs[0]['args'])
  '''
