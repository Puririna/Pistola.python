import time

def operaçao_lenta():
    time.sleep(2)
    return "Operação concluída"

inicio = time.time()
resultado = operaçao_lenta()
fim = time.time()

print(f"Tempo de execução: {fim - inicio} segundos")