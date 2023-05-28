# Create a mad lib story

# Take user input for each of these variables, and be sure to give a prompt!
mythicalAnimal = input("Enter the name of a mythical animal: ")
characterName = input("Enter the name of character: ")
age = input("Enter your age: ")
secondCharacterName = input("Enter second character name: ")
secondCharacterJob = input("Enter second character job: ")
place1 = input("Enter first place: ")
place2 = input("Enter second place: ")
pluralNoun1 = input("Enter first plural noun: ")
pluralNoun2 = input("Enter second plural noun: ")
action = input("Enter action: ")
adj1 = input("Enter first adjective: ")
adj2 = input("Enter second adjective: ")
pastTenseVerb1 = input("Enter first past tense verb: ")
pastTenseVerb2 = input("Enter second past tense verb: ")
char = input("Enter char: ")

# Create the story, replace all of the +'s with f strings to clean up the
# code.
story = f"Once upon {char} time, there was {char} {adj1} \
        + {mythicalAnimal} +  named  + \
        characterName + .  + characterName + was  + char + + str(age)\
        +  years old and lived by the  + \
        place1 + . He  + pastTenseVerb1 + + pluralNoun1 +  and  + \
        pluralNoun2 + . People thought  + \
        characterName +  was too  + adj1 + . The people sent  + \
        secondCharacterName + , the village's  \
        + secondCharacterJob + , to  + action +  the  + mythicalAnimal + \
        .  + characterName +  thought that  \
        + pastTenseVerb2 +  + adj2 + , so he left the  + place1 + . Now he " \
        f"lives in the  + place2 \
        +  and eats the  + pluralNoun1 +  and  + pluralNoun2 +  there  \
                                                                   instead."
print(story)
