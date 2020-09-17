def start():
    print("Welcom in Secrect Language Translator")

start()


def virag():
    word = str(input("Please give me a sentence:"))
    word2 = word.replace("a", "ava")
    word3 = word2.replace("e", "eve")
    word4 = word3.replace("i", "ivi")
    word5 = word4.replace("o", "ovo")
    word6 = word5.replace("u", "uvu")
    print(word6)


def fa():
    word = str(input("Please give me a sentence:"))
    word2 = word.replace("a", "afa")
    word3 = word2.replace("e", "efe")
    word4 = word3.replace("i", "ifi")
    word5 = word4.replace("o", "ofo")
    word6 = word5.replace("u", "ufu")
    print(word6)


while True:
    answer = str(input("Please choose from the following (If you want to exit the program type exit.)\nVirag or Fa: "))
    if answer.lower() in ["virag"]:
            virag();
            continue
    elif answer.lower() in ["fa"]:
            fa();
            continue
    elif answer.lower() in ["exit"]:
        break
    else:
            print("Error:Please type virag or fa.")
            continue


