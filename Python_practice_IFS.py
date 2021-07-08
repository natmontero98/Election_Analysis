counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver': 
    print(counties[1])

#If else statement
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("turn on the AC")
else: 
    print("open the windows")

 #Nested if else
 #what is the score?
score = int(input("what is your test score?"))
if score >= 90:
    print('your grade is an A.')
elif score >= 80:
    print('your grade is a B')
elif score >= 70:
    print('your grade is a C')
elif score >= 60:
    print('your grade is a D')
else:
    print('your grade is an F')
