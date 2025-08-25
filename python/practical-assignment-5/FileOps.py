# This is a sample Python script.
import math
from fileinput import filename


# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def calculate_grade(totalmarks):
    percentage=((totalmarks)/(3*100))*100
    percentage=round(percentage,2)
    print(percentage)
    if percentage >= 70:
        return percentage,"A+"
    elif percentage >= 60:
        return percentage,"A"
    if percentage >= 50:
        return percentage, "B"
    elif percentage >= 40:
        return percentage, "Pass"
    else:
        return percentage,"Fail"

def generate_report(inputFile,ouputFile):
    fread=open(inputFile,"r+")
    fwrite=open(ouputFile,"w+")
    for line in fread.readlines():
        if "RollNo" in line:
            fwrite.writelines(("RollNo ","FirstName "," Percentage "," Grade "))
            fwrite.writelines("\n")
        if "RollNo" not in line:
            data_list=list()
            # data_list=line

            records=line.split(" ")
            marks=0
            for i in range(0,2):
                data_list.append(records[i]+"\t\t")
            # for record in records[::2]:
            #     print(record)
            #     data_list.append(record)
            #     fwrite.writelines(data_list)
            # for record in records[3::]:
            #     marks+=int(record)
            for i in range(2,len(records)):
                marks+=int(records[i])
            per,grade=calculate_grade(marks)
            print(per,grade)
            data_list.append(str(per)+"%"+"\t\t")
            data_list.append(grade+"\t")
            data_list.append("\n")
            fwrite.writelines(data_list)





# def writeFile(file):









if __name__ == '__main__':
    path = "C:/Users/kalsa/OneDrive/Backup storage/OneDrive/Desktop/MSc computer science/bookish-couscous/python/practical-assignment-5/test"
    input_file = path + '/Students.txt'
    output_file = path + '/Percentage.txt'
    generate_report(input_file, output_file)
