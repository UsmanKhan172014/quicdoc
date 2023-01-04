from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
# from .forms import UploadFileForm
from .models import UploadFileForm
import docx
import os
import re


# define the home view
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        data = UploadFileForm.objects.create(name=request.POST['name'],
                                             description=request.POST['description'],
                                             file=file)
        data.save()
        return HttpResponseRedirect('/templatedocs/home/')

    else:
        form = UploadFileForm()
    return render(request, 'templatedocs/upload.html', {'form': form})


def index(request):
    data = UploadFileForm.objects.all()
    return render(request, 'templatedocs/index.html', {'data': data})


# delete function
def delete(request, id):
    data = UploadFileForm.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect('/templatedocs/get_all/')


def update_doc_form(request, id):
    data = UploadFileForm.objects.get(id=id)
    # baseurl = request.build_absolute_uri('/')
    basePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = basePath + "/media/" + str(data.file)
    doc = docx.Document(data.file)
    unique_placeholders = set()
    for para in doc.paragraphs:
        placeholders = re.findall(r"\{.*\}", para.text)
        unique_placeholders.update(placeholders)

    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    placeholders = re.findall(r"\{.*\}", para.text)
                    unique_placeholders.update(placeholders)

    unique_placeholders = list(unique_placeholders)
    return render(request, 'templatedocs/updateDoc.html', {'id': id, 'unique_placeholders': unique_placeholders})


def update(request, id):
    data = UploadFileForm.objects.get(id=id)
    if request.method == 'POST':
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        doc = docx.Document(data.file)
        try:
            for para in doc.paragraphs:
                placeholders = re.findall(r"\{.*\}", para.text)
                for placeholder in placeholders:
                    para.text = para.text.replace(placeholder, request.POST[placeholder])

            for table in doc.tables:
                for row in table.rows:
                    for cell in row.cells:
                        for para in cell.paragraphs:
                            placeholders = re.findall(r"\{.*\}", para.text)
                            for placeholder in placeholders:
                                para.text = para.text.replace(placeholder, request.POST[placeholder])

            doc.save(base_path + "/media/" + str(data.file))
            response = FileResponse(open(base_path + "/media/" + str(data.file), 'rb'),
                                    content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename="Hello.docx"'
            return response
        except Exception as e:
            print(e)
            return HttpResponse("Error")