import random

Hand = []
Nums = ['1','2','3','4','5','6','7','8','9']
Ops = ['+','-','*','/','|']

def is_Num(n):
    if n in Nums:
        return True
    return False

def is_Op(o):
    if o in Ops:
        return True
    return False

def in_Hand(x):
    if x in Hand:
        return True
    else:
        return False

def is_valid():
    length = len(expList)
    #print("length:", length)
    concat_count = 0
    if length > 7:
        print("expression length exceeded")
        return False
    elif not is_Num(expList[0]) or not is_Num(expList[length-1]):
        print("invalid expression format")
        return False
    for i in range(length):
        card = expList[i]
        if i%2 == 0:
            if not is_Num(card):
                print("invalid expression format")
                return False
            else:
                if in_Hand(int(card)):
                    Hand.remove(int(card))
                    #print(card,"removed")
                else:
                    print("you used a number not in hand")
                    return False
        if i%2 == 1 and not is_Op(card):
            print("invalid expression format")
            return False
        if card == '|':
            concat_count+=1
    if concat_count>1:
        print("concatenation limit exceeded")
        return False
    return True

print("There will be five questions! Remember that concatenation operator is '|' and you can use it at most once per expression")
total = 0

for turn in range(5):
    while len(Hand) < 5:
        Hand.append(random.randint(1,9))
    print("You have the following cards in hand:", Hand)

    cap = random.randint(66,200)
    print("The cap for question", turn+1,"is:",cap)


    exp = input("Enter your expression:")
    expList = list(exp)
    #print(expList)

  
    if is_valid():
        expList = [c for c in expList if c!= '|']
        #print(expList)
        answer = int(eval("".join(expList)))
        print("your answer is:", answer)
        if answer > cap:
            print("answer exceeded cap")
            answer = 0
        else:
            print("answer is under cap")
            print("your answer will hold!")
    else:
        print("Your expression was invalid!")
        print("Your will not get any points this question")
        answer = 0

    total += answer
    print("your total points are:", total)
    #print(Hand)
