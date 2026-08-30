import random
import sys
from datasets import load_dataset

# Classe para organizar as cores no terminal (ANSI escape codes)
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def imprimir_placar(acertos: int, tentativas: int) -> None:
    """Exibe o placar atualizado com formatação visual."""
    print(f"\n{Colors.CYAN}{'='*35}{Colors.RESET}")
    print(f"{Colors.CYAN}🎯 Placar: {acertos} acertos de {tentativas} tentativas{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*35}{Colors.RESET}\n")

def main():
    print(f"{Colors.YELLOW}Carregando o dataset... Isso pode levar alguns instantes.{Colors.RESET}")

    # Tratamento de erro ao carregar o dataset
    try:
        dataset = load_dataset("Hemg/AI-Generated-vs-Real-Images-Datasets", split="train")
    except Exception as e:
        print(f"{Colors.RED}Falha ao carregar o dataset. Verifique sua conexão. Erro: {e}{Colors.RESET}")
        sys.exit(1)

    # Mapeamento dos valores do dataset (0 para Real, 1 para AI)
    valores_dataset = {0: "Real", 1: "AI"}

    # Controle de estado do jogo
    acertos = 0
    tentativas = 0

    print(f"\n{Colors.GREEN}✅ Dataset carregado com sucesso!{Colors.RESET}")
    print(f"Pressione 'Ctrl+C' ou digite '0' a qualquer momento para encerrar o programa.\n")

    while True:
        try:
            # Seleção de imagem aleatória
            indice = random.randint(0, len(dataset) - 1)
            exemplo = dataset[indice]

            imagem = exemplo["image"]
            label_num = exemplo["label"]
            label_texto = valores_dataset.get(label_num, "Desconhecido")

            print(f"🖼️  Abrindo a imagem #{indice} no seu visualizador padrão...")
            imagem.show()

            # Loop interno de validação de input
            while True:
                resposta_str = input(f"Esta imagem é {Colors.YELLOW}(1) Real{Colors.RESET} ou {Colors.YELLOW}(2) AI{Colors.RESET}? (0 para sair): ").strip()

                # Valida se o usuário digitou uma opção permitida
                if resposta_str not in ['0', '1', '2']:
                    print(f"{Colors.RED}Entrada inválida. Digite 1 (Real), 2 (AI) ou 0 para sair.{Colors.RESET}")
                    continue
                break

            resposta_usuario = int(resposta_str)

            # Condição de saída limpa
            if resposta_usuario == 0:
                print(f"\n{Colors.YELLOW}Encerrando a sessão...{Colors.RESET}")
                break

            # Conversão lógica: Usuário digita 1 (Real) -> mapeia para 0. Digita 2 -> mapeia para 1.
            palpite_convertido = 0 if resposta_usuario == 1 else 1
            tentativas += 1

            # Avaliação do resultado
            if palpite_convertido == label_num:
                acertos += 1
                print(f"{Colors.GREEN}✨ Correto! A imagem realmente era {label_texto}.{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ Errado! A imagem era {label_texto}.{Colors.RESET}")

            imprimir_placar(acertos, tentativas)

        # Captura interrupção forçada via teclado (Ctrl+C)
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}Execução interrompida pelo usuário.{Colors.RESET}")
            break
        # Captura qualquer outro erro inesperado durante o loop
        except Exception as e:
            print(f"\n{Colors.RED}Ocorreu um erro inesperado: {e}{Colors.RESET}")
            break

    # Exibição do resultado final
    taxa_acerto = (acertos / tentativas * 100) if tentativas > 0 else 0
    print(f"\n{Colors.GREEN}Resumo da Sessão: Você acertou {acertos} de {tentativas} imagens ({taxa_acerto:.1f}%).{Colors.RESET}\n")

if __name__ == "__main__":
    main()
