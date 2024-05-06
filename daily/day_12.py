class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        if avg >= 90:
            grade = "O"
        elif avg >= 80:
            grade = "E"
        elif avg >= 70:
            grade = "A"
        elif avg >= 55:
            grade = "P"
        elif avg >= 40:
            grade = "D"
        else:
            grade = "T"
        return grade


# line = input().split()
line = ["Joe", "Smith", "12345"]
fname = line[0]
lname = line[1]
idnum = line[2]
# numScores = int(input())  # not needed for Python
scr_inpt = "50 20 13 45"
scores = list(map(int, scr_inpt.split()))
s = Student(fname, lname, idnum, scores)
s.printPerson()
print("Grade:", s.calculate())
