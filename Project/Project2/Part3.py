
# Function that reads the data of txt file and change them to a list
def order_list(file):
    f = open(file)
    result = f.readlines()
    size = len(result)
    for i in range(size):
        if result[i][-1:] == "\n":
            result[i] = result[i][:-1]
    f.close()
    return result
preorder_list = order_list("data-B.txt")
postorder_list = order_list("data-A.txt")

i = 0  # index for preorder_list
j = len(postorder_list)-1  # index for postorder_list
t = 0

def AnimalGuessing(i, j, preorder_list, postorder_list):
    if postorder_list[j][-1] != "?":
        print("My guess is " + postorder_list[j] + " Am I right? [Y or N or U]")
        answer = input()
        if answer == "Y":
            print("The answer is correct")
        elif answer == "N":
            print("I give up. What are you?")
            answer_animal = input()
            print("Please type yes/no question that will distinguish a " + answer_animal + " from a " + postorder_list[j])
            answer_question = input("Your question :  ")
            print("As a " + answer_animal + ", " + answer_question + " Please answer [Y or N or U]")
            answer6 = input()
            if answer6 == "Y":
                preorder_list.insert(i, answer_question)
                preorder_list.insert(i+1, answer_animal)
                postorder_list.insert(j, answer_animal)
                postorder_list.insert(j + 1, answer_question)
                f = open("data-A.txt", 'w')
                for m in range(len(postorder_list)):
                    f.write(postorder_list[m] + "\n")
                f.close()
                f = open("data-B.txt", 'w')
                for m in range(len(preorder_list)):
                    f.write(preorder_list[m] + "\n")
                f.close()
            if answer6 == "N":
                preorder_list.insert(i, answer_question)
                preorder_list.insert(i + 2, answer_animal)
                postorder_list.insert(j + 1, answer_question)
                postorder_list.insert(j + 2, answer_animal)
                f = open("data-A.txt", 'w')
                for m in range(len(postorder_list)):
                    f.write(postorder_list[m] + "\n")
                f.close()
                f = open("data-B.txt", 'w')
                for m in range(len(preorder_list)):
                    f.write(preorder_list[m] + "\n")
                f.close()
        elif answer == "U":
            if treelist[-1] == "R":
                j += 1
                for k in range(len(preorder_list)):
                    if postorder_list[j] == preorder_list[k]:
                        i = k
                        treelist.pop()
                        treelist.append("U")
            elif treelist[-1] == "L":
                i -= 1
                for k in range(len(preorder_list)):
                    if preorder_list[i] == postorder_list[k]:
                        j = k
                        treelist.pop()
                        treelist.append("U")
            AnimalGuessing(i, j, preorder_list, postorder_list)
    else:
        if len(treelist) > 0 and treelist[-1] == "U":
            print("Is the question " + preorder_list[i]  +" where you made a mistake? [Y or N or U]")
            answer = input()
            if answer == "U":
                treelist.pop()
                AnimalGuessing(i, j, preorder_list, postorder_list)
            elif answer == "Y":
                if treelist[-2] == "R":
                    i += 1
                    for k in range(len(preorder_list)):
                        if postorder_list[k] == preorder_list[i]:
                            j = k
                if treelist[-2] == "L":
                    j -= 1
                    for k in range(len(preorder_list)):
                        if postorder_list[j] == preorder_list[k]:
                            i = k
                treelist.pop()
                AnimalGuessing(i, j, preorder_list, postorder_list)
            elif answer == "N":
                if treelist[-2] == "R":
                    j += 1
                    for k in range(len(preorder_list)):
                        if postorder_list[j] == preorder_list[k]:
                            i = k
                if treelist[-2] == "L":
                    i -= 1
                    for k in range(len(preorder_list)):
                        if postorder_list[k] == preorder_list[i]:
                            j = k
                AnimalGuessing(i, j, preorder_list, postorder_list)
        else:
            print(preorder_list[i] + "[Y or N or U]")
            answer = input()
            if answer == "Y":
                treelist.append("L")
                i += 1
                for k in range(len(preorder_list)):
                    if preorder_list[i] == postorder_list[k]:
                        j = k
                AnimalGuessing(i, j, preorder_list, postorder_list)
            if answer == "N":
                treelist.append("R")
                j -= 1
                for k in range(len(preorder_list)):
                    if postorder_list[j] == preorder_list[k]:
                        i = k
                AnimalGuessing(i, j, preorder_list, postorder_list)
            if answer == "U":
                if treelist[-1] == "U":
                    if treelist[-2] == "R":
                        j += 1
                        for k in range(len(preorder_list)):
                            if postorder_list[j] == preorder_list[k]:
                                i = k
                    elif treelist[-2] == "L":
                        i -= 1
                        for k in range(len(preorder_list)):
                            if preorder_list[i] == postorder_list[k]:
                                j = k
                    treelist.append("U")
                elif treelist[-1] == "R":
                    j += 1
                    for k in range(len(preorder_list)):
                        if postorder_list[j] == preorder_list[k]:
                            i = k
                    treelist.append("U")
                elif treelist[-1] == "L":
                    i -= 1
                    for k in range(len(preorder_list)):
                        if preorder_list[i] == postorder_list[k]:
                            j = k
                    treelist.append("U")
                AnimalGuessing(i, j, preorder_list, postorder_list)
while True:
    treelist = []
    i = 0
    j = len(postorder_list) - 1
    format = input("Which data format do you want? [A or B]")
    AnimalGuessing(i, j, preorder_list, postorder_list)
    print("Shall we play again? [Y or N]")
    play = input()
    if play == "N":
        break