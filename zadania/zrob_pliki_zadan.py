import os

x = {1: 19,
     2: 11,
     3: 68,
     4: 57}

for dir_number in x:
    os.mkdir("{}".format(dir_number))
    for i in range(1, x[dir_number] + 1):
        open("{0}/{0}_{1}.py".format(dir_number, i), "w")
