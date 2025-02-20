#filter function - to filter some elements from any iterative object.
def even(x):
    return(x%2!=1)
L = [1,2,3,4,5,6,7,8,9,10]
E = list(filter(even,L))            #Syntax :- filter(<function>,<iteraterable Object>) return filter object / typecate with list
print(E)