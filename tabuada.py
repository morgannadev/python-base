template_base = """
---Tabuada do 2---

     {bloco}

##################
"""

numeros = list(range(1, 11))

for n1 in numeros:
    print("{:-^18}".format("Tabuada do " + str(n1)))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("\n" + "#" * 18)
