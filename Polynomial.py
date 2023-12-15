from typing import List

class Poly:

    """
    Polynomial class

    degre - degree of a polynomial
    coefficients - coefficients of a polynomial

    """
    def __init__(self, *coefficients) -> None:
        self.degre: int = 0

        if (len(coefficients) > 0 and type(coefficients[0]) == list):
            self.coefficients: tuple = tuple(coefficients[0])
        elif len(coefficients) == 0:
            self.coefficients: tuple = tuple([0])
        else:
            self.coefficients: tuple = coefficients

    def __repr__(self) -> str:
        """
        :return: Poly((coeffitients))
        """
        if len(self.coefficients) == 1:
            return f"'Poly(({self.coefficients[0]}))'"
        return f"'Poly({self.coefficients})'"

    def __str__(self) -> str:
        """
        str method create polynom's equation with self coeffitients
        :return: polynom's equation with x (example - x^2 + 1)
        """
        if all(coef == 0 for coef in self.coefficients):
            return "0"

        terms: List = []
        for degre, coef in enumerate(self.coefficients):
            if coef == 0:
                continue

            term: str = ""
            if coef != 1 or degre == 0:
                if not isinstance(coef, float):
                    term += str(coef)
                else:
                    if len(str(coef).split('.')[1]) >= 3:
                        coef = round(coef, 3)
                    term += f"{coef}" if coef != 1 else ""

            if degre > 0:
                term += f"x^{degre}" if degre > 1 else "x"

            self.degre = degre

            terms.append(term)

        result: str = " + ".join(reversed(terms))

        result = result.replace('-1x', '-x')

        return result.replace("+ -", "- ").lstrip("+") if result else "0"

    def degree(self) -> int:
        """
        degree method - about polynom's degree
        :return: integer polynom's degree
        """
        self.__str__()
        return self.degre

    def __eq__(self, other) -> bool:
        """
        P1 == P2 ?
        simple method
        :param other: second term
        :return: comparison between first term and second term
        """
        if isinstance(other, (int, float)):
            other: Poly = Poly(other)

        return self.coefficients == other.coefficients

    def __radd__(self, other):
        return self + Poly(other)

    def __neg__(self):
        return Poly([- elem for elem in self.coefficients])

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return other + (- self)

    def __iadd__(self, other):
        return self + other

    def __add__(self, other):
        """
        P1 + P2 ?

        If other == 0 return the same Poly

        Create two lists for new Poly
        new_compared = a list with new coeffitients after sum
        coeff_to_summ = a list with coeffitients which need to add to self coeffitients

        find max length list and count to summ if other not integer or float
        else create list with one element: integer or float number

        Cycle:
            while count_to_summ > 0 (variable about how many numbers need to add from list second term coeffitients)
            find sum and add to new_compared
            count_to_summ -= 1

            else
            just add remaining coeffitients to new list new_compared

        :param other: second term
        :return: new Poly with sum between first term and second term
        """
        if str(other) == "0":
            return Poly(*self.coefficients)
        else:
            new_compared: List = []
            coeff_to_summ: List = []

            if not isinstance(other, int) and not isinstance(other, float):
                max_step: int = len(self.coefficients) if len(self.coefficients) > len(other.coefficients) else len(other.coefficients)
                count_to_summ: int = len(self.coefficients) if len(self.coefficients) < len(other.coefficients) else len(other.coefficients)
                coeff_to_summ = list(other.coefficients).copy()
            else:
                max_step: int = len(self.coefficients)
                coeff_to_summ.append(other)
                count_to_summ: int = 1

            for i in range(max_step):
                if count_to_summ > 0:
                    numb: int = self.coefficients[i] + coeff_to_summ[i]
                    new_compared.append(numb)
                    count_to_summ -= 1
                else:
                    if len(coeff_to_summ) > len(self.coefficients):
                        new_compared.append(coeff_to_summ[i])
                    else:
                        new_compared.append(self.coefficients[i])
            return Poly(*new_compared)

    def __rmul__(self, other):
        return self * other

    def __mul__(self, other):
        """
        P1 * P2 ?

        if other is integer or float we multiply coef
        from self.coeffitients and other together and return new Poly class

        if other is Poly we find new degree for new Poly class and in cycle we multiply
        coef first multiplier and coef second multiplier


        :param other: other is integer or float or Poly class
        :return:
        """
        if isinstance(other, (int, float)):
            result_coefficients = [coef * other for coef in self.coefficients]
            return Poly(*result_coefficients)

        if isinstance(other, Poly):
            result_degree = self.degree() + other.degree()
            result_coefficients = [0] * (result_degree + 1)

            for i, coef_self in enumerate(self.coefficients):
                for j, coef_other in enumerate(other.coefficients):
                    result_coefficients[i + j] += coef_self * coef_other

            return Poly(*result_coefficients)

    @staticmethod
    def poly_from_str(coeff_str: str):
        """
        '1, 2, 3' -> 3x^2 + 2x + 1
    
        :param coeff_str: numbers through space from string
        :return: new Poly class
        """
        coefficients = [int(x) if x.isdigit() or (x[0] == '-' and x[1:].isdigit()) else float(x) for x in
                        coeff_str.split()]
        return Poly(*coefficients)

class DegreeIsTooBigException(Exception):
    def __init__(self, qpoly):
        self.qpoly = qpoly

class QuadraticPolynomial(Poly):
    def __init__(self, *coefficients):
        super().__init__(*coefficients)

    def solve(self):
        if self.degree() > 2:
            raise DegreeIsTooBigException(self)

        a, b, c = reversed(self.coefficients)

        if a == 0:
            if b == 0:
                return []
            else:
                root = -c / b
                return [int(root)] if isinstance(root, float) and root.is_integer() else [round(root, 3)]

        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:
            root1 = (-b + discriminant ** 0.5) / (2 * a)
            root2 = (-b - discriminant ** 0.5) / (2 * a)
            roots = [int(root) if root.is_integer() else round(root, 3) for root in [root1, root2]]
            return sorted(roots) if roots else []
        elif discriminant == 0:
            root = -b / (2 * a)
            return [int(root)] if root.is_integer() else [round(root, 3)]
        else:
            return []
