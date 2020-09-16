import tutorial01 as A1

actual_answers = [9, 12, 80, 5, 8, [2, 6, 18, 54, 162], [2, 3, 4, 5, 6]]
student_answers = []

test_case_1 = A1.add(4, 5)
student_answers.append(test_case_1)

test_case_2 = A1.subtract(14, 2)
student_answers.append(test_case_2)

test_case_3 = A1.multiply(10, 8)
student_answers.append(test_case_3)

test_case_4 = A1.divide(10, 2)
student_answers.append(test_case_4)

test_case_5=A1.power(2,3)
student_answers.append(test_case_5)

a = 2 # starting number 
r = 3 # Common ratio 
n = 5 # N th term to be find 

gp = A1.printGP(a, r, n) 
gp = list(gp) 
student_answers.append(gp)

print(gp)

# Driver code 
a = 2    # starting number 
d = 1    # Common difference 
n = 5    # N th term to be find 
  
ap=A1.printAP(a, d, n)
ap=list(ap)
student_answers.append(ap)
print(ap) 



print(actual_answers)
print(student_answers)

total_test_cases = len(actual_answers)
count_of_correct_test_cases = 0

for x, y in zip(actual_answers, student_answers):
    if x == y:
        count_of_correct_test_cases += 1

print(f"Test Cases Passed = '{count_of_correct_test_cases}'  / '{total_test_cases}'")
