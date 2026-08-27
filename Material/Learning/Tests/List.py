import keyboard

# frutas = [
#     "Maçã", "Banana", "Laranja", "Morango", "Uva",
#     "Manga", "Abacaxi", "Melancia", "Mamão", "Limão",
#     "Abacate", "Pêra", "Pêssego", "Kiwi", "Maracujá",
#     "Goiaba", "Cereja", "Ameixa", "Amora", "Coco"
# ]

# import random

# print(random.choices(frutas, k=8))


def acao_ao_digitar():
    print("Caiu No FallBack")

def action():
    keyboard.add_word_listener("stop", callback=acao_ao_digitar, triggers=['space', 'enter'])
    keyboard.wait("esc")

if __name__ == "__main__":
    try:
        action()
    except Exception as e:
        print("Erro")
    finally:
        print("Programa finalizado ")
