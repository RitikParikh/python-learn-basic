### Tuples
 - List diff with tuples -> List is mutable or Tupels are inmutable
    Ex: tea_types = ("Black","Green","Oolong")
    1. First position  = tea_types[0] --> Black 
    2. last position  = tea_types[-1] --> Oolong 
    3. slice position  = tea_types[1:] --> "Green","Oolong" 
    4. Change value  = tea_types["Black"] = "Lemon" --> Error
    5. length  = len(tea_types)--> 3
    6. more_tea  = len("Herbal", "Earl Gray")--> all_tea = more_tea + tea_types --> ("Herbal", "Earl Gray", "Black","Green","Oolong")
    7. Condation -->
    if "Green" in all_types:
        print("I have green tea")

    8. more_tea = ("Herbal","Earl Gray","Herbal") --> more_tea.count("Herbal") --> 2
    9. tupals to set --> (black, green , oolong) = tea_types --> value number count need to same
        black --> "Black"