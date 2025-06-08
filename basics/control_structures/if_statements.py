user_input_username = "john_doe"
user_input_password = "secure_password"

correct_username = "john_doe"
correct_password = "secure_password"

if user_input_username == correct_username and \
    user_input_password == correct_password:
     print("Access granted!")
else:
     print("Access denied. Please check your username and password.")