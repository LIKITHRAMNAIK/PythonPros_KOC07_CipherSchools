import random

ques_list = ["A slug's blood is green.",
             "The loudest animal is the African Elephant.",
             "Approximately one quarter of human bones are in the feet.",
             "The total surface area of a human lungs is the size of a football pitch.",
             "Australia is wider than the moon.",
             "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
             "It is illegal to pee in the Ocean in Portugal.",
             "You can lead a cow down stairs but not up stairs.",
             "Google was originally called 'Backrub'.",
             "Buzz Aldrin's mother's maiden name was 'Moon'.",
             "No piece of square dry paper can be folded in half more than 7 times.",
             "A few ounces of chocolate can to kill a small dog."]
ans_list = ["true", "false", "true", "true", "true", "false", "true", "false", "true", "true", "false", "true"]

ques_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
random.shuffle(ques_seq)

score = 0
ques_no = 1

for i in ques_seq[:5]:
    print('Q'+str(ques_no)+'. '+ques_list[i])
    response = input("True/False\n:- ")
    ques_no += 1
    if response.lower() == ans_list[i]:
        print('Congrats! You got it correct\n')
        score += 1
    else:
        print('OOPS! Your answer is wrong\n')
print("Your Overall score is", score)
print("Thank You!!")
