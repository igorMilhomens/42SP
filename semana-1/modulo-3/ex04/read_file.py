import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path_file = sys.argv[1]
        try:
            with open(path_file, "r") as arquivo:
                conteudo = arquivo.read()
            print(conteudo)
        except FileNotFoundError:
            print("Erro: Arquivo não encontrado.")
        except IsADirectoryError:
            print("Erro: O argumento enviado é um diretório.")
        except Exception as e:
            print(f"Erro inesperado: {type(e).__name__}")
    else:
        print("Erro: Parametro Vazio")
