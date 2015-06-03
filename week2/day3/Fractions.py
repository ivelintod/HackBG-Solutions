class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        if self.numerator == 0:
            return "{}".format(str(0))
        elif self.denominator == 1:
            return "{}".format(self.numerator)
        elif self.numerator == self.denominator:
            return "{}".format(str(1))
        else:
            return "{0} / {1}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        res_num = []
        res_denom = []
        for i in range(2, abs(new_numerator) + 1):
            if abs(new_numerator) % i == 0:
                res_num.append(i)
        for i in range(2, abs(new_denominator) + 1):
            if abs(new_denominator) % i == 0:
                res_denom.append(i)

        if abs(new_numerator) > abs(new_denominator):
            for denom in res_denom:
                if new_numerator % denom == 0:
                    new_numerator /= denom
                    new_denominator /= denom
        elif abs(new_numerator) < abs(new_denominator):
            for num in res_num:
                if new_denominator % num == 0:
                    new_denominator /= num
                    new_numerator /= num
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        res_num = []
        res_denom = []
        for i in range(2, abs(new_numerator) + 1):
            if abs(new_numerator) % i == 0:
                res_num.append(i)
        for i in range(2, abs(new_denominator) + 1):
            if abs(new_denominator) % i == 0:
                res_denom.append(i)

        if abs(new_numerator) > abs(new_denominator):
            for denom in res_denom:
                if new_numerator % denom == 0:
                    new_numerator /= denom
                    new_denominator /= denom
        elif abs(new_numerator) < abs(new_denominator):
            for num in res_num:
                if new_denominator % num == 0:
                    new_denominator /= num
                    new_numerator /= num

        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        res_num = []
        res_denom = []
        for i in range(2, abs(new_numerator) + 1):
            if abs(new_numerator) % i == 0:
                res_num.append(i)
        for i in range(2, abs(new_denominator) + 1):
            if abs(new_denominator) % i == 0:
                res_denom.append(i)

        if abs(new_numerator) > abs(new_denominator):
            for denom in res_denom:
                if new_numerator % denom == 0:
                    new_numerator /= denom
                    new_denominator /= denom
        elif abs(new_numerator) < abs(new_denominator):
            for num in res_num:
                if new_denominator % num == 0:
                    new_denominator /= num
                    new_numerator /= num

        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        self.numerator / self.denominator, other.numerator / other.denominator

a = Fraction(2, 23)
b = Fraction(5, 4)
print (a * b)
