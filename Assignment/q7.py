def foo(fun_list):
    fun_list.append(30)

def foo1(fun_list):
    del fun_list[1]

ls=[10,20]
ls1=ls
print(ls)
print('ls id:',id(ls))
print(ls1)
print('ls1 id:',id(ls1))

foo(ls)
print(ls)
print('ls id:',id(ls))

print(ls1)
print('ls1 id:',id(ls1))

foo1(ls)
print(ls)
print(ls1)