def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def check_fibonacci_number(num):
    fib_sequence = fibonacci_sequence(num)
    if num in fib_sequence:
        return f"O numero {num} pertence a sequência de Fibonacci."
    else:
        return f"O numero {num} nao pertence a sequência de Fibonacci."

def main():
    numero = int(input("Digite um numero para verificar se pertence a sequencia de Fibonacci: "))
    print(check_fibonacci_number(numero))

if __name__ == '__main__':
    main() 