"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
cust_name = str(input("Enter name: "))
choice = str(str.upper(input("(H)ello\n(G)oodbye\n(Q)uit\n>>>")))
while choice != "Q":
    if choice == "H":
        print(f"Hello {cust_name}")
    elif choice == "G":
        print(f"Goodbye {cust_name}")
    else:
        print(f"Invalid choice")
    choice = str(str.upper(input("(H)ello\n(G)oodbye\n(Q)uit\n>>>")))
print(f"Finished.")
