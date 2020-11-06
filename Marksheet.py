class MarkSheet:
    def __init__(self, name, department, SeatNo):
        self.name = name
        self.department = department
        self.seatNo = SeatNo

    def Show(self):
        print("\t\t==========MARK-SHEET==========")
        print("\t==========UNIVERSITY OF KARACHI==========")
        print("FULL NAME :", self.name)
        print("DEPARTMENT NAME :", self.department)
        print("SEAT # : ", self.seatNo)

    @staticmethod
    def gpa(totalMarks):
        if totalMarks >= 90:
            return 4.0
        elif 85 <= totalMarks <= 89:
            return 4.0
        elif 80 <= totalMarks <= 84:
            return 3.8
        elif 75 <= totalMarks <= 79:
            return 3.4
        elif 71 <= totalMarks <= 74:
            return 3.0
        elif 68 <= totalMarks <= 70:
            return 2.8
        elif 64 <= totalMarks <= 67:
            return 2.4
        elif 61 <= totalMarks <= 63:
            return 2.0
        elif 57 <= totalMarks <= 60:
            return 1.8
        elif 53 <= totalMarks <= 56:
            return 1.4
        elif 51 <= totalMarks <= 51:
            return 1.0
        else:
            return 0.0

    @staticmethod
    def gpaForm(gpa):
        if gpa == 4.0:
            return "A"
        elif gpa >= 3.8:
            return "A-"
        elif gpa >= 3.4:
            return "B+"
        elif gpa >= 3.0:
            return "B"
        elif gpa >= 2.8:
            return "B-"
        elif gpa >= 2.4:
            return "C+"
        elif gpa >= 2.0:
            return "C"
        elif gpa >= 1.8:
            return "C-"
        elif gpa >= 1.4:
            return "D+"
        elif gpa >= 1.0:
            return "D-"
        else:
            return "FAIL"


import time


def main():
    storeGpa = 0.0
    print("\t===========Welcome To University Of Karachi=============")
    print("We need some details about you..")
    print("Loading Please Wait......")
    time.sleep(5)
    name = str(input("Enter Your Name ==> ")).upper()
    nameOfDepartment = str(input("Enter Your Department Name ==> ")).upper()
    seatNum = str(input("Enter Your Proper Seat Number ==> ")).upper()
    omark = MarkSheet(name, nameOfDepartment, seatNum)
    totalSub = int(input("Enter Total Subjects ==> "))
    count = 1
    try:
        file = open("StudentInfo.txt", "w+")
    except IOError:
        print("Oops! Something went wrong! try again.")
        exit()
    while count <= totalSub:
        subjectName = str(input(f"Enter Subject{count} Name ==> ").capitalize())
        subjectMarks = int(input(f"Enter {subjectName} marks ==> "))
        file.writelines(subjectName + " " + str(subjectMarks) + "\n")
        storeGpa += omark.gpa(subjectMarks)
        count += 1
    file.close()
    storeGpa /= totalSub
    gpaResult = omark.gpaForm(storeGpa)
    print("PRESS Y to print Mark-Sheet")
    try:
        response = str(input("Enter ==> ")).upper()
        if response == "Y":
            omark.Show()
            print("\t==============================")
            try:
                fileRead = open("StudentInfo.txt", "r")
                print(fileRead.read())
            except IOError:
                print("Oops! Something went wrong! try again.")
            finally:
                fileRead.close()
            print("Total GPA : " + gpaResult)
            print("\t\t\t\t\tBy: Hazique Iqbal")
        else:
            print("Invalid Command!")
    except TypeError:
        print("Oops! Something went wrong. You can try later.")
        exit()
    finally:
        file.close()


main()
