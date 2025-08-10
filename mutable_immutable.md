# Python: Mutable vs Immutable Data Types and Variable Referencing

## Example 1
```python
username = 'Ritik'
username
# Output: 'Ritik'

username = 'Ritik parikh'
username
# Output: 'Ritik parikh'
```

## Example 2
```python
x = 10
y = x
y
# Output: 10

x = 15
y
# Output: 10
```

## Why does this happen? Python: Mutable vs Immutable Data Types and Variable Referencing

In Python, variables do not directly store data.
Instead, variables reference objects in memory. The memory is allocated to the data (object), not to the variable.

## Mutable vs Immutable
 - Immutable data types → Data cannot be changed after creation:

        1. int
        2. float
        3. bool
        4. str
        5. tuple
        6. frozenset
        7. bytes
 - Mutable data types → Data can be changed after creation:

        1. list
        2. set
        3. dictatory
        4. bytearray
        5. array

### Understanding Example 1 (Immutable: String)
  - 'Ritik' is stored in memory, and username references it.
  - When you assign username = 'Ritik parikh', Python creates a new string   object in memory.
  - Now username points to the new string 'Ritik parikh'.
  - The old string 'Ritik' is no longer referenced and becomes garbage.
  - Python's garbage collector removes unreferenced objects automatically.

### Understanding Example 2 (Immutable: Integer)
  - 10 is stored in memory, and x references it.
  - y = x means y also references the same integer 10.
  - When you assign x = 15, Python creates a new integer object for 15.
  - Now: x → 15, y → 10
  
      Since integers are immutable, changing x does not affect y.

  - Key Takeaways
    
    Variables reference data objects in memory; they don't own the memory.
  - Immutable objects cannot be modified in place — changing them creates a new object.
  - Mutable objects can be modified without creating a new object.

  - All data types in Python are objects.