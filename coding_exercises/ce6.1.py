todo = input("Enter a member: ") + "\n"

file = open('../files/members.txt', 'r')
member = file.readlines()
file.close()

member.append(todo)

file = open('../files/members.txt', 'w')
file.writelines(member)
file.close()
