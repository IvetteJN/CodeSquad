from conexion import Database


class Leyes:
    def __init__(self):
        self.db = Database()

    def run(self):
        while True:
            print("\n--- Menú ---")
            print("1. Agregar ley")
            print("2. Mostrar leyes")
            print("3. Actualizar estado de ley")
            print("4. Eliminar ley")
            print("5. Salir")
            choice = input("Ingrese la opción deseada: ")

            if choice == "1":
                nro_leyes = int(input("Ingrese el número de la ley: "))
                fecha = input("Ingrese la fecha: ")
                descripcion = input("Ingrese la descripción: ")
                categoria = input("Ingrese la categoría: ")
                jurisdiccion = input("Ingrese la jurisdicción: ")
                or_legislativo = input("Ingrese el órgano legislativo: ")
                palabra_clave = input("Ingrese palabras clave: ")
                self.db.insert_ley(
                    nro_leyes,
                    fecha,
                    descripcion,
                    categoria,
                    jurisdiccion,
                    or_legislativo,
                    palabra_clave,
                )
            elif choice == "2":
                self.db.get_leyes()
            elif choice == "3":
                nro_leyes = int(input("Ingrese el número de la ley a actualizar: "))
                nueva_fecha = input("Ingrese la fecha: ")
                nueva_descripcion = input("Ingrese la descripción: ")
                nueva_categoria = input("Ingrese la categoría: ")
                nueva_jurisdiccion = input("Ingrese la jurisdicción: ")
                nuevo_or_legislativo = input("Ingrese el órgano legislativo: ")
                nueva_palabra_clave = input("Ingrese palabras clave: ")
                self.db.update_ley_estado(
                    nro_leyes,
                    nueva_fecha,
                    nueva_descripcion,
                    nueva_categoria,
                    nueva_jurisdiccion,
                    nuevo_or_legislativo,
                    nueva_palabra_clave,
                )
            elif choice == "4":
                nro_leyes = int(input("Ingrese el número de la ley a eliminar: "))
                self.db.delete_ley(nro_leyes)
            elif choice == "5":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")


if __name__ == "__main__":
    leyes_program = Leyes()
    leyes_program.run()
