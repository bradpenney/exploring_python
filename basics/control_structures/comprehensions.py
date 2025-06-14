

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

comprehension_result = [x**2 for x in range(10) if x % 2 == 0]
print(f"Comprehension Result: {comprehension_result}")