fetch("http://localhost:5000/api/productos")
  .then(res => res.json())
  .then(data => {
    const contenedor = document.getElementById("productos");

    data.forEach(item => {
      const div = document.createElement("div");
      div.className = "producto";

      div.innerHTML = `
        <h3>${item.titulo}</h3>
        <p><span>${item.precio}</span></p>
        <p>Origen: ${item.origen}</p>
        <p>Fecha: ${item.fecha}</p>
      `;

      contenedor.appendChild(div);
    });
  })
  .catch(err => {
    console.error("Error al cargar los productos:", err);
  });
