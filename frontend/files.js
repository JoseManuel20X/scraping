// files.js

// Función para cargar los archivos
export function cargarArchivos() {
    fetch('http://127.0.0.1:5000/api/archivos')
        .then(response => response.json())
        .then(data => {
            console.log("Archivos obtenidos:", data);  // Verificación de los archivos
            const listaArchivos = document.getElementById('archivos-lista');
            listaArchivos.innerHTML = '';  // Limpiar la lista antes de agregar nuevos archivos

            data.forEach(archivo => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <strong>${archivo.nombre}</strong><br>
                    <a href="${archivo.url}" target="_blank">Ver archivo</a><br>
                    Hash: ${archivo.hash}
                `;
                listaArchivos.appendChild(li);
            });
        })
        .catch(error => console.error('Error al cargar archivos:', error));
}
