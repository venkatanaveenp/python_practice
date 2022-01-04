"""5. Mr.Ben has started a new Food delivery company called “OnWheels”.
As a newly started company, he is looking for a Manager to handle all the operations and take care of any issues that might arise. He prefers a candidate with a minimum experience of 5yrs, if not he does not want to
 
take them as an employee. Secondly the salary is fixed based on the Degree and years of experience.

Gender	Experience	Qualification	Salary

Male	>=10	PG	Rs.75000
	>5 and <10	PG	Rs.60000
	>=10	Graduate	Rs.50000
	>5 and <10	Graduate	Rs.35000

Female	>=10	PG	Rs.60000
	>5 and <10	PG	Rs.45000
	>=10	Graduate	Rs.30000
	>5 and <10	Graduate	Rs.20000

Help Mr.Ben to decide whether the applied candidate is eligible for the job and if yes, what would be his/her salary.

Sample Input- Employee Name:Srikanth Gender:Male
Years of Exp:12 Qualification:PG Expected Output:
Yes Srikanth is eligible for the Job with a salary of Rs.75000

Sample Input- Employee Name:Srikanth Gender:Male
Years of Exp:4 Qualification:PG Expected Output:
No Srikanth is not eligible for the Job

Sample Input- Employee Name:Janane Gender:Female
Years of Exp:10 Qualification:Graduate Expected Output:
Yes Janane is eligible for the Job with a salary of Rs.30000"""




name=input("enter name=")
gender=input("gender[male/female]=")
experience=int(input("experience="))
education=input("education[pg/graduate]")
if gender=='female':
    if experience>5:
        print("eligible for job")
        if experience>=10 and education=='pg':
            print(name,"is eligible for the Job with a salary of Rs.60000")
        
        elif experience>5 and experience<10 and education=='pg':
            print(name,"is eligible for the Job with a salary of Rs.45000")
        
        elif experience>=10 and education=='graduate':
            print(name,"is eligible for the Job with a salary of Rs.30000")
        
        elif experience>5 and experience<10 and education=='graduate':
            print(name,"is eligible for the Job with a salary of Rs.20000")
if gender=='male':
    if experience>=5:
        print("eligible for job")
        if experience>=10 and education=='pg':
            print(name,"is eligible for the Job with a salary of Rs.75000")
        
        elif experience>5 and experience<10 and education=='pg':
            print(name,"is eligible for the Job with a salary of Rs.60000")
        
        elif experience>=10 and education=='graduate':
            print(name,"is eligible for the Job with a salary of Rs.50000")
        
        elif experience>5 and experience<10 and education=='graduate':
            print(name,"is eligible for the Job with a salary of Rs.35000")
    


    