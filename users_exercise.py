users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [{"name": "monty", "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users["Jonathan"]["twitter"])

# 2. Get Erik's hometown
print(users["Erik"]["home_town"])

# 3. Get the list of Erik's lottery numbers
print(users["Erik"]["lottery_numbers"])

# 4. Get the species of Avril's pet Monty
print(users["Avril"]["pets"][0]["species"]) #there is a better way to do this!!

# 5. Get the smallest of Erik's lottery numbers
print(min(users["Erik"]["lottery_numbers"])) #might be able to do this with an if statement as well

# 6. Return an list of Avril's lottery numbers that are even
for each_of_avrils_number in users["Avril"]["lottery_numbers"]:
  if each_of_avrils_number % 2 == 0:
    print(each_of_avrils_number)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"])

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["hometown"] = "Edinburgh"
print(users["Erik"]["hometown"])

# 9. Add a pet dog to Erik called "fluffy" --> adding an item to a list; the item happens to be a dictionary
fluffy_dog = {
  "name" : "fluffy",
  "species" : "dog"
}
users["Erik"]["pets"].append(fluffy_dog)
print(users["Erik"]["pets"])

# 10. Add another person to the users dictionary --> adding an item to a dictionary
users["Frasier Crane"] = {
    "twitter" : "frasier.crane",
    "lottery_numbers" : [8, 15, 26, 32, 48, 125, 376],
    "home_town" : "Seattle",
    "pets" :[{
      "name" : "Eddie",
      "species" : "dog"
    },
    {
      "name" : "Boots",
      "species" : "cat"
    },
    {
      "name" : "Socks",
      "species" : "cat"
    }
    ]
  }
print(users)