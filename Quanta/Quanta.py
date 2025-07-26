import random
import time

cursor = 0
variables = []
run = True

file = input("File to load: ")

with open(file) as f:
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

    elif command[0] == "random":
        variables[int(command[1])] = random.randint(int(command[2]), int(command[3]))
        cursor = cursor + 1

    elif command[0] == "wait":
        if command[1] == "$":
            time.sleep(variables[int(command[2])])
            cursor = cursor + 1
        else:
            time.sleep(command[1])
            cursor = cursor + 1

    elif command[0] == "goto":
        if int(command[1]) == cursor:
            print("Error: Infinite goto loop on itself")
            run = False
        
        else:
            cursor = int(command[1])

    elif command[0] == "var":
        if command[1] == "$":
            for i in range(variables[int(command[1])]):
                variables.append(None)
        else:
            for i in range(int(command[1])):
                variables.append(None)
        cursor = cursor + 1

    elif command[0] == "set":
        if command[1] == "int":
            variables[int(command[2])] = int(command[3])
        elif command[1] == "str":
            variables[int(command[2])] = str(command[3])
        elif command[1] == "float":
            variables[int(command[2])] = float(command[3])
        elif command[1] == "bool":
            variables[int(command[2])] = bool(command[3])
        cursor = cursor + 1

    elif command[0] == "input":
        print(command[3])
        if command[1] == "int":
            variables[int(command[2])] = int(input("Type something: "))
        elif command[1] == "str":
            variables[int(command[2])] = str(input("Type something: "))
        elif command[1] == "float":
            variables[int(command[2])] = float(input("Type something: "))
        elif command[1] == "bool":
            variables[int(command[2])] = bool(input("Type something: "))
        cursor = cursor + 1

    elif command[0] == "end;":
        print("OK")
        run = False

    elif command[0] == "math":
        if command[1] == "+":
            variables[int(command[4])] = variables[int(command[2])] + variables[int(command[3])]
            cursor = cursor + 1
        elif command[1] == "-":
            variables[int(command[4])] = variables[int(command[2])] - variables[int(command[3])]
            cursor = cursor + 1
        elif command[1] == "*":
            variables[int(command[4])] = variables[int(command[2])] * variables[int(command[3])]
            cursor = cursor + 1
        elif command[1] == "/":
            variables[int(command[4])] = variables[int(command[2])] / variables[int(command[3])]
            cursor = cursor + 1

    elif command[0] == "check":
        if command[1] == "==":
            if variables[int(command[2])] == variables[int(command[3])]:
                if int(command[4]) == cursor:
                    print("Error: Infinite goto loop on itself")
                    run = False
        
                else:
                    cursor = int(command[4])
            else:
                cursor = cursor + 1

        elif command[1] == "!=":
            if variables[int(command[2])] != variables[int(command[3])]:
                if int(command[4]) == cursor:
                    print("Error: Infinite goto loop on itself")
                    run = False
        
                else:
                    cursor = int(command[4])
            else:
                cursor = cursor + 1

        elif command[1] == "<":
            if variables[int(command[2])] < variables[int(command[3])]:
                if int(command[4]) == cursor:
                    print("Error: Infinite goto loop on itself")
                    run = False
        
                else:
                    cursor = int(command[4])
            else:
                cursor = cursor + 1

        elif command[1] == ">":
            if variables[int(command[2])] > variables[int(command[3])]:
                if int(command[4]) == cursor:
                    print("Error: Infinite goto loop on itself")
                    run = False
        
                else:
                    cursor = int(command[4])
            else:
                cursor = cursor + 1

        elif command[1] == "<=":
            if variables[int(command[2])] == variables[int(command[3])]:
                if int(command[4]) <= cursor:
                    print("Error: Infinite goto loop on itself")
                    run = False
        
                else:
                    cursor = int(command[4])
            else:
                cursor = cursor + 1

        elif command[1] == ">=":
            if variables[int(command[2])] >= variables[int(command[3])]:
                if int(command[4]) == cursor:
                    print("Error: Infinite goto loop on itself")
                    run = False
        
                else:
                    cursor = int(command[4])
            else:
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