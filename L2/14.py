# Accept marks of three subjects. Print total and average along with whether a candidate has passed or fail. If student secures <= 39 marks in any subject, consider him as fail. Also assigned a subject wise grade based on the following table:

def grades(marks=0):
    if marks <= 39:
        return "Fail F"
    elif marks in range(40,45):
        return "Pass P"
    elif marks in range(45,50):
        return "Pass C"
    elif marks in range(50,55):
        return "Pass B"
    elif marks in range(55,60):
        return "Pass B+"
    elif marks in range(60,70):
        return "Pass A"
    elif marks in range(70,80):
        return "Pass A+"
    elif marks in range(80,100):
        return "Pass O"

m1,m2,m3 = int(input("Enter marks of 1st subject : ")),int(input("Enter marks of 2nd subject : ")),int(input("Enter marks of 3rd subject : "))

avg = round((m1+m2+m3)/3)
print("Average marks : ",avg)

sub1,sub2,sub3 = grades(m1),grades(m2),grades(m3)

print("Subject 1 : ",sub1,"\nSubject 2 : ",sub2,"\nSubject 3 : ",sub3,"\nOverall grade : ", grades(avg))