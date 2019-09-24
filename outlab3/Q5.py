import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('--first_name',nargs='+',required =True,help="first name of the student")
parser.add_argument('--last_name',nargs='+',required =True,help="last name of the student")
parser.add_argument('--roll_no',nargs='+',required =True, help="roll no. of the student")
parser.add_argument('--gender',nargs='+',required =True,help="his/her gender")
parser.add_argument('--mobile',nargs='+',required =True,help="contact details")
parser.add_argument('--dept',nargs='+',required =True,help="department/branch")
parser.add_argument('--CGPA',nargs='+',required =True,help="his/her CGPA")
args = parser.parse_args()
# print(args.first_name)

csvfile = open("student_database.csv",'a')
fields = ['First Name','Last Name','Roll Number','Gender','Mobile','Dept','CGPA']
csvwriter = csv.writer(csvfile)
# csvwriter.writerow(fields)

row = [args.first_name[0],args.last_name[0],args.roll_no[0],args.gender[0],args.mobile[0],args.dept[0],args.CGPA[0]]

csvwriter.writerow(row)
print("Successfully Added!!")

