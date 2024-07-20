with open('currency_conveter/rate.txt') as f:
    lines = f.readlines()

for line in lines:
    passed = line.split("\t")
    print(passed)
