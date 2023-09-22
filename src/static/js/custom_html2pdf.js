document.addEventListener("DOMContentLoaded", () => {
    // Escuchamos el click del botón
    const $boton = document.querySelector("#btnCrearPdf");
    $boton.addEventListener("click", () => {
        const $elementoParaConvertir = document.body; // <-- Aquí puedes elegir cualquier elemento del DOM
        var fecha = new Date();
		var fechaActual = fecha.getDate() + " de " + fecha.toLocaleString('default', { month: 'long' }) + " de " + fecha.getFullYear();
        var nombrePDF = "Reporte Inventario " + fechaActual + ".pdf"
        html2pdf()
            .set({
                margin: 1,
                filename: nombrePDF,
                image: {
                    type: 'jpeg',
                    quality: 0.98
                },
                html2canvas: {
                    scale: 3, // A mayor escala, mejores gráficos, pero más peso
                    letterRendering: true,
                },
                jsPDF: {
                    unit: "in",
                    format: "a3",
                    orientation: 'portrait' // landscape o portrait
                }
            })
            .from($elementoParaConvertir)
            .save()
            .catch(err => console.log(err));
    });
});