from flask import Flask, render_template, request, redirect, url_for, flash
from ausdruck import Ausdruck

app = Flask(__name__)
app.secret_key = "Hallo_peterchen"
heutige_nominierungen = []

@app.route('/')
def home():
    ausdruck="Halunke"
    return render_template("index.html", ausdruck=ausdruck)

@app.route('/nominierungen')
def nominierungen():
    ausdruck = request.args.get('ausdruck')
    heutige_nominierungen.sort()
    heutige_nominierungen.reverse()
    return render_template('nominierungen.html', ausdruck=ausdruck, nominierungsliste=heutige_nominierungen)

@app.route('/abstimmung', methods=["POST", "GET"])
def abstimmen():
    # Diese Methode wird entweder per Get oder Post aufgerufen.
    # Get wenn einfach die entsprechende URL eingegeben wird
    # Post wenn ein Abstimmungsbutton geklickt wurde
    if request.method == "POST":

        # Erhalte den ausdruck der gewählt wurde
        gewaehlter_ausdruck = request.form["ausdruck"]
        
        # Inkrementiere den likes counter
        for ausdruck in heutige_nominierungen:
            if ausdruck.ausdruck == gewaehlter_ausdruck:
                ausdruck.like_hinzufuegen()

                # flashe eine Nachricht, die in nominierung.hmtl dann auferufen wird
                nachricht=f'Supi, du hast erfolgreich für "{ausdruck.ausdruck}" abgestimmt!'
                flash(nachricht)

        return redirect(url_for("nominierungen", ausdruck=gewaehlter_ausdruck))
    else:
        return render_template('abstimmung.html', nominierungsliste=heutige_nominierungen)

@app.route('/nominierungsformular', methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        nominierter_ausdruck = request.form["nm"]
        neuer_ausdruck = Ausdruck(ausdruck=nominierter_ausdruck)
        heutige_nominierungen.append(neuer_ausdruck)
        nachricht=f'Fantastisch, du hast "{nominierter_ausdruck}" zum Ausdruck des Tages nominiert!'
        flash(nachricht)
        return redirect(url_for("nominierungen", ausdruck=nominierter_ausdruck))
    else:
        return render_template('nominierungsformular.html')

if __name__ == '__main__':
    app.run(debug=True)