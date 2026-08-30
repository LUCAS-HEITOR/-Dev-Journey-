import random
import sys
import os
import tempfile
from datasets import load_dataset
from PIL import Image

# Classe para organizar as cores no terminal (ANSI escape codes)
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def redimensionar_imagem(imagem: Image.Image, tamanho_minimo: int = 600) -> Image.Image:
    """
    Aplica upscaling na imagem caso ela seja menor que o threshold estabelecido.
    A proporção (aspect ratio) original da imagem é estritamente mantida.
    """
    largura, altura = imagem.size 

    if largura < tamanho_minimo or altura < tamanho_minimo:
        # Calcula o multiplicador necessário para que a menor dimensão atinja o tamanho mínimo
        fator_escala = max(tamanho_minimo / largura, tamanho_minimo / altura)
        nova_largura = int(largura * fator_escala)
        nova_altura = int(altura * fator_escala)

        # Utiliza o filtro de reamostragem LANCZOS, que emprega convolução matemática avançada
        # para evitar ao máximo o serrilhado (pixelização) comum ao esticar imagens pequenas.
        return imagem.resize((nova_largura, nova_altura), Image.Resampling.LANCZOS)

    return imagem

def imprimir_placar(acertos: int, tentativas: int) -> None:
    print(f"\n{Colors.CYAN}{'='*35}{Colors.RESET}")
    print(f"{Colors.CYAN}🎯 Placar: {acertos} acertos de {tentativas} tentativas{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*35}{Colors.RESET}\n")

def main():
    print(f"{Colors.YELLOW}Estabelecendo conexão de streaming com o servidor remoto...{Colors.RESET}")

    try:
        # A flag streaming=True é o coração desta otimização. Ela impede o download integral
        # do dataset para o disco rígido, buscando os dados sob demanda.
        dataset_stream = load_dataset("Hemg/AI-Generated-vs-Real-Images-Datasets", split="train", streaming=True)

        # Adiciona aleatoriedade ao fluxo com um buffer local e converte em um iterador
        dataset_iterador = iter(dataset_stream.shuffle(seed=random.randint(0, 9999), buffer_size=100))
    except Exception as e:
        print(f"{Colors.RED}Falha de I/O na rede. Detalhes do erro: {e}{Colors.RESET}")
        sys.exit(1)

    valores_dataset = {0: "Real", 1: "AI"}
    acertos = 0
    tentativas = 0

    print(f"\n{Colors.GREEN}✅ Conexão ativa! Os dados não serão armazenados permanentemente.{Colors.RESET}")
    print(f"Pressione 'Ctrl+C' ou digite '0' a qualquer momento para abortar o processo.\n")

    while True:
        caminho_arquivo_temporario = None

        try:
            # Consome o próximo pacote de dados da fila de streaming (baixa direto para a RAM)
            exemplo = next(dataset_iterador)

            imagem_original = exemplo["image"]
            label_num = exemplo["label"]
            label_texto = valores_dataset.get(label_num, "Desconhecido")

            # Etapa de pré-processamento: ajusta a resolução de imagens diminutas
            imagem_processada = redimensionar_imagem(imagem_original, tamanho_minimo=600)

            # Instanciação de arquivo em nível de sistema operacional
            # mkstemp gera um descritor de arquivo (fd) e um caminho absoluto seguro
            fd, caminho_arquivo_temporario = tempfile.mkstemp(suffix=".png")
            os.close(fd)

            # Persiste o buffer da RAM no disco temporariamente para o visualizador do SO conseguir ler
            imagem_processada.save(caminho_arquivo_temporario, format="PNG")

            print(f"🖼️  Renderizando imagem...")

            # Dispara uma chamada de sistema para abrir o visualizador padrão
            Image.open(caminho_arquivo_temporario).show()

            # Bloqueia a execução do script aguardando I/O do usuário
            while True:
                resposta_str = input(f"A imagem exibida é {Colors.YELLOW}(1) Real{Colors.RESET} ou {Colors.YELLOW}(2) AI{Colors.RESET}? (0 para sair): ").strip()
                if resposta_str not in ['0', '1', '2']:
                    print(f"{Colors.RED}Comando não reconhecido. Refaça a entrada.{Colors.RESET}")
                    continue
                break

            resposta_usuario = int(resposta_str)

            if resposta_usuario == 0:
                print(f"\n{Colors.YELLOW}Encerrando o loop de eventos...{Colors.RESET}")
                break

            palpite_convertido = 0 if resposta_usuario == 1 else 1
            tentativas += 1

            if palpite_convertido == label_num:
                acertos += 1
                print(f"{Colors.GREEN}✨ Correto! A origem é {label_texto}.{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ Falso positivo/negativo. A origem era {label_texto}.{Colors.RESET}")

            imprimir_placar(acertos, tentativas)

        # Trata o esgotamento do dataset (EOF no stream)
        except StopIteration:
            print(f"{Colors.YELLOW}O buffer de dados chegou ao fim.{Colors.RESET}")
            break
        # Tratamento seguro para sinais de interrupção (SIGINT)
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}Processo interrompido manualmente.{Colors.RESET}")
            break
        except Exception as e:
            print(f"\n{Colors.RED}Exceção detectada no tempo de execução: {e}{Colors.RESET}")
            break

        # O bloco 'finally' assegura a execução de operações de limpeza (Garbage Collection de I/O)
        # independentemente de a iteração ter tido sucesso, falha ou interrupção sistêmica.
        finally:
            if caminho_arquivo_temporario and os.path.exists(caminho_arquivo_temporario):
                try:
                    os.remove(caminho_arquivo_temporario)
                except OSError as e:
                    print(f"{Colors.RED}Falha ao realizar a exclusão atômica de {caminho_arquivo_temporario}: {e}{Colors.RESET}")

    # Processamento analítico final
    taxa_acerto = (acertos / tentativas * 100) if tentativas > 0 else 0
    print(f"\n{Colors.GREEN}Estatísticas finais da sessão: {acertos} acertos em {tentativas} requisições (Precisão: {taxa_acerto:.1f}%).{Colors.RESET}\n")

if __name__ == "__main__":
    main()
