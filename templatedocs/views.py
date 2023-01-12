from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
# from .forms import UploadFileForm
from .models import UploadFileForm
import docx
import os
import re
from pptx import Presentation


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
    return HttpResponseRedirect('/templatedocs/home/')


def update_doc_form(request, id):
    data = UploadFileForm.objects.get(id=id)
    # baseurl = request.build_absolute_uri('/')
    basePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = basePath + "/media/" + str(data.file)
    if ".docx" in file:
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
    elif ".pptx" in file:
        prs = Presentation(file)
        unique_placeholders = set()
        for slide in prs.slides:
            for shape in slide.shapes:
                if not shape.has_text_frame:
                    continue
                for paragraph in shape.text_frame.paragraphs:
                    placeholders = re.findall(r"\{.*\}", paragraph.text)
                    unique_placeholders.update(placeholders)
        unique_placeholders = list(unique_placeholders)
        # return HttpResponse(unique_placeholders)
        return render(request, 'templatedocs/updateDoc.html', {'id': id, 'unique_placeholders': unique_placeholders})
    else:
        return HttpResponse("File not supported")

def update(request, id):
    data = UploadFileForm.objects.get(id=id)
    if request.method == 'POST':
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if ".docx" in data.file.name:
            doc = docx.Document(data.file)

            try:
                for para in doc.paragraphs:
                    placeholders = re.findall(r"\{.*\}", para.text)
                    for placeholder in placeholders:
                        style1 = doc.styles['heading 1']
                        style2 = doc.styles['heading 2']
                        default_color = style2.font.color.rgb
                        if str(default_color) == 'FFFFFF':
                            para.text = para.text.replace(placeholder, request.POST[placeholder])
                            para.style.font.color.rgb = style1.font.color.rgb
                        else:
                            para.text = para.text.replace(placeholder, request.POST[placeholder])
                for table in doc.tables:
                    for row in table.rows:
                        for cell in row.cells:
                            for para in cell.paragraphs:
                                placeholders = re.findall(r"\{.*\}", para.text)
                                for placeholder in placeholders:
                                    style = para.style
                                    para.text = para.text.replace(placeholder, request.POST[placeholder])
                                    para.style = style

                doc.save(base_path + "/media/documents/updated.docx")
                response = FileResponse(open(base_path + "/media/documents/updated.docx", 'rb'),
                                        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                response['Content-Disposition'] = 'attachment; filename="Hello.docx"'
                return response
            except Exception as e:
                print(e)
                return HttpResponse(e)
        elif ".pptx" in data.file.name:
            prs = Presentation(base_path + "/media/" + str(data.file))
            try:
                for slide in prs.slides:
                    for shape in slide.shapes:
                        if not shape.has_text_frame:
                            continue
                        for paragraph in shape.text_frame.paragraphs:
                            placeholders = re.findall(r"\{.*\}", paragraph.text)
                            for placeholder in placeholders:
                                print(placeholder)
                                paragraph.text = paragraph.text.replace(placeholder, request.POST[placeholder])
                prs.save(base_path + "/media/documents/updated.pptx")
                response = FileResponse(open(base_path + "/media/documents/updated.pptx", 'rb'),
                                        content_type='application/vnd.openxmlformats-officedocument.presentationml.presentation')
                response['Content-Disposition'] = 'attachment; filename="Hello.pptx"'
                return response
                # return HttpResponse("Success")
            except Exception as e:
                print(e)
                return HttpResponse("Error")
        else:
            return HttpResponse("File not supported")
    else:
        return HttpResponseRedirect('/templatedocs/home/')
