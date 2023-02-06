groupmates = [
    {
        "name": "Диана",
        "surname": "Крюкова",
        "exams": ["ВвИТ", "АиГ", "Философия"],
        "marks": [4, 4, 5]
    },
    {
        "name": "Михаил",
        "surname": "Романчук",
        "exams": ["АиГ", "Философия", "ВвИТ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Павел",
        "surname": "Охримчук",
        "exams": ["Философия", "АиГ", "ВвИТ"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Александр",
        "surname": "Плешаков",
        "exams": ["АиГ", "Философия", "ВвИТ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Алан",
        "surname": "Шарифуллин",
        "exams": ["Философия", "ВвИТ", "АиГ"],
        "marks": [4, 5, 5]
    }
]

from statistics import mean

def filter_students(students, mark):
    for student in students:
        mean_mark = mean(student['marks'])
        if mark <= mean_mark:
            print(student['name'], student['surname'], mean_mark)

filter_students(groupmates, float(input()))