### Dictionary
 - Initialize Dictionary using --> Dict keyword or , {}
 - Example -> chai_types = { "Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

- 1 print(chai_types)
- 2. Access using key --> print(chai_types['Masala']) --> "Spicy"
- 3. Access using get method --> print(chai_types.get('Ginger')) --> "Zesty"
- 4. If key not in the Dict using get method--> print(chai_types.get('Gingery')) --> None
- 5. If key not in the Dict direct --> print(chai_types['Gingery']) --> keyError
- 5. change value of key --> chai_types['Green'] = 'Fresh' --> print(chai_types) --> { "Masala": "Spicy", "Ginger": "Zesty", "Green": "Fresh"}
- 6. loop on it --> get keys --> ["Masala", "Ginger","Green"]
for chai in chai_type:
    print(chai)

- 8. loop on it --> get values --> ["Spicy", "Zesty","Mild"]
for chai in chai_type:
    print(chai_types[chai])

- 9. loop on it --> get key/index and values direct -->
for key, value in chai_type.items():
    print(key, value)

- 10. If condation --> 
if "Masala" in chai_types:
    print("I have this tea")

- 11. get dict length --> print(len(chai_types))
- 12. chai_types["Earl Grey"] = 'Citrus' --> print(chai_types) --> { "Masala": "Spicy", "Ginger": "Zesty", "Green": "Fresh", "Earl Grey": "Citrus"}
- 13. remove key value using key --> chai_types.pop("Ginger") --> print(chai_types) --> { "Masala": "Spicy", "Green": "Fresh", "Earl Grey": "Citrus"}
- 14. remove key last key --> chai_types.popitem() --> print(chai_types) --> { "Masala": "Spicy", "Green": "Fresh"}
- 15. remove memory reference with key--> del chai_types["Green"] --> print(chai_types) --> { "Masala": "Spicy"}
- 16. Copy Dict --> chai_types_copy = chai_types.copy[chai_types] --> print(chai_types_copy) --> { "Masala": "Spicy"}
- 17. Nested Dict -->
tea_shop = {
    "chai": { "Masala": "Spicy", "Ginger": "Zesty", "Green": "Fresh" },
    "Tea": { "Green": "Mild", "Black": "Strong"}
}
print(tea_shop) --> {"chai": { "Masala": "Spicy", "Ginger": "Zesty", "Green": "Fresh" }, "Tea": { "Green": "Mild", "Black": "Strong"} }

-18. fetch nested value --> print(tea_shop["chai"]["Ginger"]) --> "Zesty"
- 19. for loop for range in dict --> print({x:x**2 for x in range(6)}) --> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
-20. make empty the dict --> chai_types.clear()

-21. keys set --> keys = ["Masala", "Ginger", "Lemon"] --> default_value = "Delicious"
    new_dict = dict.fromkeys(keys, default_value) --> new_dict --> {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}

- 22 two dict merge -->  new_dict = dict.fromkeys(keys, keys) --> {'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}