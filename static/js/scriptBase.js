// $(function () {
//     // Function to load modal content
//     var loadForm = function () {
//         var btn = $(this);
//         $.ajax({
//             url: btn.attr("data-url"),
//             type: 'get',
//             dataType: 'json',
//             beforeSend: function () {
//                 $("#modal-placeholder").html("");
//             },
//             success: function (data) {
//                 $("#modal-placeholder").html(data.html_form);
//                 $("#materialModal").modal("show");
//             }
//         });
//     };

//     // Bind the function to the buttons that open the modal
//     $(".js-create-material").click(loadForm);
//     $(".js-update-material").click(loadForm);
// });

