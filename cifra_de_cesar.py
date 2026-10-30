# =======================================================
# ALUNA: Sara Ellen Matias da Silva
# ATIVIDADE PRÁTICA: Cifra de César no Python
# =======================================================

# Passo 1 e Desafio Final: Função principal da Cifra de César
def cifra_de_cesar(texto, chave_deslocamento):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""
    texto = texto.lower()  # Padroniza tudo em letras minúsculas
    
    for letra in texto:
        if letra in alfabeto:
            # Encontra a posição, soma a chave e usa % 26 para não estourar o alfabeto
            posicao = (alfabeto.find(letra) + chave_deslocamento) % 26
            resultado += alfabeto[posicao]
        else:
            # Mantém espaços, números e pontuações intactos
            resultado += letra
            
    return resultado

# === ÁREA DE TESTES E EXECUÇÃO ===

# Teste 1: Cifrando a frase do desafio (Chave 5)
frase_teste = "python eh divertido"
print("--- TESTE 1: CRIPTOGRAFIA ---")
print("Frase Original:", frase_teste)
print("Frase Cifrada: ", cifra_de_cesar(frase_teste, 5))
print("-" * 30)

# Resposta da Pergunta de Reflexão: Descriptografando com chave -3
mensagem_recebida = "rod pxpgr"  # Esse é o código de "ola mundo"
mensagem_original = cifra_de_cesar(mensagem_recebida, -3)

print("--- TESTE 2: DESCRIPTOGRAFIA (RESPOSTA DA PERGUNTA) ---")
print("Mensagem Cifrada Recebida:", mensagem_recebida)
print("Mensagem Original Decifrada:", mensagem_original)
print("-" * 30)