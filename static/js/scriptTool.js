// $(document).ready(function(){
//     // Abrir el modal para crear/editar tool
//     $('.openToolModal').click(function(event){
//         event.preventDefault();
//         var url = $(this).data('url');
        
//         // Realizar la petición AJAX para obtener el formulario
//         $.ajax({
//             url: url,
//             success: function(data){
//                 // Insertar el formulario en el cuerpo del modal
//                 $('#toolModal .modal-body').html(data.html_form);
//                 // Mostrar el modal
//                 $('#toolModal').modal('show');
//             }
//         });
//     });

//     // Manejar el envío del formulario desde el modal
//     $('#toolModal').on('submit', 'form', function(event){
//         event.preventDefault();
//         var form = $(this);
//         var formData = new FormData(this);
        
//         // Realizar la petición AJAX para guardar el tool
//         $.ajax({
//             url: form.attr('action'),
//             type: form.attr('method'),
//             data: formData,
//             contentType: false,
//             processData: false,
//             success: function(data){
//                 if (data.form_is_valid) {
//                     // Si el formulario es válido, cerrar el modal y actualizar la página o lista
//                     $('#toolModal').modal('hide');
//                     location.reload(); // Recargar la página o actualizar la lista de tools
//                 } else {
//                     // Si hay errores de validación, mostrar el formulario actualizado con los errores
//                     $('#toolModal .modal-body').html(data.html_form);
//                 }
//             },
//             error: function(xhr, textStatus, errorThrown){
//                 console.log('Error al enviar el formulario:', errorThrown);
//                 // Manejar errores de la petición AJAX aquí si es necesario
//             }
//         });
//     });
// });
