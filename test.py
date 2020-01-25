import unbit 

n = unbit.unbit(0x4141,'word')
print(n.value)
n.bxor(0x4141)
print(n.value)
n.binc()
print(n.value)
n.bdec()
print(n.value)