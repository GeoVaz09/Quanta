cursor = 0
variables = []
run = True

with open('program.txt') as f:
    program = [line.rstrip() for line in f]

while run:

    command = program[cursor].split("; ")
#    print(command)

    if command[0] == "print":
        if command[1] == "$":
            print(variables[int(command[2])])
            cursor = cursor + 1
        else:
            print(command[1])
            cursor = cursor + 1

    elif command[0] == "#":
#        print("Comment:", command[1])
        cursor = cursor + 1

    elif command[0] == "goto":
        if int(command[1]) == cursor:
            print("Error: Infinite goto loop on itself")
            run = False
        
        else:
            cursor = int(command[1])

    elif command[0] == "var":
        for i in range(int(command[1])):
            variables.append(None)
        cursor = cursor + 1

    elif command[0] == "set":
        variables[int(command[1])] = command[2]
        cursor = cursor + 1

    elif command[0] == "input":
        print(command[2])
        variables[int(command[1])] = input("Type something: ")
        cursor = cursor + 1

    elif command[0] == "end;":
        print("OK")
        run = False

    elif command[0] == "math":
        if command[1] == "+":
            variables[int(command[4])] = int(variables[int(command[2])]) + int(variables[int(command[3])])
            cursor = cursor + 1
        elif command[1] == "-":
            variables[int(command[4])] = int(variables[int(command[2])]) - int(variables[int(command[3])])
            cursor = cursor + 1
        elif command[1] == "*":
            variables[int(command[4])] = int(variables[int(command[2])]) * int(variables[int(command[3])])
            cursor = cursor + 1
        elif command[1] == "/":
            variables[int(command[4])] = int(variables[int(command[2])]) / int(variables[int(command[3])])
            cursor = cursor + 1

    elif command[0] == "break;":
        user = input('Press Enter to continue or type "q" to exit: ')
        
        if user == "q":
            print("Exiting the code...")
            print("OK")
            run = False
        
        else:
            cursor = cursor + 1
    
    else:
        print("Error: Command not found!")
        run = False