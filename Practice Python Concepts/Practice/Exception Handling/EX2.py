try:
    # i = 9   
    print(i)        # NameError: name 'i' is not defined
except NameError:
    print("There is an ERROR: Variable is NOT Defined!!!")
except:     # Anythig else other than NameError
    print('Something is WRONG!!!')