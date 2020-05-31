lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    if start >= len(iterable):
        start = 0
    while start<len(iterable):
        yield start,iterable[start]
        start+=1



for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
