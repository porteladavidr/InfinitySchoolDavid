def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

def verificar_situacao(media):
    if media == 10:
        return "Parabéns, sua média é 10"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    notas = []
    while True:
        nota = input("Digite uma nota (ou digite 'sair' para finalizar): ")
        if nota.lower() == 'sair':
            break
        else:
            notas.append(float(nota))

    if notas:
        media = calcular_media(notas)
        situacao = verificar_situacao(media)
        print(f"A média do aluno é: {media:.2f}")
        print(f"Situação: {situacao}")
    else:
        print("Nenhuma nota foi inserida.")

if __name__ == "__main__":
    main()
10