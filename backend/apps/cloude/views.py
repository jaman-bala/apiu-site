from django.shortcuts import render, redirect
from .forms import CreateFolderForm, UploadFileForm
from .models import Folder, File
from django import forms

MAX_FILE_SIZE = 10485760 # 10MB

def create_folder(request):
    if request.method == 'POST':
        form = CreateFolderForm(request.POST)
        if form.is_valid():
            folder = Folder(name=form.cleaned_data['name'], user=request.user)
            folder.save()
        return redirect('folder_list')

    else:
        form = CreateFolderForm()
        return render(request, 'cloude/create_folder.html', {'form': form})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file', [])
            if len(files) > 0:
                for f in files:
                    file = File(name=f.name, file=f, folder=form.cleaned_data['folder'])
                    file.save()
                return redirect('folder_detail', folder_id=file.folder.id)
            else:
                form.add_error('file', 'No files were selected')

    else:
        form = UploadFileForm()
    return render(request, 'cloude/upload_file.html', {'form': form})


def folder_list(request):
    folders = Folder.objects.filter(user=request.user)
    return render(request, 'cloude/folder_list.html', {'folders': folders})

def folder_detail(request, folder_id):
    folder = Folder.objects.get(id=folder_id)
    files = File.objects.filter(folder=folder)
    return render(request, 'cloude/folder_detail.html', {'folder': folder, 'files': files})
