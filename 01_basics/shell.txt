Python shell initiate using --> python3 in terminal
print (10)

2+2

3+5

"hello-world" * 8

score = 100
score

goal gives error (Name error also called as a namespace error)

import os
os.ced()

Loops 
for c in "chai":
... print(c)
IndentationError: expected an indented block when wrong becket open close
for c in "chai":
...     print(c)
...     

import sys
>>> sys.plateform

    sys.plateform --> wromg error
AttributeError: module 'sys' has no attribute 'plateform'. Did you mean: 'platform'?
>>> sys.platform
'darwin'

# ModuleNotFoundError: No module named 'hello_world' --
--> calleing from wrong dir

>>> import hello_world
Ritik or python
Lemon tea
>>> hello_world.hello("ss")
ss


Import reload to python take new code

from importlib import reload
>>> reload(hello_world)
Ritik or python
Lemon tea
<module 'hello_world' from '/Users/ritikparikh/ritik/python-learn-basic/01_basics/hello_world.py'>
>>> hello_world.one
'One'