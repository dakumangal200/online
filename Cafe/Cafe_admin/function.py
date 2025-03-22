def handle_uploaded_file(f):
    with open('Cafe_admin/static/assets/images/'+f.name,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)