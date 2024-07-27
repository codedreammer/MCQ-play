questions = [
    ["What is the capital of India?"," Uttrakhand", " Kerla", " Delhi", " Bihar", 3],
    ["What is the full form of HTML?"," Hyp Markup Language", " Hypertext Markup Language", " Hypertext Mark Language", " Hypertext Markup Program", 2],
    ["How is your life after choosing ENGINEERING!?"," Fucked up", " All of these", " Dont't you dare to ask again", " don't know", 2],
    ["What is Happiness as an Engineer?","Project completed", " Date with Crush", "Promotion", " Work from Home", 1 ],
]

levels=[1000,20000,50000,1000000]

for i in range(0, len(questions)):
    question = questions[i]
    print(f"question  for Rs. {levels[i]}")
    print(f"a.{question[1]}             b.{question[2]}  ")
    print(f"c. {question[3]}            d.{question[4]}  ")

reply = int(input("Enter your answer (1-4) "))
if(reply == question[-1]):
    print(f"correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
        money = 1000
    elif(i == 9):
        money = 50000
    elif(i == 14):
        money = 100000
else:
    print("worng answer!")
    break
    
     