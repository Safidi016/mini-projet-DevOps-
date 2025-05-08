from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Données de login 
users = {
    "admin": "password123"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Vérifier les informations de login
        if username in users and users[username] == password:
            return redirect(url_for("welcome"))
        else:
            return "Échec de la connexion. Vérifiez vos identifiants."

    return render_template("login.html")

@app.route("/welcome")
def welcome():
    return "<h1>Bienvenue sur le site, vous êtes connecté !</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
