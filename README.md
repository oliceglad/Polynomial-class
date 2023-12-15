# Polynomial class

## 1. Find the sum of polynomials
```
  poly1 = Poly([1,4,0.3654,-6,-1,0])
  poly2 = Poly()
  poly3 = Poly(1)
  poly4 = Poly(1,-2,-3.12345)
  print(poly1+poly2)
  print(poly1+poly3)
  print(poly1+poly4)
  print(poly2+poly3)
  print(poly1+5)
  print(8.1+poly3)
```
## 2. Find the multiply of polynomials or integers and floats
```
poly1 = Poly([1, 1])
poly2 = Poly(2, 1)
print(poly1 * poly2)
```
## 3. Fint the difference of polynomials or integers and floats
```
poly1 = Poly([1,4,0.3654,-6,-1,0])
poly2 = Poly()
poly3 = Poly(1)
poly4 = Poly(1,-2,-3.12345)
print(poly1-poly2)
print(poly1-poly3)
print(poly1-poly4)
print(poly2-poly3)
print(poly1-poly1)
print(poly1-4)
print(3.5-poly2)
```
## 4. Compare two polynomials together or with integers and floats
```
poly1 = Poly([1,4,0.3654,-6,-1,0])
poly2 = Poly()
poly3 = Poly(1)
poly4 = Poly(1,-2,-3.12345)
print(poly1 == poly1)
print(poly1 == poly2)
print(poly3 == poly3)
print(poly1 == poly4)
print(poly3 == 1)
print(0 == poly2)
print(2 == poly2)
```
## 5. To know about degree of polynomial
```
poly1 = Poly([-6, -2, 5, 1])
print(poly1.degree())
```
## 6. Create polynomial from string numbers
```
print(Poly.poly_from_str('1 2 3'))
```
## 7. Solve a QuadraticPolynomial by using Discriminant
Important   - your polynomial`s degree must be 2
```
poly1 = QuadraticPolynomial(2, 3, 1)
print(poly1.solve())
```
