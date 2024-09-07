def geometric_progression(a, r, n):
    try:
        a, r, n = float(a), float(r), int(n)
        if n < 0:
            raise ValueError("Number of terms must be non-negative")
        if n == 0:
            return 1
        else:
            return a * geometric_progression(a * r, r, n - 1)
    except (ValueError, TypeError) as e:
        print(f"Invalid input for geometric progression: {e}")
        return None


def sum_geometric_progression(a, r, n):
    try:
        a, r, n = float(a), float(r), int(n)
        if n < 0:
            raise ValueError("Number of terms must be non-negative")
        if n == 0:
            return 0
        else:
            return a + sum_geometric_progression(a * r, r, n - 1)
    except (ValueError, TypeError) as e:
        print(f"Invalid input for geometric progression: {e}")
        return None


def arithmetic_progression(a, d, n):
    try:
        a, d, n = int(a), int(d), int(n)
        if n < 0:
            raise ValueError("Number of terms must be non-negative")
        if n == 0:
            return a
        else:
            return a + d * n
    except (ValueError, TypeError) as e:
        print(f"Invalid input for arithmetic progression: {e}")
        return None


def binary_representation(n):
    try:
        n = int(n)
        if n < 0:
            raise ValueError("Input must be non-negative")
        if n == 0:
            return 0
        else:
            return n % 2 + 10 * binary_representation(n // 2)
    except (ValueError, TypeError) as e:
        print(f"Invalid input for binary representation: {e}")
        return None


def gcd(a, b):
    try:
        a, b = int(a), int(b)
        if a < 0 or b < 0:
            raise ValueError("Both numbers must be non-negative")
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    except (ValueError, TypeError) as e:
        print(f"Invalid input for GCD: {e}")
        return None


def lcm(a, b):
    try:
        a, b = int(a), int(b)
        if a < 0 or b < 0:
            raise ValueError("Both numbers must be non-negative")
        return a * b // gcd(a, b)
    except (ValueError, TypeError) as e:
        print(f"Invalid input for LCM: {e}")
        return None


"Доделать ввод через консоль и проверить коректность"


def main():
    print(geometric_progression(2, 3, 5))
    print(sum_geometric_progression(2, 3, 5))
    print(arithmetic_progression(5, 2, 5))
    print(binary_representation(10))
    print(gcd(48, 18))
    print(lcm(48, 18))


if __name__ == '__main__':
    main()
