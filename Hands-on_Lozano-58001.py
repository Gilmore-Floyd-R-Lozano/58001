class Person():
    def __init__(self, std1, std2, std3, pre, mid, fin):
        self._std1 = std1
        self._std2 = std2
        self._std3 = std3
        self._pre = pre
        self._mid = mid
        self._fin = fin

    def Grade(self):
        Average = (self._pre + self._mid + self._fin) / 3
        print("The average grade of", self._std1 + self._std2 + self._std3, "is", Average, "\n")


student1 = Person(input("Enter Name of Student 1: "), "", "", float(input("Enter Prelim Grades: ")),
                  float(input("Enter Midterm Grades: ")), float(input("Enter Finals Grades: ")))
student1.Grade()
student2 = Person("", input("Enter Name of Student 2: "), "", float(input("Enter Prelim Grades: ")),
                  float(input("Enter Midterm Grades: ")), float(input("Enter Finals Grades: ")))
student2.Grade()
student3 = Person("", "", input("Enter Name of Student 3: "), float(input("Enter Prelim Grades: ")),
                  float(input("Enter Midterm Grades: ")), float(input("Enter Finals Grades: ")))
student3.Grade()


