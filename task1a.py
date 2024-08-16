# Flow 29
# Task 1a

def evaluate_performance(data):
    evaluation=[]
    if data['salesTarget'] > 120:
        salesTarget = 4
    elif data['salesTarget'] >= 100 and data['salesTarget'] <= 120:
        salesTarget = 3
    elif data['salesTarget'] >= 80 and data['salesTarget'] < 100:
        salesTarget = 2
    else:
        salesTarget = 1
    evaluation.append(salesTarget)
    if data['customerSatisfaction'] == 10:
        customerSatisfaction = 4
    elif data['customerSatisfaction'] >= 8 and data['customerSatisfaction'] <= 9:
        customerSatisfaction = 3
    elif data['customerSatisfaction'] >= 6 and data['customerSatisfaction'] <= 7:
        customerSatisfaction = 2
    else:
        customerSatisfaction = 1
    evaluation.append(customerSatisfaction)
    if data['attendance'] >= 28:
        attendance = 4
    elif data['attendance'] >= 25 and data['attendance'] <= 27:
        attendance = 3
    elif data['attendance'] >= 20 and data['attendance'] <= 24:
        attendance = 2
    else:
        attendance = 1
    evaluation.append(attendance)
    if data['peerFeedback'] >= 9 and data['peerFeedback'] <= 10 :
        peerFeedback = 4
    elif data['peerFeedback'] >= 7 and data['peerFeedback'] <= 8:
        peerFeedback = 3
    elif data['peerFeedback'] >= 4 and data['peerFeedback'] <= 6:
        peerFeedback = 2
    else:
        peerFeedback = 1
    evaluation.append(peerFeedback)
    print(evaluation)
    Threes = evaluation.count(3)
    Fours = evaluation.count(4)
    Total = Threes + Fours
    print(Total)
    if evaluation.count(4) == 4:
        print('Outstanding')
    elif evaluation.count(1) >= 2:
        print('Needs Improvement')
    elif Total == 3:
        print('Strong Performer')
    else:
        print('Satisfactory')
    


data = {
    'salesTarget': 8,
    'customerSatisfaction': 7,
    'attendance': 25,
    'peerFeedback': 10
}

evaluate_performance(data)