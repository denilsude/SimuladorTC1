class TC1:
    def __init__(self):
        self.registers = [0] * 8  # Registradores r0 a r7
        self.pc = 0  # Contador de programa
        self.memory = [0] * 16  # Memória com 16 locais
        self.running = True

    def fetch(self):
        instruction = self.memory[self.pc]
        self.pc += 1
        return instruction

    def decode(self, instruction):
        opcode, operands = instruction.split(' ', 1)
        return opcode, operands.split(',')

    def execute(self, opcode, operands):
        if opcode == 'MOV':
            dest_reg, value = operands
            self.registers[int(dest_reg[1])] = int(value)
        elif opcode == 'ADD':
            dest_reg, src_reg1, src_reg2 = operands
            self.registers[int(dest_reg[1])] = self.registers[int(src_reg1[1])] + self.registers[int(src_reg2[1])]
        elif opcode == 'HLT':
            self.running = False
        else:
            print(f"Opcode não suportado: {opcode}")

    def run(self, program):
        self.running = True
        self.pc = 0
        while self.running and self.pc < len(program):
            instruction = self.fetch()
            opcode, operands = self.decode(instruction)
            self.execute(opcode, operands)

# Programa de teste em linguagem de montagem TC1
program = [
    "MOV r1,10",   # Mover 10 para r1
    "MOV r2,20",   # Mover 20 para r2
    "ADD r3,r1,r2",  # Adicionar r1 e r2 e armazenar em r3
    "HLT"  # Parar a execução
]

# Criar uma instância do simulador TC1 e executar o programa
simulator = TC1()
simulator.run(program)

# Imprimir o estado final dos registradores após a execução do programa
print("Estado final dos registradores:")
for i, value in enumerate(simulator.registers):
    print(f"r{i}: {value}")
