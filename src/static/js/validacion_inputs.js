(function () {
    'use strict'

    //Obtiene todos los formularios a los que se le aplica la case .needs-validation
    var forms = document.querySelectorAll('.needs-validation')

    //Verifica si los campos están correctos, de lo contrario no se enviara el formulario
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }

                form.classList.add('was-validated')
            }, false)
        })
})()
