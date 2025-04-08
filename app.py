from flask import Flask, render_template, request
import fdb
import uuid

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_SAMESITE='Lax'
)

def bd_cconnection():
    return fdb.connect(
    dsn='firebird3-engine:cencaico',
    user='SYSDBA',
    password='MyPass123',
    charset='UTF8'
)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about-us")
def aboutus():
    return render_template('about-us.html')

@app.route("/courses")
def courses():
    return render_template('courses.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/catalog")
def catalog():
    return render_template('catalog.html')

@app.route("/reclamaciones")
def ldr():
    return render_template('ldr.html')

@app.route("/politicas")
def politicas():
    return render_template('politicas.html')

@app.route("/condiciones")
def condiciones():
    return render_template('condiciones.html')

@app.errorhandler(404)
def error_handler(e):
    return render_template('404.html'), 404

@app.route("/reclamo", methods=["GET","POST"])
def reclamo():
    if request.method == "POST":
        id_str = str(uuid.uuid4()) 
        id_ = id_str.upper()

        data = [
            id_,
            request.form.get("nombre"),
            request.form.get("apellidos"),
            request.form.get("domicilio"),
            request.form.get("dni"),
            request.form.get("phone"),
            request.form.get("email"),
            request.form.get("parents"),
            request.form.get("tipo_bien"),
            int(request.form.get("monto")),
            request.form.get("mdescription"),
            request.form.get("tipo_detalle"),
            request.form.get("detalle"),
            request.form.get("pedido"),
            request.form.get("declaracion")
        ]

        print(data)
        con = bd_cconnection()
        cur = con.cursor()
        cur.execute(
            """INSERT INTO RECLAMACIONES (ID, RNAME, SNAME, DOMICILIO, DNI, PNUMBER, EMAIL, PARENTS, BIEN, MONTO, DESCRIPTION, RECLAMOQUEJA, DETALLE, PEDIDO, DECLARACION)
            VALUES (CHAR_TO_UUID(?), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, data)
        
        con.commit()
        con.close()
    return "Formulario recibido"

@app.route('/melamina-arequipa')
def melamina_arequipa():
    return render_template('melamina_lp.html')

@app.route('/guardar-melamina', methods=['POST'])
def guardar_datos_melamina():
    id_str = str(uuid.uuid4()) 
    id_ = id_str.upper()
    nombre  = request.form.get('nombre')
    numero = request.form.get('numero')
    rubro = request.form.get('rubro')
    disponibilidad = request.form.get('disponibilidad')
    inicio_curso = request.form.get('inicio-curso')
    costos = request.form.get('costos')

    data = [
        id_,
        nombre,
        numero,
        rubro,
        disponibilidad,
        inicio_curso,
        costos
    ]

    try:
        con = bd_cconnection()
        cur = con.cursor()
        cur.execute("""
        INSERT INTO LPMELAMINA (ID, CNAME, NUMERO, RUBRO, DISPONIBILIDAD, INICIOCURSO, COSTOS)
        VALUES (CHAR_TO_UUID(?), ?, ?, ?, ?, ?, ?);
        """, data)
        con.commit()
        con.close()
        return '', 200
    except Exception as e:
        print("Error al guardar los datos: ", e)
        return 'Error', 200

@app.route('/drywall-arequipa')
def drywall_arequipa():
    return render_template('drywall_lp.html')

@app.route('/guardar-drywall', methods=['POST'])
def guardar_datos_drywall():
    id_str = str(uuid.uuid4()) 
    id_ = id_str.upper()
    nombre  = request.form.get('nombre')
    numero = request.form.get('numero')
    rubro = request.form.get('rubro')
    disponibilidad = request.form.get('disponibilidad')
    inicio_curso = request.form.get('inicio-curso')
    costos = request.form.get('costos')

    data = [
        id_,
        nombre,
        numero,
        rubro,
        disponibilidad,
        inicio_curso,
        costos
    ]

    try:
        con = bd_cconnection()
        cur = con.cursor()
        cur.execute("""
        INSERT INTO LPDRYWALL (ID, CNAME, NUMERO, RUBRO, DISPONIBILIDAD, INICIOCURSO, COSTOS)
        VALUES (CHAR_TO_UUID(?), ?, ?, ?, ?, ?, ?);
        """, data)
        con.commit()
        con.close()
        return '', 200
    except Exception as e:
        print("Error al guardar los datos: ", e)
        return 'Error', 200


@app.route('/porcelanato-arequipa')
def porcelanato_arequipa():
    return render_template('porcelanato_lp.html')

@app.route('/guardar-porcelanato', methods=['POST'])
def guardar_datos_porcelanato():
    id_str = str(uuid.uuid4()) 
    id_ = id_str.upper()
    nombre  = request.form.get('nombre')
    numero = request.form.get('numero')
    rubro = request.form.get('rubro')
    disponibilidad = request.form.get('disponibilidad')
    inicio_curso = request.form.get('inicio-curso')
    costos = request.form.get('costos')

    data = [
        id_,
        nombre,
        numero,
        rubro,
        disponibilidad,
        inicio_curso,
        costos
    ]

    try:
        con = bd_cconnection()
        cur = con.cursor()
        cur.execute("""
        INSERT INTO LPPORCELANATO (ID, CNAME, NUMERO, RUBRO, DISPONIBILIDAD, INICIOCURSO, COSTOS)
        VALUES (CHAR_TO_UUID(?), ?, ?, ?, ?, ?, ?);
        """, data)
        con.commit()
        con.close()
        return '', 200
    except Exception as e:
        print("Error al guardar los datos: ", e)
        return 'Error', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)