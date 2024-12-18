with open("input.txt") as file:
    data = file.read()

registers, program = data.split("\n\n")
registers = registers.splitlines()
registerA, registerB, registerC = [int(register.split(': ')[1]) for register in registers]

program = program.split(': ')[1]
program = [int(num) for num in program.split(',')]


def get_operand_combo_value(operand, registerA, registerB, registerC):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return registerA
        case 5:
            return registerB
        case 6:
            return registerC
        case _:
            return None


def run_command(command, operand, register_a, register_b, register_c, instructions_pointer, output):
    combo_value = get_operand_combo_value(operand, register_a, register_b, register_c)
    newRegisterA, newRegisterB, newRegisterC = register_a, register_b, register_c
    default_register_move = True
    match command:
        case 0:
            newRegisterA = register_a // pow(2, combo_value)
        case 1:
            newRegisterB = register_b ^ operand
        case 2:
            newRegisterB = combo_value % 8
        case 3:
            if newRegisterA != 0:
                default_register_move = False
                instructions_pointer = operand
        case 4:
            newRegisterB = register_b ^ register_c
        case 5:
            output.append(combo_value % 8)
        case 6:
            newRegisterB = register_a // pow(2, combo_value)
        case 7:
            newRegisterC = register_a // pow(2, combo_value)

    if default_register_move:
        instructions_pointer += 2

    return newRegisterA, newRegisterB, newRegisterC, instructions_pointer, output


instructions_pointer = 0
output = []

i = 0
while instructions_pointer < len(program):
    print(i)
    command = program[instructions_pointer]
    operand = program[instructions_pointer + 1]
    registerA, registerB, registerC, instructions_pointer, output = run_command(
        command,
        operand,
        registerA,
        registerB,
        registerC,
        instructions_pointer,
        output
    )
    i += 1

print(','.join([str(num) for num in output]))
print(len(output))
