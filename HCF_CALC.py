import math

def find_hcf(a, b):
    return math.gcd(a, b)

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    hcf = find_hcf(num1, num2)
    print(f"✅ The HCF of {num1} and {num2} is {hcf}")
