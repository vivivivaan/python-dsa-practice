from LinkedList import LinkedList

ll = LinkedList(100)
len__: int = ll.get_length()

#  pop_head()

for i in range(2, 11):
    ll.append(i * 100)

ll.print_list_by_idx()

print(f"Getting node at 4th index: {ll.get(4).data}\n")
print("Updating the node at 4th index..")
if ll.set_(4, 2000):
    print(
        "The updated linked list after successfully updating node at the 4th index is:"
    )
    ll.print_list_by_idx()
else:
    print("The node at the 4th index could not be updated.\n")

print("Inserting the node at the 4th index..")
ll.insert(4, 550)
print("The linked list after successful node insertion at the 4th index is..")
ll.print_list_by_idx()

print("The linked list reversed is: ")
ll.reverse()

print(f"The mid node in the reversed linked list is: {ll.find_mid().data}\n")
print("Time to pop the heads!\n")
for head in range(3):
    print(f"Popping the element {head}: ", ll.pop_head().data)

print()
ll.print_list_by_idx()

ll.create_cycle()
ll.print_list_by_idx()

# print("The linked list after creating cycle: ")
# # ll.create_cycle()
# if ll.has_loop():
#     print("The linked list has a loop...")
#     sys.exit()
# else:
#     print("Did not detect any loops in the linked list. Cont..")

# print(f"Popping the element {ll.get_length()}: ", ll.pop_head().data)
# # print(f"The Linked list after popping the element {ll.get_length()} is: ")
# ll.print_list_by_idx()

# print(f"Popping the element {ll.get_length()}: ", ll.pop_head().data)
# # print(f"The Linked list after popping the element {ll.get_length()} is: ")
# ll.print_list_by_idx()

# print(f"Popping the element {ll.get_length()}: ", ll.pop_head().data)
# # print(f"The Linked list after popping the element {ll.get_length()} is: ")
# ll.print_list_by_idx()

# print(f"Popping the element {ll.get_length()}: ", ll.pop_head().data)
# # print(f"The Linked list after popping the element {ll.get_length()} is: ")
# ll.print_list_by_idx()

# print(f"Popping the element {ll.get_length()}: ", ll.pop_head().data)
# # print(f"The Linked list after popping the element {ll.get_length()} is: ")
# ll.print_list_by_idx()


# # pop_tail()

# for i in range(2, 9):
#     ll.append(i * 100)

# print("The Linked list is: ")
# ll.print_list()

# print(f"Popping the element {ll.get_length()}: ", ll.pop_tail().data)
# print(f"The Linked list after popping the element {ll.get_length()} is: ")
# ll.print_list()

# print(f"Popping the element {ll.get_length()}: ", ll.pop_tail().data)
# print(f"The Linked list after popping the element {ll.get_length()} is: ")
# ll.print_list()

# print(f"Popping the element {ll.get_length()}: ", ll.pop_tail().data)
# print(f"The Linked list after popping the element {ll.get_length()} is: ")
# ll.print_list()

# print(f"Popping the element {ll.get_length()}: ", ll.pop_tail().data)
# print(f"The Linked list after popping the element {ll.get_length()} is: ")
# ll.print_list()

# print(f"Popping the element {ll.get_length()}: ", ll.pop_tail().data)
# print(f"The Linked list after popping the element {ll.get_length()} is: ")
# ll.print_list()
