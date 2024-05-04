# Simulador TC1

Este é um simulador básico para uma arquitetura fictícia denominada TC1. Ele suporta um conjunto limitado de instruções e possui um conjunto fixo de registradores e memória.

## Estrutura do Simulador

O simulador `TC1` consiste nas seguintes partes:

### Inicialização

No método `__init__`, são inicializados os registradores, o contador de programa (`pc`) e a memória.

### Busca (`fetch`)

O método `fetch` busca a próxima instrução da memória, avançando o contador de programa.

### Decodificação (`decode`)

O método `decode` divide uma instrução em opcode e operandos.

### Execução (`execute`)

O método `execute` executa a instrução com base no opcode e nos operandos.

### Execução do Programa (`run`)

O método `run` executa o programa fornecido, buscando, decodificando e executando cada instrução até encontrar uma instrução de parada ou até o final do programa.

## Instruções Suportadas

- `MOV`: Move um valor para um registrador.
- `ADD`: Adiciona o conteúdo de dois registradores e armazena o resultado em um terceiro registrador.
- `HLT`: Para a execução do programa.

## Exemplo de Uso

Um exemplo de programa de teste em linguagem de montagem TC1 é fornecido no código. Após a criação de uma instância do simulador `TC1` e a execução do programa, o estado final dos registradores é impresso.

```python
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
```

Esse código cria um simulador `TC1`, executa um programa de teste e imprime o estado final dos registradores.
