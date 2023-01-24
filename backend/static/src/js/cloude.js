document.addEventListener('DOMContentLoaded', function(){
  var input = document.getElementById('files');
  input.addEventListener('change', handleFileSelect);

  function handleFileSelect(event) {
    var files = event.target.files;
    var output = document.getElementsByClassName('upload-list')[0];
    var fileList = "";
    for (var i = 0; i < files.length; i++) {
      fileList += "<tr><td>" + files[i].name + "</td><td>" + files[i].type + "</td><td>" + files[i].size + "</td></tr>";
      }
      output.innerHTML = "<table><thead><tr><th>File name</th><th>File format</th><th>File size</th></tr></thead><tbody>" + fileList + "</tbody></table>";
      }
      });


$('ul li').on('click', function() {
    $('li').removeClass('active');
    $(this).addClass('active');
});

$(document).ready(function() {
  // Add a change event to the file input
  $("#file_input").change(function() {
  // Get the selected file name
  var fileName = $(this).val();
            // Show the selected file name
  $(this).siblings(".file-upload-text").text(fileName);
  });
});

var input = document.getElementById("id_file");
    var progressBar = document.getElementById("progress-bar");
    var percentage = document.getElementById("percentage");

    input.onchange = function() {
        var files = input.files;
        var formData = new FormData();
        for (var i = 0; i < files.length; i++) {
            formData.append('file', files[i]);
        }

        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'your_upload_url', true);
        xhr.onprogress = function(e) {
          if (e.lengthComputable) {
            var percentComplete = (e.loaded / e.total) * 100;
            progressBar.style.width = percentComplete + '%';
            percentage.innerHTML = percentComplete + '%';
          }
        }
        xhr.onload = function() {
          if (xhr.status === 200) {
          // Загрузка завершена
          }
          else {
          // Ошибка
          }
          };
          xhr.send(formData);
          
};
