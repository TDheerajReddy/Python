# User definer Exception
x = 5
if x < 0:
    raise Exception('Negative Number are not allowed!!!')

st = 'jabbaz Eagle Baba'
if not type(st) is int:
    raise Exception('Sorry, Only int values are allowed!!!')
else:
    print('Successfully Executed')
