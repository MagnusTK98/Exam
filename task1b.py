# Flow 29
# Task 1b

def calculate_bonus(data):
    if data['performanceRating'] == 'Outstanding':
        bonus = 1000
    elif data['performanceRating'] == 'Strong Performer':
        bonus = 800
    elif data['performanceRating'] == 'Satisfactory':
        bonus = 500
    elif data['performanceRating'] == 'Poor':
        bonus = 200
    else:
        print('Performance Rating does not match')
    
    if data['yearsOfService'] > 5:
        bonus *= 2
    elif data['yearsOfService'] >= 2 and data['yearsOfService'] <= 5:
        bonus *= 1.5
    elif data['yearsOfService'] < 2:
        bonus *= 1
    print(bonus)

data = {
    'performanceRating': 'Outstanding',
    'yearsOfService': 3
}
calculate_bonus(data)