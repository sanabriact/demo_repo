print("bueno bro, perdon por tener menos iq")
import sys

def preguntar():
    while True:
        respuesta = input("¿va  a hablarle a la niña? (si/no): ").lower().strip()
        
        if respuesta == "no":
            # Repite el mensaje 100 veces
            for i in range(1, 101):
                print(f"{i}: ¡gay!")
            print("\n--- ¡Bucle terminado! Intentémoslo de nuevo. ---\n")
            
        elif respuesta == "si":
            print("Entendido. Cerrando el programa... ¡Adiós!")
            sys.exit() # Cierra el programa por completo
            
        else:
            print("Por favor, responde solo con 'si' o 'no'.")

if __name__ == "__main__":
    preguntar()