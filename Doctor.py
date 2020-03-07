import random
history = []
hedges = ("Please tell me more.", 
"Many of my patients tell me the same thing.",
"Please continue.")

qualifiers = ("Why do you say that ",
"You seem to think that ", 
"Can you explain why ")

replacements = {"I": "you", "me":"you", "my":"your", 
"we":"you", "us":"you", "mine":"yours"}

class Doctor:
    def __init__(self):
        pass

    def greeting(self):
        return "Good morning, I hope you are well today.\nWhat can I do for you?"

    def farewell(self):
        return "Have a nice day!"

    def reply(self,sentence): #builds and returns a reply to the sentence.
        probability = random.randint(1,5)
        if probability in (1,2):
            return random.choice(hedges)
        elif probability == 3 and len(history)>3: #return to an earlier topic
            return "Earlier you said that " + \
            changePerson(random.choice(history))
        else:
            history.append(sentence)#adds current sentence to history
            return random.choice(qualifiers) + changePerson(sentence)

def changePerson(sentence): #replaces first person pronouns with second person pronouns
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)

def main(): #handles the interaction between patient and doctor
    doc = Doctor()
    print(doc.greeting())
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print(doc.farewell())
            input("Press Enter to quit.")
            break
        print(doc.reply(sentence))
    

#The entry point of program execution
if __name__ == "__main__" : 
    main()



    