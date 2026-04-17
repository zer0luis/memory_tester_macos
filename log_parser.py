import time

def consumir_ram():
    print("Iniciando consumo de RAM... Presiona Ctrl + C para detener.")
    memoria_ocupada = []
    
    try:
        while True:
            bloque = ' ' * (10**8) 
            memoria_ocupada.append(bloque)
            
            print(f"Consumo aproximado: {len(memoria_ocupada) * 100} MB añadidos...")
            
            
            time.sleep(0.5) 
            
    except KeyboardInterrupt:
        print("\n[!] Interrupción detectada. Liberando memoria y saliendo...")
        
        memoria_ocupada.clear()
    except MemoryError:
        print("\n[O] Programa finalizado exitosamente.")

if __name__ == "__main__":
    consumir_ram()
