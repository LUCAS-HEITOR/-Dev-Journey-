import time
import resources

list = []
i = 0
while i < 100:
    try:
        time.sleep(0.1)
        x = 1024 * 1024 #1 MB
        a = 'x' * x
        i += 1

        list.append(a)
        print(i)
    except KeyboardInterrupt:
        break

    finally:
        print("Finished")


#E aí mano! No meu app/jogo, eu quero criar um sistema de memória dinâmico com um limite estrito de recursos. Pense nisso como uma barra de progresso de 0% a 100%. Quando o app está parado, ele usa pouca RAM (tipo 0-10%). Mas quando há uma tarefa pesada, ele aumenta dinamicamente para 70-100%. A regra principal é: ele NUNCA vai ultrapassar esse limite de 100% que eu defini. Quando a tarefa pesada termina, o Garbage Collector libera a memória e ela volta a cair. Basicamente, eu quero um limite estrito de memória sem vazamentos (memory leaks)."
