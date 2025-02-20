try:
    # pass
    print(i)        # NameError: name 'i' is not defined
except:
    print("Caught Exception!!!")
finally:
    print('~Cumpulsory Executed Block~')