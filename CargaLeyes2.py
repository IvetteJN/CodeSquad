import mysql.connector


try:
    conexión = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="",
        database="proyecto",
    )
    # IMPORTANTE: poner en PASSWORD = "" la contraseña que tengan en su base de datos.

    cursor = conexión.cursor()

    leyes = [
        (
            26653,
            "2010-11-03",
            "Esta ley establece que todo sitio web público o privado en Argentina debe respetar las normas y requisitos de accesibilidad de la información, garantizando el acceso a personas con discapacidad y evitando cualquier forma de discriminación. La ley establece las obligaciones para el Estado nacional, organismos descentralizados, empresas estatales, empresas privadas concesionarias de servicios públicos y organizaciones de la sociedad civil que reciben subsidios o contrataciones con el Estado.",
            "Derecho informático",
            "Nacional",
            "Congreso de la Nación",
            """Accesibilidad de la información, páginas web, personas con discapacidad, igualdad de oportunidades, discriminación, ONTI, derechos de las personas con discapacidad.""",
        ),
        (
            23551,
            "1998-03-23",
            "Esta ley regula la organización y el funcionamiento de las asociaciones sindicales en Argentina. Establece los derechos y obligaciones de los sindicatos, los procedimientos para su constitución y reconocimiento, las condiciones para la representación de los trabajadores, la negociación colectiva, la resolución de conflictos laborales y las medidas de acción sindical, entre otros aspectos.",
            "Laboral",
            "Nacional",
            "Congreso de la Nación",
            """Asociaciones sindicales, sindicatos, derechos laborales, negociación colectiva, representación sindical, acción sindical.""",
        ),
        (
            26388,
            "2008-06-05",
            "Esta ley establece los delitos informáticos y las sanciones correspondientes en Argentina. Tiene como objetivo proteger la seguridad de los sistemas informáticos, prevenir y reprimir actividades ilícitas relacionadas con las tecnologías de la información y las comunicaciones. La ley aborda delitos como el acceso indebido a sistemas, sabotaje informático, fraude electrónico, falsificación de datos, entre otros.",
            "Derecho Informático",
            "Nacional",
            "Congreso de la Nación",
            """Delitos informáticos, ciberdelitos, seguridad informática, sanciones, acceso indebido, fraude electrónico, falsificación de datos.""",
        ),
        (
            24557,
            "1995-09-13",
            "Esta ley establece el régimen de prevención y reparación de los accidentes de trabajo y enfermedades profesionales en Argentina. Tiene como objetivo principal proteger a los trabajadores y garantizar la seguridad laboral, estableciendo los mecanismos de prevención de riesgos, la cobertura de las contingencias laborales, la responsabilidad de los empleadores y las prestaciones para los trabajadores damnificados.",
            "Laboral",
            "Nacional",
            "Congreso de la Nación",
            """Riesgos del trabajo, accidentes laborales, enfermedades profesionales, prevención, reparación, seguridad laboral.""",
        ),
    ]

    query = "INSERT INTO leyes (nro_leyes, fecha, descripcion, categoria, jurisdiccion, or_legislativo, palabra_clave) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    cursor.executemany(query, leyes)

    conexión.commit()
    # a modo de comprobación  a la hora de subir nuestros datos, tenemos esta instancia
    # la misma nos dira si todo se subio correctamente o si de lo contrario algun tipo de error fue detectado

    print("Datos insertados correctamente.")
except mysql.connector.Error as error:
    print("Error al insertar datos en la base de datos:", error)
finally:
    if cursor:
        cursor.close()
    if conexión:
        conexión.close()
