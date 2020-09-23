import numpy as np
import tutorial02 as A2
import math

actual_answers = [0.55, 0.64, 0.30, 0.09, -0.38,
                  1.99, 0.47, 0.22, 0.40, -1.47, 0.05, 0, 0, 0]
student_answers = []


x, y = np.loadtxt("results.csv", delimiter=",",
                  usecols=(0, 1), unpack=True, skiprows=1)
x = list(x)
y = list(y)

test_case_1 = A2.mean(x)
student_answers.append(test_case_1)

test_case_2 = A2.median(x)
student_answers.append(test_case_2)

test_case_3 = A2.standard_deviation(x)
student_answers.append(test_case_3)

test_case_4 = A2.variance(x)
student_answers.append(test_case_4)

test_case_5 = A2.skewness(x)
student_answers.append(test_case_5)

test_case_6 = A2.kurtosis(x)
student_answers.append(test_case_6)

test_case_7 = A2.rmse(x, y)
student_answers.append(test_case_7)

test_case_8 = A2.mse(x, y)
student_answers.append(test_case_8)

test_case_9 = A2.mae(x, y)
student_answers.append(test_case_9)

test_case_10 = A2.nse(x, y)
student_answers.append(test_case_10)

test_case_11 = A2.pcc(x, y)
student_answers.append(test_case_11)

p = [1, 4, 5, 7, 7, 5, 4]
q = [5, 7, 2, 4, 8, 9, 1, 9]

# Invalid since length of p & q is not same. #Return 0
test_case_10 = A2.mae(p, q)
student_answers.append(test_case_10)

r = [1, 4, 5, "a", 7, "India", 4]
# Invalid since list contains non-numeric data-type e.g., string/character #Return 0
test_case_11 = A2.mean(r)
student_answers.append(test_case_11)

# Invalid since list  r contains non-numeric data-type e.g., string/character #Return 0
test_case_12 = A2.rmse(p, r)
student_answers.append(test_case_12)

print(actual_answers)
print(student_answers)

total_test_cases = len(actual_answers)
count_of_correct_test_cases = 0

for x, y in zip(actual_answers, student_answers):
    if x == round(y, 2):
        count_of_correct_test_cases += 1

print(
    f"Test Cases Passed = '{count_of_correct_test_cases}'  / '{total_test_cases}'")
