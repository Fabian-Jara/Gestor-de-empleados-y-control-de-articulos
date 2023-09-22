$(document).ready(function () {
    $('#tablaUser').DataTable({
        language: {
            url: "https://cdn.datatables.net/plug-ins/1.13.2/i18n/es-ES.json"
        },
        responsive: true,
    });
});

$(document).ready(function () {
    $('#tabla_Paginas').DataTable({
        language: {
            url: "https://cdn.datatables.net/plug-ins/1.13.2/i18n/es-ES.json"
        },
        responsive: true,
    });
});

$(document).ready(function () {
    $('#tabla_carrusel').DataTable({
        language: {
            url: "https://cdn.datatables.net/plug-ins/1.13.2/i18n/es-ES.json"
        },
        responsive: true,
    });
});

$(document).ready(function () {
    $('#tabla_Empleados').DataTable({
        language: {
            url: "https://cdn.datatables.net/plug-ins/1.13.2/i18n/es-ES.json"
        },
        responsive: true,
    });
});

$(document).ready(function () {
    $('#tabla_Noticias').DataTable({
        language: {
            url: "https://cdn.datatables.net/plug-ins/1.13.2/i18n/es-ES.json"
        },
        responsive: true,
    });
});

$(document).ready(function () {
    var fecha = new Date();
	var fechaActual = fecha.getDate() + " de " + fecha.toLocaleString('default', { month: 'long' }) + " de " + fecha.getFullYear();
    var nombrePDF = "Reporte Inventario " + fechaActual
    $('#tabla_Inventario').DataTable({
        language: {
            url: "https://cdn.datatables.net/plug-ins/1.13.2/i18n/es-ES.json"
        },
        responsive: true,
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                exportOptions: {
                    columns: [2, 3, 4, 5, 6, 7, 8]
                },
                className: 'btn btn-success',
                filename: nombrePDF
            }
        ],
        order: [[1, 'asc']]
    });
});