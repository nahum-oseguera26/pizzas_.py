bienvenidos a pizzas nahum

pizzas=["pepperoni", "hawaiana", "queso", "champiñones"]

def imprimir_menu():
    print("1 mostrar pizzas")
    print("2 eliminar pizzas")
    print("3 agregar pizzas")
    print("4 salir")
    valor = input("ingrese el valor a la accion:")
    return valor

continuar = true

while continuar:
    #v_retornado = valor retornado
    v_retornado = imprimir_menu()
    if int(v_retornado) == 1:
        for pizzas in pizzas:
            print(pizzas)
        elif int(v_retornado) == 2:
            pizzas = 
        elif int(v_retornado) == 3:
            valor = input("ingrese el pizzas a agregar")
            pizzas.append(valor)
        elif int(v_retornado) == 4:
            continuar = false
            else:
                print("opcion no controlada")
            
            
