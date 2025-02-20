# Slice operations on a string
st = 'hellow world'
print(st[1])
print(st[1:10])
print(st[1:10+1])
print(st[-1])
print(st[-8])
print(st[:])
print(st[3:9:2])
print(st[3:9:3])
print(st[::])
print(st[::3])     # every 3rd element
print(st[::-1])
print(st[::-3])   # every 3rd element in reverse order
print(st[:1:-2])  # every 2nd element in reverse order
print(st[1:1:1])  # Empty string

# print(type(st))