# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/23 21:30
'项目：生成随机的测试试卷'
'''
进行美国各州的首府进行一个小测验，你希望随机调整问题的次序，这样每份试卷都是独一无二的。
程序任务：
• 创建 35 份不同的测验试卷。
• 为每份试卷创建 50 个多重选择题，次序随机。
• 为每个问题提供一个正确答案和 3 个随机的错误答案，次序随机。
• 将测验试卷写到 35 个文本文件中。
• 将答案写到 35 个文本文件中。
程序实现：
• 将州和它们的首府保存在一个字典中。
• 针对测验文本文件和答案文本文件，调用 open()、write()和 close()。 
• 利用 random.shuffle()随机调整问题和多重选项的次序。
'''
import random,os

# 测验的州府数据，键是州，值是州首府
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau',
            'Arizona': 'Phoenix','Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee','Georgia': 'Atlanta',
            'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois':'Springfield', 'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines', 'Kansas':'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
            'Maine':'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan':'Lansing',
            'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri':'Jefferson City', 'Montana': 'Helena',
            'Nebraska': 'Lincoln', 'Nevada':'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'NewMexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh','North Dakota': 'Bismarck',
            'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence','South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee':'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont':'Montpelier', 'Virginia': 'Richmond',
            'Washington': 'Olympia', 'WestVirginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

os.makedirs('question',exist_ok=True)
os.makedirs('answer',exist_ok=True)
# 生成35个测验文件
for quiz_num in range(35):
    # TODO:生成测验和答案的文件
    quiz_file = open(os.path.join('question','capitalsquiz{}.txt'.format(quiz_num+1)),'w')
    answer_file = open(os.path.join('answer','capitalsquiz_answers{}.txt'.\
                       format(quiz_num +1)),'w')

    # TODO:写下测验文件的标题
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' '*20) + \
                    'State Capitals Quiz(From {})'.format(quiz_num+1))
    quiz_file.write('\n\n')

    # TODO:随机排列各州
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO:遍历50个州，对每个州提出问题
    for questionNum in range(50):
        # 获取正确和错误答案
        correctAnswer = capitals[states[questionNum]]
        capitalsAnswer = list(capitals.values())
        del capitalsAnswer[capitalsAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(capitalsAnswer,3)
        answerOptions = wrongAnswer + [correctAnswer]
        random.shuffle(answerOptions)

        # TODO:将问题和选项写入测试文件
        quiz_file.write('{}.What is the capitals of {}\n'.\
                        format(questionNum+1,states[questionNum]))
        for i in range(4):
            quiz_file.write(' {}. {}\n'.\
                            format('ABCD'[i],answerOptions[i]))
        quiz_file.write('\n')

        # TODO: 将答案写入文件
        answer_file.write(' {}. {}\n'.format(questionNum+1,
                    'ABCD'[answerOptions.index(correctAnswer)]))
    quiz_file.close()
    answer_file.close()