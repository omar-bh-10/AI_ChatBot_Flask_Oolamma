async function sendMessage() {

    const fileInput = document.getElementById("file-input");
    const file = fileInput.files[0];

    

    const input = document.getElementById("user-input");
    const message = input.value;

    if (message.trim() === "" && !file) {
        return;
    }

    const formData = new FormData();   // IMPORTANT : F majuscule
    formData.append("message", message);

    if (file) {
        formData.append("file", file);
    }

    const response = await fetch("/chat", {
        method: "POST",
        body: formData   // IMPORTANT : pas de headers
    });

    const data = await response.json();

    const chatBox = document.getElementById("chat-box");

    if (file) {
        chatBox.innerHTML += `<p>📎 Fichier : ${file.name}</p>`;
    }

    chatBox.innerHTML += `
        <p><strong>Vous :</strong> ${message || "(Analyse du fichier)"}</p>
        <p><strong>Assistant :</strong> ${data.reponse}</p>
        <hr>
    `;
    

    
    input.value = "";
    document.getElementById("file-preview").innerHTML = "";

    fileInput.value = "";
}

document.getElementById("file-input").addEventListener("change", function () {
    const file = this.files[0];
    const preview = document.getElementById("file-preview");

    if (file) {
        preview.innerHTML = `
            <div class="file-box">
                📎 ${file.name}
            </div>
        `;
    } else {
        preview.innerHTML = "";
    }
});

