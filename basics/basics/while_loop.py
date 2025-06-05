keep_looping = True
while keep_looping:
    user_input = input("Enter 'exit' to stop the loop: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        keep_looping = False
    else:
        print(f"You entered: {user_input}")

value = 10

while value > 0:
    print(f"Current value: {value}")
    value -= 1  # Decrease the value by 1 each iteration
print("Loop has ended.")