
export function cargarProductos() {
    fetch('http://127.0.0.1:5000/api/productos')
        .then(response => response.json())
        .then(data => {
            console.log("Productos obtenidos:", data);  // Verificación de los datos recibidos
            const listaProductos = document.getElementById('productos-lista');
            listaProductos.innerHTML = '';  // Limpiar la lista antes de agregar nuevos productos

            data.forEach(producto => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <strong>${producto.titulo}</strong><br>
                    Precio: ${producto.precio}<br>
                    <a href="${producto.url}" target="_blank">Ver producto</a>
                `;
                listaProductos.appendChild(li);
            });
        })
        .catch(error => console.error('Error al cargar productos:', error));
}
