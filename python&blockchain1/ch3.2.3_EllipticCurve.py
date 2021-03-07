##模拟椭圆曲线算法的过程
##本文为数学展示，未作改动
def inv_mod(b, p):
    if b < 0 or p <= b:
        b = b % p

    c, d = b, p
    uc, vc, ud, vd = 1, 0, 0, 1
    while c != 0:
        q, c, d = divmod(d, c) + (c,)
        uc, vc, ud, vd = ud - q * uc, vd - q * vc, uc, vc

    # 如果d==1，则报错无解
    assert d == 1
    if ud > 0:
        return ud
    else:
        return ud + p

inv_mod(2,23)

3*inv_mod(2,23)%23



#展示所有的点
def show_points(p,a,b):
    return [(x, y) for x in range(p) for y in range(p)
            if (y*y-(x*x*x+a*x+b))%p ==0]

show_points(p=29, a=4, b=20)

