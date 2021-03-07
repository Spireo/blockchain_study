import hashlib
string='be those gentle waves'
value = hashlib.sha256(string.encode())

print(value)
print(type(value))




#调用类方法获得原字节
value.digest()
len=len(value.digest())
print(f"你知道吗，字符串长度是{len}")


# 哈希摘要字节长度
print("哈希摘要字节长度：%s" % value.digest_size)
# 返回十六进制字符串摘要
print("十六进制字符串摘要：%s" % value.hexdigest())
# 内部块长度
print("内部块长度：%s" % value.block_size)

# 直接计算
hashlib.sha256(b'strawberry guy').hexdigest()
