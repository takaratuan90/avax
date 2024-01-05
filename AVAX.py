from threading import Thread
import threading
import urllib.request
from urllib.request import Request, urlopen
import re
import requests

from web3.middleware import geth_poa_middleware # Needed for Binance
from json import loads
from blocknative.stream import Stream
from datetime import datetime

import json
import time
import datetime
from web3 import Web3
web3 = Web3(Web3.HTTPProvider('https://avalanche.public-rpc.com'))

#web3 = Web3(Web3.HTTPProvider('https://go.getblock.io/84d68a1c4db249ff9e70ac2a4f8632bd'))


print(web3.isConnected())
tuan='0x68361413a9a21e4848BA8Ac248AB0A14E7456385'
panRouterContractAddress = '0x60aE616a2155Ee3d9A68541Ba4544862310933d4'
with open('jsontradejoi.json', 'r') as file:
    panabi = json.loads(file.read())

spend = web3.toChecksumAddress("0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7")  #WBNB Address
contract = web3.eth.contract(address=panRouterContractAddress, abi=panabi)
timestamp = int(time.time()) + 10000 
hex_timestamp = hex(timestamp)[2:20]


def balancebnb():
    for i in range(4):
        txt = open("4wallet.txt").read().splitlines()[i]
        receved_Wallet = txt.split("|")[0]
        receved_Wallet=web3.toChecksumAddress(receved_Wallet) 
        balance1 = web3.eth.get_balance(receved_Wallet)
        humanReadable = web3.fromWei(balance1,'ether')
        BalanceBNB=round(humanReadable,4)
        print(receved_Wallet+'|'+str(BalanceBNB))

balancebnb()

#-----------------------------------------------------------------------------------------------------------------------




def senddata():
    for i in range(7):
        gas_price1 = web3.eth.gasPrice
        gas_float = gas_price1 / 10**9
        gas = int(gas_float)
        gasbuy=gas+150
        try:
            txt = open("4wallet.txt").read().splitlines()[i]
            sender_address10 = txt.split("|")[0]
            sender =sender_address10.lower()[2:1000]
            private10 = txt.split("|")[1]
            data ="0xb066ea7c00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000000000000"+sender+"00000000000000000000000000000000000000000000000000000000"+hex_timestamp+"000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000000000000e000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002000000000000000000000000b31f66aa3c1e785363f0875a1b74e27b85fd66c7000000000000000000000000"+tokenToBuy2
            sTO = web3.toChecksumAddress('0xb4315e873dBcf96Ffd0acd8EA43f689D8c20fB30')#tradejoi


            transaction_dict = {'from':sender_address10,
                                'to':sTO,
                                'chainId':43114,
                                'value': web3.toWei(0.7,'ether'),
                                'gasPrice':web3.toWei(gasbuy,'gwei'),
                                'gas':500000 ,
                                'nonce':web3.eth.get_transaction_count(sender_address10),
                                'data':data}
            signed_transaction_dict = web3.eth.account.signTransaction(transaction_dict, private10)
            tx_token1 = web3.eth.send_raw_transaction(signed_transaction_dict.rawTransaction)
            print(web3.toHex(tx_token1))
        except:
            print('erro')



def buymulti():
    for i in range(4):
        gas_price1 = web3.eth.gasPrice
        gas_float = gas_price1 / 10**9
        gas = int(gas_float)
        gasbuy=gas+550
        try:
            txt = open("4wallet.txt").read().splitlines()[i]
            sender_address10 = txt.split("|")[0]
            private10 = txt.split("|")[1]
            nonce1 = web3.eth.get_transaction_count(sender_address10)
            amount_out_min = 0
            pancakeswap2_txn1 = contract.functions.swapExactAVAXForTokensSupportingFeeOnTransferTokens(
                amount_out_min,
                [spend,tokenToBuy],
                sender_address10,
                (int(time.time()) + 10000)
                ).buildTransaction({
                'from': sender_address10,
                'value': web3.toWei(0.5,'ether'),#đây là số bnb dùng để mua coin multi
                'gas': 1400000,
                'gasPrice':web3.toWei(gasbuy,'gwei'),
                'nonce': nonce1,
                })
            signed_txn1 = web3.eth.account.sign_transaction(pancakeswap2_txn1, private10)
            tx_token1 = web3.eth.send_raw_transaction(signed_txn1.rawTransaction)
            print(web3.toHex(tx_token1))
        except:
            print('next')


def buyMaxTxs():
    for i in range(1):
        gas_price1 = web3.eth.gasPrice
        gas_float = gas_price1 / 10**9
        gas = int(gas_float)
        gasbuy=gas+300
        try:
            txt = open("4wallet.txt").read().splitlines()[i]
            sender_address10 = txt.split("|")[0]
            private10 = txt.split("|")[1]
            nonce1 = web3.eth.get_transaction_count(sender_address10)
            #amount_out_min = 1000*10**9
            amount_out_min = 10000*10**18
            pancakeswap2_txn1 = contract.functions.swapAVAXForExactTokens(
              amount_out_min,
              [spend,tokenToBuy],
              sender_address10,
              (int(time.time()) + 10000)
              ).buildTransaction({
              'from': sender_address10,
              'value': web3.toWei(1,'ether'),
              'gas': 1500000,
              'gasPrice':web3.toWei(gasbuy,'gwei'),
              'nonce': nonce1,
              })
            signed_txn1 = web3.eth.account.sign_transaction(pancakeswap2_txn1, private10)
            tx_token1 = web3.eth.send_raw_transaction(signed_txn1.rawTransaction)
            print(web3.toHex(tx_token1))   

        except:
            print('ee')   

def balancetoken(sellTokenContract):
    tuan_wallet=web3.toChecksumAddress(tuan)
    while 1:
        balance = sellTokenContract.functions.balanceOf(tuan_wallet).call()
        balance_dev1 = int(web3.toWei(balance,'ether'))
        print('Balance now:'+str(balance_dev1))

###########################################################################################################################

token = '0x265A650ECc71a8Ef49552911aE3575CA3f7169bA'

tokenToBuy2= token.lower()[2:1000]

tokenToBuy = web3.toChecksumAddress(token)

dev_wallet = web3.toChecksumAddress('0x9fa0DE3053f8358325f7ffE8474F52b4e306b09E')




#--------------------------------------------------------------------------------------------------------------------------

#sellAbi  = '[{"type":"constructor","stateMutability":"nonpayable","inputs":[]},{"type":"event","name":"Approval","inputs":[{"type":"address","name":"owner","internalType":"address","indexed":true},{"type":"address","name":"spender","internalType":"address","indexed":true},{"type":"uint256","name":"value","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"OwnershipTransferred","inputs":[{"type":"address","name":"previousOwner","internalType":"address","indexed":true},{"type":"address","name":"newOwner","internalType":"address","indexed":true}],"anonymous":false},{"type":"event","name":"Transfer","inputs":[{"type":"address","name":"from","internalType":"address","indexed":true},{"type":"address","name":"to","internalType":"address","indexed":true},{"type":"uint256","name":"value","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"TREEBA","inputs":[{"type":"uint256","name":"Taxfee","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"_Marketing","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint8","name":"","internalType":"uint8"}],"name":"_decimals","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"_liquidityFee","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"_name","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"_symbol","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"_taxFee","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"allowance","inputs":[{"type":"address","name":"owner","internalType":"address"},{"type":"address","name":"spender","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"approve","inputs":[{"type":"address","name":"spender","internalType":"address"},{"type":"uint256","name":"amount","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"balanceOf","inputs":[{"type":"address","name":"account","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint8","name":"","internalType":"uint8"}],"name":"decimals","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"decreaseAllowance","inputs":[{"type":"address","name":"spender","internalType":"address"},{"type":"uint256","name":"subtractedValue","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"getOwner","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"increaseAllowance","inputs":[{"type":"address","name":"spender","internalType":"address"},{"type":"uint256","name":"addedValue","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"marketingWallet","inputs":[{"type":"address","name":"Newmarketing","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"name","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"owner","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"renounceOwnership","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setLiqFee","inputs":[{"type":"uint256","name":"LiqFee","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"symbol","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"totalSupply","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"transfer","inputs":[{"type":"address","name":"recipient","internalType":"address"},{"type":"uint256","name":"amount","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"transferFrom","inputs":[{"type":"address","name":"sender","internalType":"address"},{"type":"address","name":"recipient","internalType":"address"},{"type":"uint256","name":"amount","internalType":"uint256"}]}]'

sellAbi  = '[{"type":"constructor","stateMutability":"nonpayable","inputs":[]},{"type":"event","name":"Approval","inputs":[{"type":"address","name":"owner","internalType":"address","indexed":true},{"type":"address","name":"spender","internalType":"address","indexed":true},{"type":"uint256","name":"value","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"Transfer","inputs":[{"type":"address","name":"from","internalType":"address","indexed":true},{"type":"address","name":"to","internalType":"address","indexed":true},{"type":"uint256","name":"value","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"allowance","inputs":[{"type":"address","name":"owner","internalType":"address"},{"type":"address","name":"spender","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"approve","inputs":[{"type":"address","name":"spender","internalType":"address"},{"type":"uint256","name":"amount","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"balanceOf","inputs":[{"type":"address","name":"account","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint8","name":"","internalType":"uint8"}],"name":"decimals","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"decreaseAllowance","inputs":[{"type":"address","name":"spender","internalType":"address"},{"type":"uint256","name":"subtractedValue","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"increaseAllowance","inputs":[{"type":"address","name":"spender","internalType":"address"},{"type":"uint256","name":"addedValue","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"name","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"symbol","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"totalSupply","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"transfer","inputs":[{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"amount","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"transferFrom","inputs":[{"type":"address","name":"from","internalType":"address"},{"type":"address","name":"to","internalType":"address"},{"type":"uint256","name":"amount","internalType":"uint256"}]}]'
#--------------------------------------------------------------------------------------------------------------------------
sellTokenContract = web3.eth.contract(tokenToBuy, abi=sellAbi)

blocks = web3.eth.block_number
print(blocks)



#balance token


balance = sellTokenContract.functions.balanceOf(dev_wallet).call()
balance_dev1 = int(web3.toWei(balance,'ether'))
print('------AVAX-------')
print(balance_dev1)



GH=27768000000000000000000000000000000000000000000000
buytime =GH
print(buytime)
print('---------------')
if buytime == balance_dev1:
    print('------working------')
    blocks = web3.eth.block_number
    print(blocks)
    while 1:
            gas_price1 = web3.eth.gasPrice
            gas_float = gas_price1 / 10**9
            gas = int(gas_float)
            if gas < 2000:
                balance = sellTokenContract.functions.balanceOf(dev_wallet).call()
                balance_dev1 = int(web3.toWei(balance,'ether'))
                #print('Balance dev now:'+str(balance_dev1))
                if balance_dev1 != buytime:
                    buymulti()
                    print('buy')
                    balancetoken(sellTokenContract)
                    close = input()
    print('done')
else:
    print('check lai balance dev')











'''
#balance avax

receved_Wallet = dev_wallet
balance1 = web3.eth.get_balance(receved_Wallet)
humanReadable = web3.fromWei(balance1,'ether')
BalanceBNB=round(humanReadable,4)
print(receved_Wallet+'dev|'+str(BalanceBNB))



GH=71

blocks = web3.eth.block_number
print(blocks)
while 1:
        receved_Wallet = dev_wallet
        balance1 = web3.eth.get_balance(receved_Wallet)
        humanReadable = web3.fromWei(balance1,'ether')
        BalanceBNB=round(humanReadable,4)
        print(receved_Wallet+'dev|'+str(BalanceBNB))
        if BalanceBNB < GH:
            #senddata()
            print('buy')
            balancetoken(sellTokenContract)
            close = input()


print('done')





#balance token


balance = sellTokenContract.functions.balanceOf(dev_wallet).call()
balance_dev1 = int(web3.toWei(balance,'ether'))
print('---------------')
print(balance_dev1)



GH=694200000000000000000000000000000
buytime =GH
print(buytime)
print('---------------')
if buytime == balance_dev1:
    print('------working------')
    blocks = web3.eth.block_number
    print(blocks)
    while 1:
            gas_price1 = web3.eth.gasPrice
            gas_float = gas_price1 / 10**9
            gas = int(gas_float)
            if gas < 2000:
                balance = sellTokenContract.functions.balanceOf(dev_wallet).call()
                balance_dev1 = int(web3.toWei(balance,'ether'))
                #print('Balance dev now:'+str(balance_dev1))
                if balance_dev1 != buytime:
                    #senddata()
                    print('buy')
                    balancetoken(sellTokenContract)
                    close = input()
    print('done')
else:
    print('check lai balance dev')












'''
'''

v2='0x60aE616a2155Ee3d9A68541Ba4544862310933d4'
v21='0xb4315e873dBcf96Ffd0acd8EA43f689D8c20fB30'

GH=20000000000000000000000000000000000000000

blocks = web3.eth.block_number
print(blocks)
while 1:
        balance = sellTokenContract.functions.balanceOf(dev_wallet).call()
        balance_dev1 = int(web3.toWei(balance,'ether'))
        print('Balance dev now:'+str(balance_dev1))
        if balance_dev1 != GH:
            #buymulti()
            close = input()


print('done')


'''













'''
0xb066ea7c
0000000000000000000000000000000000000000000000000000000000000000  ;minout
0000000000000000000000000000000000000000000000000000000000000080   ; giữ nguyên 128
00000000000000000000000068361413a9a21e4848ba8ac248ab0a14e7456385   ; ví mua
0000000000000000000000000000000000000000000000000000000065773ddc   ; time
0000000000000000000000000000000000000000000000000000000000000060
00000000000000000000000000000000000000000000000000000000000000a0
00000000000000000000000000000000000000000000000000000000000000e0
0000000000000000000000000000000000000000000000000000000000000001
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000001
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000002
000000000000000000000000b31f66aa3c1e785363f0875a1b74e27b85fd66c7
000000000000000000000000299363917407290052eb8c5d9cfa954a2edb2cf2
'''


