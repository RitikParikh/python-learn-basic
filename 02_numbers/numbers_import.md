### 
- Number import statements
1. Random
 - import random
 - random.random() --> it give random value between 0 and 1
 - random.randint(1,10) --> 2 --> any integer thing between values provide
 - random.choice([1,2,3]) --> 1 --> anything return deom array
 - random.shuffle([1,2,3]) --> [2,1,3] --> shuffles array

2. 0.1 + 0.1 + 0.1 - 0.3 --> 5.551115123125783e-17 () Decimal context manager
solve this 
- from decimal import Decimal
- Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') --> Decimal('0.0')

3. Fractions
- from fractions import Fraction
- myFra = Fraction(2,7)
- myFra -->  Fraction(2,7)


4.Sets datatype (use use for unions, intersections, difference, superset)
- setone = { 1,2,3, 4}
- setone & {1, 3 } --> {1, 3} -> intersections
- setone | {1, 3 ,7} --> {1, 2, 3, 4, 7} --> unions
- setone - {1, 3 ,7} --> {2, 3, 7} --> difference

- One poinmt when you difference make full on set then it not return empty {} instead it return the () because {} type is dictionary

- type of value 
 - type({}) --> <class 'dict'>

- Boolean Type is a number of 0 and 1
- True == 1 --> True in memory it is different

