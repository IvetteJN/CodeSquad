import mysql.connector


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="proyecto",
            port=3307,
        )
        self.create_table()

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS leyes (
                id_leyes INT AUTO_INCREMENT PRIMARY KEY,
                nro_leyes INT NOT NULL,
                fecha DATE NOT NULL,
                descripcion VARCHAR(500) NOT NULL,
                categoria VARCHAR(20) NOT NULL,
                jurisdiccion VARCHAR(20) NOT NULL,
                or_legislativo VARCHAR(20) NOT NULL,
                palabra_clave VARCHAR(500) NOT NULL
            )
        """
        with self.conn.cursor() as cursor:
            cursor.execute(query)
        self.conn.commit()

    def insert_ley(
        self,
        nro_leyes,
        fecha,
        descripcion,
        categoria,
        jurisdiccion,
        or_legislativo,
        palabra_clave,
    ):
        query = "INSERT INTO leyes (nro_leyes, fecha, descripcion, categoria, jurisdiccion, or_legislativo, palabra_clave) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        with self.conn.cursor() as cursor:
            cursor.execute(
                query,
                (
                    nro_leyes,
                    fecha,
                    descripcion,
                    categoria,
                    jurisdiccion,
                    or_legislativo,
                    palabra_clave,
                ),
            )
        self.conn.commit()
        print("Ley agregada exitosamente.")

    def get_leyes(self):
        query = "SELECT id_leyes, nro_leyes, fecha, descripcion, categoria, jurisdiccion, or_legislativo, palabra_clave FROM leyes ORDER BY nro_leyes ASC"
        with self.conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(
                    f"ID: {row[0]}, Numero_ley: {row[1]}, Fecha: {row[2]}, Descripción: {row[3]}, Categoría: {row[4]}, Jurisdicción: {row[5]}, Organo_Legislativo: {row[6]}, Palabras_Clave: {row[7]}"
                )

    def update_ley_estado(
        self,
        nro_leyes,
        nueva_fecha,
        nueva_descripcion,
        nueva_categoria,
        nueva_jurisdiccion,
        nuevo_or_legislativo,
        nueva_palabra_clave,
    ):
        query = "UPDATE leyes SET fecha, descripcion, categoria, jurisdiccion, or_legislativo, palabra_clave = %s WHERE nro_ley = %s"
        with self.conn.cursor() as cursor:
            cursor.execute(
                query,
                (
                    nueva_fecha,
                    nueva_descripcion,
                    nueva_categoria,
                    nueva_jurisdiccion,
                    nuevo_or_legislativo,
                    nueva_palabra_clave,
                    nro_leyes,
                ),
            )
        self.conn.commit()
        print("Ley actualizada exitosamente.")

    def delete_ley(self, nro_leyes):
        query = "DELETE FROM leyes WHERE nro_leyes = %s"
        with self.conn.cursor() as cursor:
            cursor.execute(query, (nro_leyes,))
        self.conn.commit()
        print("Ley eliminada exitosamente.")
