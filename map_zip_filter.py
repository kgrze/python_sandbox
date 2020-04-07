# Examples of map, sort, zip, filter functions

# Examples of map()
print ("\nmap():")
print( list(map(lambda *a: a, range(3)) ) ) #1-element list
print( list(map(lambda *a: a, range(3), "abc") ) ) #2-element list
print( list(map(lambda *a: a, range(3), "abcd", "12") ) ) #3-element list with shortest selected

# Sorting
print ("\n\nSorting:")
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
# Sort students by age
print( sorted(student_objects, key=lambda student: student.age) )   # sort by age

students = [
    dict(id=0, credits=dict(math=9, physics=6, history=7)),
    dict(id=1, credits=dict(math=6, physics=7, latin=10)),
    dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
    dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]

def decorate(student):
    # create a 2-tuple (sum of credits, student) from student dict
    return (sum(student['credits'].values()), student)

def undecorate(decorated_student):
    # discard sum of credits, return original student dict
    return decorated_student[1]

# Sort students by sum of their credits
students = sorted(map(decorate, students), reverse=True)
print("\n")
print(students)
students = list(map(undecorate, students))
print("\n")
print(students)

# Zip
print ("\nzip():")
grades = [18, 23, 30, 27]
avgs = [22, 21, 29, 24]
print( list(zip(avgs, grades)) )
print()
print( list(map(lambda *a: a, avgs, grades)) )  # equivalent to zip

print("\n")
a = [5, 9, 2, 4, 7]
b = [3, 7, 1, 9, 2]
c = [6, 8, 0, 5, 3]

maxs = list(map(lambda n: max(*n), zip(a, b, c)))
print(maxs)

# filter()
print ("\nfilter():")
test = [2, 5, 8, 0, 0, 1, 0]
print(test)
print(list(filter(None, test)))
print(list(filter(lambda x: x, test)))  # equivalent to previous one
print(list(filter(lambda x: x > 4, test)))  # keep only items > 4