### List
 - Example -> tea_varieties = ["Black", "Green", "Oolong", "White"]
- 1 Zero position element of list -> print(tea_varieties[0]) --> "Black"
- 2 Last element of list -> print(tea_varieties[-1]) --> "White"
- 3 Length of list -> print(len(tea_varieties)) --> 4
- 4 Slice of list -> print(tea_varieties[1:3]) --> ["Green", "Oolong"]
- 4 Hopping of list -> print(tea_varieties[:,2]) --> ["Black", "Oolong"]
- 4 Position value change-> tea_varieties[3] = "Herbal" -> print(tea_varieties) --> ["Black", "Green", "Oolong", "Herbal"]
- 4 add values in array-> tea_varieties[1:1] = ["Herbal"] -> print(tea_varieties) --> ["Black", "Herbal", "Green", "Oolong", "Herbal"]
- 5 remove values in array-> tea_varieties[1:2] = [] -> print(tea_varieties) --> ["Black", "Green", "Oolong", "Herbal"]
- 6 for tea in tea_varieties:
        print(tea)

- 7 end(treat default as /n) statement in print function -> for tea in tea_varieties:
        print(tea, end)
- 8 end assign value statement in print function -> for tea in tea_varieties:
        print(tea, end="-")
- 9 add last in list -> tea_varieties.append("Oolong") --> ["Black", "Green", "Masala", "White", "Oolong"]

- 10 conditional question on list -> 
    if "Oolong" in tea_varieties:
        print("I have Oolong tea") --> "I have Oolong tea"
- 11 Remove last element in list -> tea_varieties.pop() --> ["Black", "Green", "Masala", "White"]
- 12 Remove specific value in list -> tea_varieties.remove("Green") --> ["Black", "Masala", "White"]
- 13 Insert specific value in list -> tea_varieties.insert(1, "Green") --> ["Black", "Green", "Masala", "White"]
- 14 Copy list for same reference -> tea_varieties_copy = tea_varieties --> print(tea_varieties_copy) --> ["Black", "Green", "Masala", "White"] --> it copied reference then you any one value of memory it change for bot variable
- 15 Copy list for copy new value in memory -> tea_varieties_copy = tea_varieties.copy() --> print(tea_varieties_copy) --> ["Black", "Green", "Masala", "White"]

- 16 List for for loops also known as List comprehension -> squared_nums = [x**2 for x in range(10)] --> [0,1,4,9,16,25,36,49,64,81] --> x take value from for loop and range make the how many time loop will run