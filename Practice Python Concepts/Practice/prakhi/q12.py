s="hello world"
print(s.lower())
print(s.isupper())
print(s.startswith('o'))
print(s.join('1234'))
print(s.split('w'))
#print(s.split())
print(s.rjust(60))
print(s.ljust(60))
print(s.center(60))     # half of the 60
s="             hello world"
print(s.lstrip())       # remove the left space\
s="'''''''''''''hello world"
print(s.lstrip(" h' ")) 
