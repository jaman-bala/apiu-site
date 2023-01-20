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