def gcd(n1: int, n2: int) -> int:
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1

def lcm(n1, n2):
    divisor = gcd(n1, n2)
    return n1 * n2 // divisor

def test_gcd_lcm():
    # GCD tests
    assert gcd(48, 18) == 6
    assert gcd(7, 3) == 1
    assert gcd(100, 10) == 10
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5

    # LCM tests
    assert lcm(4, 6) == 12
    assert lcm(7, 3) == 21
    assert lcm(10, 5) == 10
    assert lcm(0, 5) == 0
    assert lcm(5, 0) == 0

    print("All tests passed.")

test_gcd_lcm()