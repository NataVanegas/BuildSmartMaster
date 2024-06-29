$(document).ready(function() {
    $('#searchButton').click(function() {
      var query = $('#searchInput').val().trim();
      
      if (query !== '') {
        console.log("llega aqui");
        $.ajax({
          type: 'GET',
          url: '{% url "materials:search_materials" %}',
          data: {
            query: query
          },
          success: function(data) {
            $('.card-material').html(data);
          },
          error: function(xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
          }
        });
      }
    });
  });