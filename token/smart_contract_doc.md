# Functions in MengjuKuo Smart Contract

## `transfer`
- **Description** <br>
 As long as you have enough token, you can transfer your token to another account.
- **Syntax** <br>
`transfer(address _to, uint256 _value)`
- **Parameters** <br>
  -- `to`: (`address`), the address of account you want to transfer.
- **Return value** <br>
  `(bool success)`
  -`success` return transaction is successful or not
- **Event emitted** <br>
  `Transfer(msg.sender, _to, _value)`:
   -`msg.sender`:  the one who launch the transaction
   -`_to`:  the one who receive the token
   -`_value`: the number of token being tranferred  
 
<br>

## `transferFrom` 
- **Description** <br>
  Remember this function could only be used after you get the `approve` from the account where you want to transfer the money to other accounts.
- **Syntax** <br>
`transferFrom(address _from, address _to, uint256 _value`
- **Parameters** <br>
  - `_from`: (`address`), the address of token owner
  - `_to`: (`address`), the address who receive the token
  - `_value`: (`uint256`), the number of token will be tranferred
  - **Return value** <br>
  `(bool success)`
  -`success` return transaction is successful or not
- **Event emitted** <br>
  `Transfer(from, _to, _value)`:
   -`from`:  the address of token owner
   -`_to`:  the address who receive the token
   -`_value`: the number of token being tranferred  

<br>

## `balanceOf`
- **Description** <br>
  This function will be used to check the number of token in the account.
- **Syntax** <br>
`balanceOf(address _owner)`
- **Parameters** <br>
  - `_owner`: (`address`), the address whose token you want to check
- **Return value** <br>
  `(uint256 balance)`: 
    - `balance`: the number of token

<br>

## `approve`
- **Description** <br>
  This function is very important. No matter you want to use `transferFrom` or `burnFrom`, you need to get the approvement from this function. The function ususlly be used by `the token owner` that is those functions's parameter **address _from**
- **Syntax** <br>
`approve(address _spender, uint256 _value)`
- **Parameters** <br>
  - `_spender`: (`address`), the address whom the token owner gives the approvement to  
  - `_value`: (`uint256`), the maximum value you give the `_spender` to utilitize you token 
- **Return value** <br>
  `(bool success)`
  -`success` return transaction is successful or not
- **Event emitted** <br>
  `Approval(msg.sender, _spender, _value)`:
   -`msg.sender`:  the address of token owner
   -`_spender`:  the address whom the token owner gives the approvement to
   -`_value`: the number of token being tranferred  

<br>

## `allowance`
- **Description** <br>
  This funciton is used to check the number of token  which `spender` can use from `token owner`
- **Syntax** <br>
`allowance(address _owner, address _spender))`
- **Parameters** <br>
  - `_owner`: (`address`), the address of token owner
  - `_spender`: (`address`), the address whom the token owner gives the approvement to
- **Return value** <br>
  `(uint256 remaining)`:
    - `remaining`: the maximum token value the spender could utilitize from the token owner 

<br>

## `mintToken`
- **Description** <br>
  This function is used to increase the number of total token, and only be triggerd by **creater**
- **Syntax** <br>
`mintToken(address target, uint256 mintedAmount)`
- **Parameters** <br>
  - `targer`: (`address`), the address whom the creater wants to increase its token
  - `mintedAmount`: (`uint256`), the number of increased token
- **Event emitted** <br>
  `Transfer(msg.sender, target, mintedAmount)`:
   -`msg.sender`:  the address of token owner
   -`target`:  the address whom the creater wants to increase its token
   -`mintedAmount`: the number of increased token

<br>

## `burn`
- **Description** <br>
  This function is used to decrease the number of total token, and only be triggerd by **creater**
- **Syntax** <br>
`burn(uint256 _value)`
- **Parameters** <br>
  - `_value`: (`uint256`), the number of decreased token
- **Event emitted** <br>
  `Burn(msg.sender, _value)`:
   -`msg.sender`:  the address of creater
   -`_value`: the number of decreased token

<br>

## `burnFrom` 
- **Description** <br>
  Remember this function could only be used after you get the `approve` from the account where you want to decrease someone's token
- **Syntax** <br>
`burnFrom(address _from, uint256 _value`
- **Parameters** <br>
  - `_from`: (`address`), the address of token owner
  - `_value`: (`uint256`), the number of decreased token
  - **Return value** <br>
  `(bool success)`
  -`success` return transaction is successful or not
- **Event emitted** <br>
  `Burn(_from, _value)`:
   -`from`:  the address of token owner
   -`_value`: the number of decreased token 


## Constructor
- **Description** <br>
  Construct the contract. The `initialAmount` `tokenName` `decimalUnits` `tokenSymbol` will be determined when contract is deployed
- **Syntax** <br>
`<contract_name>(uint256 _initialAmount,string _tokenName,uint8 _decimalUnits,string _tokenSymbol)`
- **Parameters** <br>
  - `_initialAmount`: the total number of token
  - `_tokenName`: the name of token
  - `_decimalUnits`: amount of decimals for display purposes EX: ether will be 18
  - `tokenSymbol`: the abbreviation of token name