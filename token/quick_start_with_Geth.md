# Quick start with Geth

## Prerequisite
1. [Truffle](https://truffleframework.com/truffle)
2. [Geth](https://geth.ethereum.org/downloads/)

## Start the geth nodes
- Use the start-scripts to set up a geth node. (The scripts are in the `gethnode_instruction.md` directory of documentation ) You can change options in the scripts freely.


## Deploy the smart contract 
- `cd` to `token_ganache` folder
    - `truffle compile`
    - `truffle migrate --network development`  **Please make sure when you deploy your contract there must be at least one node is mining** <br> 
    - ~~copy the abi object from `token_ganache/build/contracts/MengjuKuo.json` to `interface/contract_address.json`~~ `cd` to `interface/`, run `get_contract_abi.py --name <contract_name>` 
    - copy the `MengjuKuo` contract address from console to `interface/contract_address.json`

### An example
1. `truffle migrate --network privateTestChain`.  
2. `python get_contract_abi -name MengjuKuo`


## Start interfaces
- `cd` to `interface/`
    - `python3 token_interface.py`  the default ip argument is local host, set it to the ip address where the ganache node is hosted if necessary
    



