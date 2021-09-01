import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany',
            'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


def QuizMaker(num):
    for quiz_num in range(num):
        quiz_header = f"USA states capitals Quiz - version nr: {quiz_num + 1} \nName:\nDate:\n\n"

        with open(f"C:\\temp\CapitalQuiz_{quiz_num + 1}.txt", "w") as newFile:
            answerKeyFile = open(f'C:\\temp\Quiz_answers_{quiz_num + 1}.txt', 'w')
            states = list(capitals.keys())
            random.shuffle(states)
            newFile.write(quiz_header)
            for question_num in range(50):
                question = f"{question_num + 1}. What is the capital of {states[question_num]}?\n"
                correct_answer = capitals[states[question_num]]
                wrongAnswers = list(capitals.values())
                del wrongAnswers[wrongAnswers.index(correct_answer)]
                wrongAnswers = random.sample(wrongAnswers, 3)
                answerOptions = wrongAnswers + [correct_answer]
                random.shuffle(answerOptions)
                newFile.write(question)
                answerKeyFile.write(f"{question_num + 1}: {'ABCD'[answerOptions.index(correct_answer)]}\n")
                for nr in range(4):
                    x = "ABCD"
                    newFile.write(f"{x[nr]}) {answerOptions[nr]}\n")

                newFile.write("\n")


QuizMaker(35)
