from collections import defaultdict
test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
print("Original:",test_list)
res=defaultdict(list)
for ele in test_list:
    res[ele].append(ele)
print(dict(res))