from sys import argv

questions = {
    0 :"Which is the national birld of INDIA:\n",
    1 :"Who received Karnataka Ratna in 2022:\n",
    2 :"Who is the PM of india (2022):\n",
    3 :"Where is the 2nd largest sitting Statue Located:\n",
    4 :"Who is the Founder Of RNS:\n"
}
answers = {
    0 : ["peacock", 'pea-cock'],
    1 : ['punith', "punith rajkumar"],
    2 : ['narendra modi', 'modi'],
    3 : ['murdeshwar', 'murdeshwara'],
    4 : ['r.n.shetty', 'r n shetty', 'rn shetty', 'rama nagappa shetty']
}
def quiz_Func(name):
    count = 0
    print(f"Hello {name} lets check your Knowledge")
    for i in range(len(questions)):
        # print(i)
        user_answer = input((questions[i]))
        if user_answer.lower().strip() in answers[i]:
            print("Congrulations,Correct answer!!")
            count += 1
        else:
            print("Sorry u got it Wrong!!")
            count -= 0.5 
    return count



print(f"You have scored a total of {quiz_Func(argv[-1])} Points out of {len(questions)}")

