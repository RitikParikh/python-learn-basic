###
- String is multiple variants to write --> ' ', " ", """ """
- Find First Char --> chai = "Masala Chai"--> first_char = chai[0]--> print(first_char)
- Slice String 
   - 1. slice_chai = chai[0:6] --> print(slice_chai) --> Masala
   - 2. num_list = "0123456789"
      - num_list[:] --> "0123456789"
      - num_list[3:] --> "3456789"
      - num_list[:7] --> "0123456"
      - num_list[0:7:3] --> "0246" // Hopping method

- print 
   - 1 lower string -> print(chai.lower()) --> "masala chai"
   - 2 upper string -> print(chai.upper()) --> "MASALA CHAI"
   - 3 Strip(Trim) string -> chai = "   Masala Chai " --> print(chai.strip())
   - 4 Replace -> chai = "Lemon tea" --> print(chai.replace("Lemon", "Ginger"))
   - 5 string to list -> chai = "Lemon, Ginger, Masala, Mint" --> chai.split(", ") -> ['Lemon', 'Ginger', 'Masala', "Mint"]
   - 6 Find string -> chai = "Masala chai" -> print(chai.find("chai")) -> 7 //found strin from 7 position
   - 7 Find string -> chai = "Masala chai" -> print(chai.find("Chai")) -> -1 // not found provided string
   - 8 Find string count -> chai = "Masala chai chai chai" -> print(chai.count("Chai")) -> 3
   - 9 variable inputting in string -> chai_type = "Masala" quantity = 2 order= "I ordered {} cups of {} chai" --> print(order.format(quantity, chai_type)) --> I ordered 2 cups of Masala chai
   - 10 List to string -> chai_variety = ["Lemon", "Masala", "Ginger"] -> print(", ".join(chai_variety)))
   - 11 Length find of string -> chai = "Masala Chai" --> print(len(chai))
   - 12 String on for -> 
      for letter in chai:
        print(letter)
   - 13 -> chai = "He said, \"Masala chai is awesome\"" -> He said, "Masala chai is awesome"
   - 14 Use raw method for raw string -> chai = r"Masala\nChai" -> "Masala\nChai" -> if not this time then it print to Masala next line Chai
   - 15 Containing question -> chai = "Masala Chai" --> Print("Masala" in chai) --> True