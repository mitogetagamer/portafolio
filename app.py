
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('FLASK_SECRET_KEY', '2211')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

@app.route("/")
def index():
    return render_template('index.html')  # Asegúrate de tener este archivo en 'templates/'

@app.route('/send_email', methods=['POST'])
def send_email(): 
    try: 
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        mensaje = request.form["mensaje"]

        # Comprobar que los campos no estén vacíos
        if not nombre or not correo or not mensaje:
            flash("Todos los campos son obligatorios", "error")
            return redirect(url_for('index'))

        msg = Message("Nuevo mensaje de contacto",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[app.config['MAIL_USERNAME']])
        msg.body = f"Nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}"

        mail.send(msg)
        flash("Mensaje enviado con éxito", "success")
    except Exception as e:
        print(f"Error: {e}")
        flash(f"Error al enviar el mensaje: {e}", "error")

    return render_template('index.html')  # Asegúrate de tener este archivo en 'templates/'

if __name__ == "__main__":
    app.run(debug=True)











































