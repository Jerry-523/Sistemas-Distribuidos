document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const downloadForm = document.getElementById('downloadForm');
    const fileList = document.getElementById('fileList');
    const downloadSelect = document.getElementById('downloadSelect');
    const downloadButton = document.getElementById('downloadButton');

    uploadForm.addEventListener('submit', function(event) {
        event.preventDefault();

        var fileInput = document.getElementById('fileInput');
        var file = fileInput.files[0];
        if (!file) {
            alert('Por favor, selecione um arquivo para enviar.');
            return;
        }

        var formData = new FormData();
        formData.append('file', file);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao enviar arquivo.');
            }
            return response.text();
        })
        .then(data => {
            alert(data);  
            updateFileList();
        })
        .catch(error => {
            alert('Erro ao enviar arquivo: ' + error.message); 
        });
    });

    downloadButton.addEventListener('click', function() {
        const selectedFile = downloadSelect.value;
        if (!selectedFile) {
            alert('Por favor, selecione um arquivo para baixar.');
            return;
        }

        window.location.href = `/download/${selectedFile}`;
    });

    function updateFileList() {
        fetch('/files')
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao listar arquivos.');
            }
            return response.json();
        })
        .then(data => {
            fileList.innerHTML = '';
            data.forEach(file => {
                const listItem = document.createElement('li');
                listItem.textContent = file;
                fileList.appendChild(listItem);
            });
        })
        .catch(error => {
            alert(error.message); 
        });
    }

    updateFileList();
});