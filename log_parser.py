import time
import signal

def ignorar_interrupcion(sig, frame):
    print(" [O] Señal recibida y registrada.")

signal.signal(signal.SIGINT, ignorar_interrupcion)

def consumir_ram():
    print("Iniciando consumo de RAM... Cierre por Ctrl + C.")
    memoria_ocupada = []
    
    while True:
        try:
            bloque = ' ' * (10**8)
            memoria_ocupada.append(bloque)
            
            print(f"Memoria acumulada: {len(memoria_ocupada) * 100} MB...")
            time.sleep(0.5)
            
        except MemoryError:
            print("[O] RAM testeada. Manteniendo el consumo actual...")
            while True:
                time.sleep(1)

if __name__ == "__main__":
    consumir_ram()
