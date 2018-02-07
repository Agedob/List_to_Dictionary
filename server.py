name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def ltd(arr1,arr2):
    new_dict = {}
    for abc in range(len(arr1)):
        new_dict[arr1[abc]] = arr2[abc]
    return new_dict
print ltd(name,favorite_animal)