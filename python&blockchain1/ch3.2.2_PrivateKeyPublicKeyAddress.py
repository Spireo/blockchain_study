##本文测试并建立起全节点交易的密码学安排基础，
# 从Simchain导入Network
from simchain import Network
# 创建一个网络，初始节点12个
net = Network()
# 0号节点命名为ashen_one
ashen_one = net.peers[0]
# 6号节点命名为karla
karla = net.peers[7]

#访问私钥数量
print(ashen_one.wallet.nok)
#访问字节串编码形式的私钥对
print(ashen_one.wallet.keys[0].sk.to_bytes())


print(ashen_one.wallet.addrs[0])

# 生成新的密钥和地址
ashen_one.wallet.generate_keys()

#再次访问私钥数量
print(ashen_one.wallet.nok)

#创建交易：指向karla的地址
ashen_one.create_transaction(karla.wallet.addrs[0], 1000)

#ashen_one广播交易（指将交易信息传输至邻近节点
ashen_one.broadcast_transaction()

# 访问节点创建的最新交易
tx = ashen_one.txs[-1]
print(tx)
# ashen_one创建交易使用的UTXO所在的交易编号
ashen_one.blockchain[0].txs[0].id

# 获取交易的第1个输出单元
vout = ashen_one.blockchain[0].txs[0].tx_out[0]
print(vout)

# 该地址输入ashen_one
print(vout.to_addr in ashen_one.wallet.addrs)
# 指向ashen_one第一个地址
print(ashen_one.wallet.addrs)
#karla验证该交易
assert karla.verify_transaction(tx)

from simchain import Vin

##更换签名验证交易是否能够成立
# 获取交易的输入
vin = tx.tx_in[0]
# 创建新的输入，放入新的签名
vin1 = Vin(vin.to_spend, b'1'*64, vin.pubkey)
# 替换输入单元
tx.tx_in[0] = vin1
# karla验证交易不通过
karla.verify_transaction(tx)

##修改公钥
pk_str = karla.pk
# 创建新的输入单元
vin2 = Vin(vin.to_spend, vin.signature, pk_str)
# 替换输入单元
tx.tx_in[0] = vin2
# karla验证交易不通过
karla.verify_transaction(tx)

from simchain import Pointer
# 创建一个新的定位指针
pointer = Pointer(vin.to_spend.tx_id, 1)
# 新指针指向的输出单元
new_out = ashen_one.blockchain[0].txs[0].tx_out[1]
new_out

# 输出单元指向的地址
new_out.to_addr

#测试该地址是否属于ashen_one
new_out.to_addr in ashen_one.wallet.addrs

# 创建一个新的输入单元
vin3 = Vin(pointer, vin.signature, vin.pubkey)
# 替换输入单元
tx.tx_in[0] = vin3
# karla验证交易不通过
karla.verify_transaction(tx)



