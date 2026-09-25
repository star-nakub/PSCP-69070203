"""x"""
def calc(units):
    """calc"""
    base_cost = 0.0
    if units > 200:
        base_cost += (units - 200) * 15
        units = 200
    if units > 100:
        base_cost += (units - 100) * 12
        units = 100
    if units > 50:
        base_cost += (units - 50) * 10
        units = 50
    if units > 10:
        base_cost += (units - 10) * 7
        units = 10
    if units > 0:
        base_cost += units * 5
    vat = base_cost * 0.07
    return base_cost, vat
def main():
    """main"""
    N = int(input())
    base_cost, vat = calc(N)
    ft_cost = N * 0.50
    total_bill = base_cost + vat + ft_cost
    print(f"{total_bill:.1f}")
if __name__ == "__main__":
    main()
