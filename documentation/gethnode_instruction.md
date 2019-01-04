# PrivateChain Node launch script

## Detail information 
[Clique PoA consensus Private chain](https://medium.com/taipei-ethereum-meetup/使用-go-ethereum-1-6-clique-poa-consensus-建立-private-chain-1-4d359f28feff)

## Start the geth nodes
- `cd` to `smart-contract` folder
- `geth --datadir ./data --networkid $55661(your initial setting) --port $2003(should be different from other peers) --unlock $7a105190d3525b9890adf3707cf4cbfdc8ad7dc0(key address) --rpcport $8545 --rpc  console`

## Common instruction in geth console 
- **Show node information** <br> 
`admin.nodeInfo`
- **Add p2p Peers** <br> 
`admin.addPeer(“enode://$ you will see it after launching the geth node @$ip:$port”)`
`EX:admin.addPeer(“enode://$87692411dd1af113ccc04d3f6d3d7d47366c81e595525c861c7a3c902ca0a86f46e8d7a837f431536822dbb012f68d942ed96910385805864e990efdf3839a1e@$127.0.0.1:$2000”)`
- **Show Peers** <br> 
`admin.peers` Please make sure each node all connects to other nodes 
- **Mining** <br> 
`miner.start()`











