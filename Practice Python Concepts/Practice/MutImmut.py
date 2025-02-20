def func(t1):
    del t1[2]
    for i in t1:
        print(i)

li = [1,2,3,4,5]    #list
tu = (1,2,3,4,5)

func(li)
func(tu)  # TypeError: 'tuple' object doesn't support item deletion
