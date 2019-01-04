var Migrations = artifacts.require("./Migrations.sol");
var MengjuKuo=artifacts.require("./MengjuKuo.sol");
var EIP20=artifacts.require("./EIP20Interface.sol");

module.exports = function(deployer) {
  //params:uint256 _initialAmount,string _tokenName,uint8 _decimalUnits,string _tokenSymbol
  
  deployer.deploy(MengjuKuo,100000,"MengjuKuo",0,"MK");
  
};
