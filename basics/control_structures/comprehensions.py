

# # General Form
# # new_list = [<expression> for <item> in <iterable> if <condition>]
# new_list = [x for x in range(10)]
# new_set = {x for x in range(10)}
# new_dict = {k:v for k,v in enumerate(range(10))}

# print(f"New List: {new_list}")
# print(f"New Set: {new_set}")
# print(f"New Dict: {new_dict}")

# General Form
# new_list = [<expression> for <item> in <iterable> if <condition>]

# for_loop_result = []
# for x in range(5):
#     for_loop_result.append(x**2)

# comprehension_result = [x**2 for x in range(5)]

# print(f"For Loop Result: {for_loop_result}")
# print(f"Comprehension Result: {comprehension_result}")

# comprehension_result = [x**2 for x in range(10) if x % 2 == 0]
# print(f"Comprehension Result: {comprehension_result}")

# numbers = [1, 2, 3, 4, 5, 6]
# odd_even = {num: 'odd' for num in numbers if num % 2 == 1}
# print("Odd/Even classification:", odd_even)

# grades = [85, 92, 78, 65, 98, 72]
# results = ["Pass" if grade >= 70 else "Fail" for grade in grades]
# print(results)  # ['Pass', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass']

# # Sample data - a list of email domains from user signups
# emails = ['user1@gmail.com', 'user2@yahoo.com', 'user3@gmail.com',
#           'user4@outlook.com', 'user5@gmail.com', 'user6@yahoo.com']

# # Extract unique domains using a set comprehension
# unique_domains = {email.split('@')[1] for email in emails}
# print(f"Unique domains: {unique_domains}")  # {'gmail.com', 'yahoo.com', 'outlook.com'}


words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
word_length_category = {
    word: 'short' if len(word) <= 5 else 'long'
    for word in words
}
print("Conditional expression - all words categorized:", word_length_category)