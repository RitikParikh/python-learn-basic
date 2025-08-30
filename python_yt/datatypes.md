# Data Types / Object Types

- Number: 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
- String : 'spam', "Bob's",  b'a\x01c', u'sp\xc4m'
- List: [1, [2, 'three'], 4,5], list(range(10))
- Tuple: (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dict(Dictionary): {'food': 'spam', 'taste':'Yum'}, dict(hours=10)
- Set: set('abc'), {'a','b', 'c '}
- File: It is not datatype bundle large file so it here: open('eggs.txt'), open(r'C:\ham.bin','wb')
- Boolean: True, False
- None: None
- Functions, modules, classes
- Advance : Decorators, Generators, Iterators, Meta Programming, Comprehensions, Context Mangers

Shall
>>> 12+12
24
>>> 2.5 * 5
12.5
>>> 2 ** 5
32
>>> 2 ** 100
1267650600228229401496703205376
>>> import math
>>> math.pi
3.141592653589793
>>> import random
>>> random.random()
0.8636664706060747
>>> random.choice([1,2,3,4,5])
3
>>> username = "hello_world"
>>> len(username)
11
>>> username[0]
'h'
>>> username[0] = 'A'
Traceback (most recent call last):
  File "<python-input-12>", line 1, in <module>
    username[0] = 'A'
    ~~~~~~~~^^^
TypeError: 'str' object does not support item assignment
>>> username[-1]
'd'
>>> username[1:3]
'el'
>>> mylist = [123, "chai",3.14]
>>> mylist
[123, 'chai', 3.14]
>>> len(mylist)
3
>>> myD = {"one":'ginger', "two":"lemon", "comic":"nagraj" }
>>> myD['one']
'ginger'
>>> myTup = (1,2,4)
>>> myTup[0]
1