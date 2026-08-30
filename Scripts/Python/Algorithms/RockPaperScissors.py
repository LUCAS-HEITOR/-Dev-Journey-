import random

Escolha = ["Rock", "Paper", "Scissors"]
jogador = input("Choose Rock, Paper or Scissors: ").capitalize()


def Computador_Escolhe(x):
    computador = random.choice(Escolha)
    if x == computador:
        return f"Tie Computer Chose {computador}"
    if (
        (x == "Rock" and computador == "Scissors")
        or (x == "Scissors" and computador == "Paper")
        or (x == "Paper" and computador == "Rock")
    ):
        return f"You Won computer chose {computador}"
    else:
        return f"You lost computer chose {computador}"


print(Computador_Escolhe=(jogador))
