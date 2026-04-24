print("Este programa recebe um número de 4 digitos e converte para a constante de kaprekar.")

num = int(input("\nDigite o número: "))

if num < 0 or num > 9999:
    print("\nNúmero inválido!")
else:

    #Variável para contar o número de repetições
    contador = 0

    while num != 6174:

        d1 = num // 1000
        d2 = (num // 100) % 10
        d3 = (num // 10) % 10
        d4 = num % 10

        
        # VALIDAÇÃO: no máximo 2 repetidos
        
        if (d1 == d2 and d1 == d3) or (d1 == d2 and d1 == d4) or (d1 == d3 and d1 == d4) or (d2 == d3 and d2 == d4):
            print("Número inválido: possui três ou mais dígitos iguais")
            break

        # Ordenar crescente
        a = d1
        b = d2
        c = d3
        d = d4

        if a > b: a, b = b, a
        if a > c: a, c = c, a
        if a > d: a, d = d, a
        if b > c: b, c = c, b
        if b > d: b, d = d, b
        if c > d: c, d = d, c

        ndc = a*1000 + b*100 + c*10 + d

        # Ordenar decrescente
        if a < b: a, b = b, a
        if a < c: a, c = c, a
        if a < d: a, d = d, a
        if b < c: b, c = c, b
        if b < d: b, d = d, b
        if c < d: c, d = d, c

        ndd = a*1000 + b*100 + c*10 + d

        resultado = ndd - ndc
        contador += 1

        print("Iteração", contador, ":", ndd, "-", ndc, "=", resultado)

        if resultado == 0:
            break

        num = resultado

    print("Constante de Kaprekar atingida em", contador, "iterações.")