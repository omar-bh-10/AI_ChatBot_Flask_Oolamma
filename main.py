from flask import Flask, render_template, request, jsonify
import requests
import PyPDF2
import docx

app = Flask(__name__)

OOLAMA_URL = "http://localhost:11434/api/chat"


# ====== Extraction PDF ======
def extract_text_from_pdf(file_stream):
    reader = PyPDF2.PdfReader(file_stream)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


# ====== Extraction DOCX ======
def extract_text_from_docx(file_stream):
    document = docx.Document(file_stream)
    text = "\n".join([p.text for p in document.paragraphs])
    return text


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    # Récupération du texte
    user_message = request.form.get("message", "")

    # Récupération du fichier
    uploaded_file = request.files.get("file")

    extracted_text = ""

    # ====== Analyse du fichier ======
    if uploaded_file:
        filename = uploaded_file.filename.lower()

        if filename.endswith(".pdf"):
            extracted_text = extract_text_from_pdf(uploaded_file)

        elif filename.endswith(".docx"):
            extracted_text = extract_text_from_docx(uploaded_file)

        elif filename.endswith(".txt"):
            extracted_text = uploaded_file.read().decode("utf-8")

        else:
            return jsonify({"reponse": "❌ Format non supporté. Utilise PDF, DOCX ou TXT."})

    # ====== Construction du prompt ======
    if extracted_text:
        prompt = f"Résume ce document :\n\n{extracted_text}"

    else:
        prompt = user_message

    # ====== Envoi à Mistral via Ollama ======
    payload = {
        "model": "mistral",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    response = requests.post(OOLAMA_URL, json=payload)
    result = response.json()

    bot_response = result["message"]["content"]

    return jsonify({"reponse": bot_response})


if __name__ == "__main__":
    app.run(debug=True)
