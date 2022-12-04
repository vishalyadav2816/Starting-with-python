#dictionaruy - usedto store data value in key:value pairs
"""
myDictionary = {
    "name" : "vishal",
    "age" : 17, 
    "percent" : 65.81
}
age = myDictionary.get("age")
keys = myDictionary.values()
items = myDictionary.items()
print(items)

"""
"""
#ordered
#changeable
#does not allow duplicate values 
print(myDictionary)
myDictionary.popitem()
print(myDictionary)



#merge two dictionaries in one 
dict1 = {"one":1, "two":2, "three":3}
dict2 = {"four":4, "five":5, "six":6}

dict1.update(dict2)
print(dict1)

"""


dict1 = {
    "class":{
        "student":{
            "name":"xyz",
            "marks":{
                "python":100,
                "web":90
            }
        }
    }
}

print(dict1['class']['student']['marks']['web'])