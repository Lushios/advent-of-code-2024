from time import sleep

with open("input.txt") as file:
    data = file.read()


class Gate:
    def __init__(self, source1, operation, source2, destination):
        self.source1 = source1
        self.operation = operation
        self.source2 = source2
        self.destination = destination

    def operate(self):
        if self.operation == 'AND':
            result = wire_values[self.source1] & wire_values[self.source2]
        elif self.operation == 'OR':
            result = wire_values[self.source1] | wire_values[self.source2]
        else:
            result = wire_values[self.source1] ^ wire_values[self.source2]
        return self.destination, result


wires, input_gates = data.split('\n\n')

wires = [wire.split(': ') for wire in wires.split('\n')]
wire_values = {name: int(value) for name, value in wires}

input_gates = [gate.split(' -> ') for gate in input_gates.split('\n')]
gates = {}
# wire_pairs = []
z_counter = 0
for gate in input_gates:
    gate_destination = gate[1]
    if gate_destination[0] == 'z':
        z_counter += 1
    gate_source1, operation, gate_source_2 = gate[0].split(' ')
    # wire_pair = (gate_source1, gate_source_2)
    # wire_pairs.append(wire_pair)
    gates[gate_destination] = Gate(gate_source1, operation, gate_source_2, gate_destination)


while len([wire for wire in wire_values if wire[0] == 'z']) < z_counter:
    for destination_gate, gate in gates.items():
        if gate.source1 not in wire_values or gate.source2 not in wire_values:
            continue
        destination, value = gate.operate()
        wire_values[destination] = value

result = ''
for i in range(z_counter):
    key = 'z0' + str(i) if i < 10 else 'z' + str(i)
    result = str(wire_values[key]) + result

result = int(result, 2)
print(result)
