
// Example JS code to add functionality to folder list view
const folders = document.querySelectorAll('.folder');
folders.forEach(folder => {
    folder.addEventListener('click', e => {
        e.preventDefault();
        const folderId = folder.getAttribute('data-id');
        fetch(`/folder/${folderId}`)
            .then(res => res.json())
            .then(data => {
                const folderDetailContainer = document.querySelector('#folder-detail-container');
                folderDetailContainer.innerHTML = '';
                data.files.forEach(file => {
                    const fileNode = document.createElement('li');
                    fileNode.innerText = file.name;
                    folderDetailContainer.appendChild(fileNode);
                });
            });
    });
});

document.getElementById('file').addEventListener('change', handleFileSelect, false);

function handleFileSelect(evt) {
    var files = evt.target.files; // FileList object
    var output = [];
    for (var i = 0, f; f = files[i]; i++) {
        // Only process image files.
        if (!f.type.match('image.*')) {
            continue;
        }
        var reader = new FileReader();
        // Closure to capture the file information.
        reader.onload = (function(theFile) {
            return function(e) {
                // Render thumbnail.
                var span = document.createElement('span');
                span.innerHTML = ['<img class="thumb" src="', e.target.result,
                                  '" title="', escape(theFile.name), '"/>'].join('');
                document.getElementById('list').insertBefore(span, null);
            };
        })(f);
        // Read in the image file as a data URL.
        reader.readAsDataURL(f);
    }
}


document.getElementById('files').addEventListener('change', handleFileSelect, false);

function handleFileSelect(event) {
  var files = event.target.files;
  var output = document.getElementsByClassName('upload-list')[0];
  var fileList = "";
  for (var i = 0; i < files.length; i++) {
    fileList += "<tr><td>" + files[i].name + "</td><td>" + files[i].type + "</td><td>" + files[i].size + "</td></tr>";
  }
  output.innerHTML = "<table><thead><tr><th>File name</th><th>File format</th><th>File size</th></tr></thead><tbody>" + fileList + "</tbody></table>";
}
