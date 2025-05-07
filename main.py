from flask import Flask,request,render_template

app=Flask(__name__)

if __name__=="main":
    app.run(debug=True)

    @app.route('/buscar')
    def buscar():
     producto = request.args.get('producto')
     talla = request.args.get('tamano')
     color = request.args.get('color')
     if producto is None and talla is None and color is None:
        return "faltan datos"
     return f"Buscando {producto} de talla {talla} y color {color}"
    
@app.route("/registro", methods=["GET"])
def ruta_formulario():
    return render_template("formulario.html")


@app.route("/registro", methods=["POST"])
def ruta_registro():
    nombre=request.form.get("estudiante")
    email=request.form.get("correo")
    password=request.form.get("contrasena")
    return f"usuario registrado: {nombre}, {email}, {password}"
    
