from django.shortcuts import render
from django.http import HttpResponse

def Form(request):
    return render(request, "fichier/upload.html", {})

def Upload(request):
    for count, x in enumerate(request.FILES.getlist("files")):
        def process(f):
            with open('media/file_' + str(count), 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        process(x)
    return HttpResponse("File(s) uploaded!")