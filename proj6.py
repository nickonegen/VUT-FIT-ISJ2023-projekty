#!/usr/bin/env python3


class Polynomial:
    """Polynomial class"""

    coefs: list = []  # Polynomial coefficients

    def __init__(self, *args, **kwargs) -> None:
        """Polynomial constructor"""
        if len(args) == 1 and isinstance(args[0], list):
            # Argument is a list
            self.coefs = args[0]
        elif len(args) > 0:
            # Argument is a tuple
            self.coefs = list(args)
        else:
            # Argument is a dictionary
            self.coefs = [0] * (max(int(k[1:]) for k in kwargs) + 1)
            for k, v in kwargs.items():
                self.coefs[int(k[1:])] = v

        # Remove trailing zeroes
        while len(self.coefs) > 1 and self.coefs[-1] == 0:
            self.coefs.pop()

    def __str__(self) -> str:
        """Convert polynomial to a human-readable string"""
        members = []  # Members of the polynomial

        for i, c in reversed(list(enumerate(self.coefs))):
            if c != 0:
                # Sign & coefficient
                if i < len(self.coefs) - 1:
                    sign = "- " if c < 0 else "+ "
                    coef = f"{abs(c)}" if abs(c) != 1 or i == 0 else ""
                else:
                    sign = ""
                    coef = f"{c}" if c != 1 or i == 0 else ""

                # Variable & exponent
                if i == 1:
                    var_exp = "x"
                elif i > 1:
                    var_exp = f"x^{i}"
                else:
                    var_exp = ""

                # Combine all and append
                members.append(f"{sign}{coef}{var_exp}")

        # Combine all members and return the result
        return " ".join(members).strip() or "0"

    def __eq__(self, other) -> bool:
        """Compare two polynomials for equality"""
        if not isinstance(other, Polynomial):
            return False

        return self.coefs == other.coefs

    def __add__(self, other) -> "Polynomial":
        """Add two polynomials"""
        if not isinstance(other, Polynomial):
            return False

        # Add corresponding coefficients of both polynomials
        coefs = [a + b for a, b in zip(self.coefs, other.coefs)]

        # Add remaining coefficients of the longer polynomial
        coefs.extend(self.coefs[len(coefs) :])
        coefs.extend(other.coefs[len(coefs) :])

        return Polynomial(coefs)

    def __pow__(self, n):
        """Raise the polynomial to the power of n"""
        result = self
        for _ in range(n - 1):
            result = result * self
        return result

    def __mul__(self, other):
        """Multiply two polynomials"""
        if not isinstance(other, Polynomial):
            return False

        # New list of coefficients with length of both polynomials
        new_coefs = [0] * (len(self.coefs) + len(other.coefs) - 1)

        # Iterate over all coefficients of both polynomials...
        for i, a in enumerate(self.coefs):
            for j, b in enumerate(other.coefs):
                # ...and multiply them
                new_coefs[i + j] += a * b

        return Polynomial(new_coefs)

    def derivative(self):
        """Compute the derivative of the polynomial."""
        # Multiply each coefficient with its exponent
        coefs = [i * c for i, c in enumerate(self.coefs)][1:]
        return Polynomial(coefs)

    def at_value(self, x1, x2=None):
        """Evaluate the polynomial at the given value(s) of x."""
        if x2 is None:
            # One arg provided -- evaluate all at x1
            return sum(c * x1**i for i, c in enumerate(self.coefs))
        # Two args provided -- evaluate difference of x1 and x2
        return self.at_value(x2) - self.at_value(x1)


def test():
    assert (
        str(Polynomial(0, 1, 0, -1, 4, -2, 0, 1, 3, 0))
        == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    )
    assert (
        str(Polynomial([-5, 1, 0, -1, 4, -2, 0, 1, 3, 0]))
        == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    )
    assert (
        str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3=-1, x1=1))
        == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    )
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2, 0, 3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1) + Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1, 1, 1, 0]) + Polynomial(1, -1, 1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1 + pol2) == "3x^2 + x + 1"
    assert str(pol1 + pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1, x1=1) ** 1) == "x - 1"
    assert str(Polynomial(x0=-1, x1=1) ** 2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1, x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2, x1=3, x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2, x1=3, x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2, x1=3, x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2, 3, 4, -5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3, 5) == 44
    pol5 = Polynomial([1, 0, -2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1, 3.6) == -23.92
    assert pol5.at_value(-1, 3.6) == -23.92


if __name__ == "__main__":
    test()
