

##不确定性钱包工作原理
from simchain import Wallet

# 创建一个钱包
w = Wallet()

# 随机生成10对密钥
for _ in range(10):
    w.generate_keys()
w.nok

# 访问最后一对密钥中私钥的字节串编码
w.keys[-1].sk.to_bytes()

# 访问倒数第二对密钥中私钥的字节串编码
w.keys[8].sk.to_bytes()

##分层确定性钱包
import os
import hashlib
import hmac
from simchain import SigningKey

# 生成一个随机种子，256位
master_seed = os.urandom(32)
master_seed

# 使用HMAC-SHA512运算得到512位输出
deriv = hmac.new(key=b'Simchain seed', msg=master_seed, digestmod=hashlib.sha512).digest()

# 取输出的左边256位生成主私钥
master_privkey_str = deriv[:32]
master_privkey = SigningKey.from_bytes(master_privkey_str)
master_privkey.to_bytes()

# 由主私钥生成主公钥
master_pubkey = master_privkey.get_verifying_key()
master_privkey.to_bytes()

from simchain.ecc import convert_pubkey_to_addr
# 由主公钥生成主地址
convert_pubkey_to_addr(master_privkey.to_bytes())


##衍生密钥(通过具体的算法来演示
# 获得主链码
master_chain = deriv[32:]

from simchain.ecc import number_to_bytes

# 衍生主私钥的索引为1的子密钥
idx = 1
# 将整数转换为字节串
idx_str = number_to_bytes(idx, 4)
idx_str

# 将主私钥与索引组合
message = master_privkey_str + idx_str
# 将主链码作为钥匙，主私钥和索引组合作为消息进行HMAC-SHA512运算
deriv_child = hmac.new(key=master_chain, msg=message, digestmod=hashlib.sha512).digest()
# 取输出的左256位作为子私钥
child_privkey_str = deriv_child[:32]
child_privkey_str

# 生成子私钥
child_privkey = SigningKey.from_bytes(child_privkey_str)
child_privkey.to_bytes()

# 生成子公钥
child_pubkey = child_privkey.get_verifying_key()
child_pubkey.to_bytes()

# 生成子地址
convert_pubkey_to_addr(child_pubkey.to_bytes())

##生成分层确定性钱包

from simchain.hdwallet import Keys
import os

# 生成随机种子
seed = os.urandom(32)
# 通过种子生成主密钥
master_keys = Keys.from_master_seed(seed)
# 访问主密钥私钥的字节串编码
master_keys.sk.to_bytes()

# 访问主密钥公钥的字节串编码
master_keys.pk.to_bytes()

# 主密钥的深度为0
master_keys.depth

# 返回为None，表示没有父亲
master_keys.child_index

# 主密钥衍生成2个字密钥，索引为0和1
child0 = master_keys.child(0)
child1 = master_keys.child(1)
# 子密钥的深度都为1
assert child0.depth == child1.depth

child0.child_index

child1.child_index

child0.sk.to_bytes()

child0.pk.to_bytes()

# 子密钥链码
child0.chain

# 生成孙密钥，索引分别为2和4
grandson2 = child0.child(2)
grandson4 = child1.child(4)
# 孙密钥深度为2
assert grandson2.depth == grandson4.depth == 2

grandson2.child_index

grandson4.child_index

##将“种子”转换为可逆的助记符
from simchain.mnemonics import Mnemonics
# 生成种子
seed = os.urandom(32)
seed

# 生成助记词对象
m = Mnemonics(seed)
# 中文助记符
m.chinese


# 英文助记符
m.english

# 由中文助记词得到种子
seed1 = Mnemonics.decode_from_chinese(m.chinese)
seed1

# 由英文助记词得到种子
seed2 = Mnemonics.decode_from_english(m.english)
seed2