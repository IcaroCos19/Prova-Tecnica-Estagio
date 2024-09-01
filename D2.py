def fibo(n):
    fi = [0,1]
    while fi [-1] < n:
        fi.append(fi[-1]+fi[-2])

    if n in fi:
        return f"O numero {n} pertence a sequencia."
    else:
        return f"O numero {n} nao pertence a sequencia."
    
n = int(input("Digite o valor que voce deseja conferir: "))
resultado = fibo(n)
print(resultado)