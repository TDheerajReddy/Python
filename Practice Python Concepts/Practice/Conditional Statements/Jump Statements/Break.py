#Break Statement
i = 1
pass
for i in range(5):      # by default i value is 0, so the Output without break is 0, 1 , 2, 3, 4
    if i == 4:
        break
    print(i)