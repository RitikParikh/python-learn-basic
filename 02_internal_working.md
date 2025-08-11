## 

#### 1. Memory Object reference count -> In background python has reference count but when we use to print it interpreter manipulates dons't so correct value

##### Shall
 - import sys
 - sys.getrefcount(24601) //Output 3
 - sys.getrefcount('ritik') //Output 3
 - sys.getrefcount('r') //Output 4294967295
 - sys.getrefcount('ritik') //Output 3
 - sys.getrefcount('riti') //Output 3
 - sys.getrefcount('r') //Output 4294967295

### 2. How Ref works
- In python any datatype it stays on memory not on variable 

### 3. Exception for garbage collection 
- For numbers and string garbage collection happen some time after because python assumes if same value came again then it reduce some computation on that
- we can forcefully also can collect the garbage 

### 4. List memory management
- Numbers and strings are immutable so it only reference out never updates
- In the list is a mutable datatype so value can change and it in memory it behave different from string and numbers
- ## List example 1:
   - myListOne = [1,2,3]
   - myListTwo = myListOne  
   - So now if print both it give same value with it is reference same object now because we assign myListOne to myListTwo
   - So now we change one value in it
    - myListOne[0] = 33
    - So here if print myListOne to myListTwo then it shows myListOne is [1,2,33] and myListTwo [1,2,33]
    - Why it happen because it reference same value
- ## List Example 2:
  - myListOne = [1,2,3]
  - myListTwo = myListOne  
  - myListOne = [1,2,33]
  - So if print both then myListOne prints the [1,2,33] but myListTwo [1,2,3]
    because we make new reference for list one

### In python we some comparison method for checking
- Like take 
- Example:1 again
- myListOne == myListTwo //True
- myListOne is myListTwo //True

--
- Example:3 
myListOne = [1,2,33] and myListTwo = [1,2,33]
- myListOne == myListTwo //True
- myListOne is myListTwo //False

-This happen because '==' check the value comparison but 'is' check the variable references in ex3 i assign same value two time list is mutable so it create two same data but references are different

### Copy
- Ex1:  
- h1 = [1,2,3]
- h2 = h1[:] //using slice to copy the List
Other method copy is
import copy
h3 = copy.copy(h1)
h4 = copy.deepcodpy(h1) //Use for nested data copy