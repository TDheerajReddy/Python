# Read string and find occurence of all characters in a string
st = input('Enter a String : ')
t = set(st)
for i in t:
    for j in st:
        if i == j:
            print(j,'=',st.count(j))
            st = st.replace(j,'')
            break