# colours = {"red","green","blue", "orange", "red", "blue", "red"}
# chess_pieces = set(["king","queen","knight","knight", "bishop","bishop",
#                     "rook", "rook", "pawn", "pawn", "pawn", "pawn", "pawn",
#                     "pawn", "pawn", "pawn"])
# print(f"Colours: {colours}")
# print(f"Object type of colours variable: {type(colours)}")
# print(f"Chess Pieces: {chess_pieces}")
# print(f"Object type of chess_pieces variable: {type(chess_pieces)}")

# s1 = {1, 2, 3}
# s2 = {4, 5, 6}
# print(s1.isdisjoint(s2))

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# s1.add(4)
# print(f"Set 1 after adding 4: {s1}")
# s1.update(s2)
# print(f"Set 1 after adding Set 2: {s1}")

# s1 = {1, 2, 3}
# s2 = {1, 2, 3}
# s1.add(4)
# print(f"Set 1 after adding 4: {s1}")
# s1.update(s2) # (1)
# print(f"Set 1 after adding Set 2: {s1}")

# print(s1 < s2)

# manager_nodes = {"host1", "host7", "host12"}
# print(f"Manager Nodes: {manager_nodes}")
# manager_nodes.discard("host7")
# manager_nodes.discard("host13")  # This will not raise an error if "host13" is not present
# print(f"Manager Nodes after discarding 'host7' and 'host13': {manager_nodes}")

# print(f"Cluster Nodes: {cluster_nodes}")
# print(f"Manager Nodes are present in Cluster Nodes: {manager_nodes.issubset(cluster_nodes)}")
# print(f"Cluster Nodes contain all Manager Nodes: {cluster_nodes.issuperset(manager_nodes)}")

mechanic_tools = {"wrench", "screwdriver", "hammer", "pliers", "jack"}
carpenter_tools = {"saw", "hammer", "chisel", "screwdriver", "level"}
print(f"Mechanic-only Tools: {mechanic_tools.difference(carpenter_tools)}")
print(f"Carpenter-only Tools: {carpenter_tools.difference(mechanic_tools)}")
# print(f"Intersection: {mechanic_tools.intersection(carpenter_tools)}")
# print(f"Union: {mechanic_tools.union(carpenter_tools)}")

# s1.update(s2)
# print(f"Set 1 after adding 4 and updating with Set 2: {s1}")
# s1.remove(2)
# s1.discard(3)
# print(f"Set 1 after removing 2 and discarding 3: {s1}")
# s1.pop()
# print(f"Set 1 after popping an element: {s1}")
# s1.clear()
# print(f"Set 1 after clearing: {s1}")
# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# print(f"Set 1: {s1}")
# print(f"Set 2: {s2}")
# print(f"Union of Set 1 and Set 2: {s1.union(s2)}")
# print(f"Intersection of Set 1 and Set 2: {s1.intersection(s2)}")
# print(f"Difference of Set 1 and Set 2: {s1.difference(s2)}")
# print(f"Symmetric Difference of Set 1 and Set 2: {s1.symmetric_difference(s2)}")
# # Check if Set 1 is a subset of Set 2
# print(f"Is Set 1 a subset of Set 2? {s1.issubset(s2)}")
# # Check if Set 2 is a superset of Set 1
# print(f"Is Set 2 a superset of Set 1? {s2.issuperset(s1)}")
# # Check if Set 1 is disjoint with Set 2
# print(f"Are Set 1 and Set 2 disjoint? {s1.isdisjoint(s2)}")
# # Check if Set 1 is equal to Set 2
# print(f"Are Set 1 and Set 2 equal? {s1 == s2}")