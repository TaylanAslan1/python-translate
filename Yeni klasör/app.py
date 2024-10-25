from flask import Flask, render_template, request, flash
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Flash mesajları için gerekli

@app.route("/", methods=["GET", "POST"])
def index():
    sonuc = ""
    if request.method == "POST":
        metin = request.form["metin"]
        hedef_dil = request.form["hedef_dil"]

        if hedef_dil not in LANGUAGES.keys():  # Geçerli dil kodu kontrolü
            flash("Geçersiz hedef dil kodu. Lütfen geçerli bir dil kodu girin.", "error")
            return render_template("index.html", sonuc=sonuc)

        translator = Translator()
        try:
            ceviri = translator.translate(metin, dest=hedef_dil)
            sonuc = ceviri.text
        except Exception as e:
            flash(f"Çeviri işlemi sırasında bir hata oluştu: {e}", "error")
    
    return render_template("index.html", sonuc=sonuc)

if __name__ == "__main__":
    app.run(debug=True)
