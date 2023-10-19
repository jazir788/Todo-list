import json
CorrectAnswer = 0
InCorrectAnswer = 0
with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["questions"])
    for index, alternatives in enumerate(question["alternatives"]):
        print(index+ 1, "-", alternatives)
    user_choice = int(input("Enter your answer in number format: "))
    question["user_choice"] = user_choice
    if user_choice == question["correct_answer"]:
        CorrectAnswer += 1
        print("Correct")
    else:
        InCorrectAnswer += 1
        print("Incorrect, Your answer is",question["user_choice"], "The Correct answer is ", question["correct_answer"])
print("Number of Correct Answers: ", CorrectAnswer)
print("Number of Incorrect Answers: ", InCorrectAnswer)


