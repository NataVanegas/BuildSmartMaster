$(function () {
  // Function to load modal content
  var loadForm = function () {
      var btn = $(this);
      $.ajax({
          url: btn.attr("data-url"),
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
              $("#modal-placeholder").html("");
          },
          success: function (data) {
              $("#modal-placeholder").html(data.html_form);
              $("#materialModal").modal("show");
          }
      });
  };

  // Function to save form data
  var saveForm = function () {
      var form = $(this);
      $.ajax({
          url: form.attr("action"),
          data: form.serialize(),
          type: form.attr("method"),
          dataType: 'json',
          success: function (data) {
              if (data.form_is_valid) {
                  $("#material-table tbody").html(data.html_material_list);  // Update the table
                  $("#materialModal").modal("hide");  // Hide the modal
              } else {
                  $("#modal-placeholder").html(data.html_form);  // Re-render the form with errors
              }
          }
      });
      return false;  // Prevent default form submission
  };

  // Bind the functions to the buttons
  $(".js-create-material").click(loadForm);
  $("#modal-placeholder").on("submit", ".js-material-form", saveForm);
});
