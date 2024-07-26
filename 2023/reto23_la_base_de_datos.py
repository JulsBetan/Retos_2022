# /*
#  * Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente base de datos MySQL:
#  * - Host: mysql-5707.dinaserver.com
#  * - Port: 3306
#  * - User: mouredev_read
#  * - Password: mouredev_pass
#  * - Database: moure_test
#  * 
#  * Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
#  * - SELECT * FROM `challenges`
#  *
#  * Se pueden usar librerías para realizar la lógica de conexión a la base de datos.
#  */

import pymysql

config = {
    'user': 'mouredev_read',
    'password':  'mouredev_pass',
    'host': 'mysql-5707.dinaserver.com',
    'database': 'moure_test',
    'port': 3306
}

try:
    connection = pymysql.connect(**config)
    print("Conexion exitosa a la base de datos")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM challenges")

    results = cursor.fetchall()
    for row in results:
        print(row)

except pymysql.MySQLError as err:
    print(f"Error: {err}")
finally:
    connection.close()
    print("Conexion cerrada")
    