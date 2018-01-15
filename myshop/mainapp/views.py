from django.shortcuts import render

def index_view(req):
    return render(req , 'mainapp/index.html')

def products_view(req):
    return render(req, 'mainapp/products.html')

def contact_view(req):
    return render (req, 'mainapp/contact.html')
