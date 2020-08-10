my_password = "dan123"
right_answer = ""
number_of_tries = 0
max_number_of_tries = 5
Max_try = "not reached"

while right_answer != my_password and Max_try != "Reached":
    if number_of_tries < max_number_of_tries:
        right_answer = input("what is my password?")
        number_of_tries = number_of_tries+1
    else:
        Max_try = "Reached"
if Max_try == "Reached":
    print("Aaccount blocked")
else:
    print("access granted")