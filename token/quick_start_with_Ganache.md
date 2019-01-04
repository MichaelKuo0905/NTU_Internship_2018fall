# Quick start with Ganache

1. start ganache node
    - `ganache-cli `
    - `Ganache` which is a visualized version. [Download](https://truffleframework.com/ganache)
2. deploy the smart contract
    - `cd` to `token_ganache` folder
    - `truffle compile`
    - `truffle migrate --network development`
    - ~~copy the abi object from `token_ganache/build/contracts/MengjuKuo.json` to `interface/contract_address.json`~~ `cd` to `interface/`, run `get_contract_abi.py --name <contract_name>` 
    - copy the `MengjuKuo` contract address from console to `interface/contract_address.json`
3. start the interface
    - `cd` to `interface/`
    - `python3 token_interface.py`  the default ip argument is local host, set it to the ip address where the ganache node is hosted if necessary
    
