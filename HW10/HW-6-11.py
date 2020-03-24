def computeCommission(salesAmount):
    if salesAmount <= 5000:
        return salesAmount * 0.08
    elif 5000 < salesAmount and salesAmount <= 10000:
        return 400 + (salesAmount - 5000)*0.1
    elif salesAmount > 10000:
        return 400 + 500 + (salesAmount - 10000)*0.12


def main():
    print("{0:1}  {1:2}".format("Sales Amount", "Commission"))
    for i in range(10000, 100001, 5000):
        print("{0:<15}{1:9}".format(i, computeCommission(i)))

main()