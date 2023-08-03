import mysql.connector


try:
    conexión = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database='proyecto'
    )
    #IMPORTANTE: poner en PASSWORD = '' la contraseña que tengan en su base de datos.

    cursor = conexión.cursor()

    leyes = [
        (20774, "1974-09-29", "Esta ley regula las relaciones laborales entre empleadores y empleados en el país. Establece los derechos y obligaciones laborales, abarcando temas como contratación, remuneración, horarios, vacaciones, licencias y protección laboral. Su objetivo es proteger los derechos de los trabajadores y promover condiciones laborales justas y equitativas.", "Laboral.", "Nacional.", "Congreso de la Nación.", """Teletrabajo, Trabajo remoto, Derechos laborales, Obligaciones laborales, Jornada laboral, Desconexión digital, Compensación de gastos, Salud y seguridad laboral Acuerdo de teletrabajo."""),
        (27555, "2020-07-14", "Esta ley establece los derechos y obligaciones tanto de los empleadores como de los trabajadores en el ámbito del teletrabajo. Aborda aspectos como la jornada laboral, la desconexión digital, la compensación de gastos y la protección de la salud y seguridad laboral. Su objetivo es garantizar condiciones justas y equitativas para los trabajadores que desempeñan sus labores de forma remota.", "Laboral", "Nacional", "Congreso de la nación", """Teletrabajo, Trabajo remoto, Derechos laborales, Obligaciones laborales, Jornada laboral, Desconexión digital, Compensación de gastos, Salud y seguridad laboral Acuerdo de teletrabajo."""),
        (7642, "1987-11-21", "Esta ley regula la práctica de la profesión de informática en la provincia de Córdoba, estableciendo requisitos y normas para los profesionales de este campo. Su objetivo es garantizar la calidad y el cumplimiento ético de los servicios informáticos en la región. Ademas de establecer entre los profesionales de Ciencias Informáticas una comunidad de intereses e ideales éticos, normativos y profesionales a fin de propender a su continuo perfeccionamiento.", "Derecho profesional", "Provincial", "Legislatura de Córdoba", """Matriculación, Ciencias Informaticas, Informatica, Ejercicio profesional, Titulos, Graduados, Ética, Profesional en Informatica, Deberes del profesional, Consejo, Tribunal de disciplina.""")
    ]

    query = "INSERT INTO leyes (nro_leyes, fecha, descripcion, categoria, jurisdiccion, or_legislativo, palabra_clave) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    cursor.executemany(query, leyes)

    
    conexión.commit()
    # a modo de comprobación  a la hora de subir nuestros datos, tenemos esta instancia
    #la misma nos dira si todo se subio correctamente o si de lo contrario algun tipo de error fue detectado

    print("Datos insertados correctamente.")
except mysql.connector.Error as error:
    print("Error al insertar datos en la base de datos:", error)
finally:
    if cursor:
        cursor.close()
    if conexión:
        conexión.close()
        
