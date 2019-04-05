from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from eventApp.models import Logo_Client, Recent_Travail, Category, Presentation, About_manager, About_porfolio, About_text, Manager_say

# Create your views here.
def index(request):
    logo_client_list = Logo_Client.objects.all()
    recent_travail_list = Recent_Travail.objects.all()
    # category_list = Category.objects.all()

    context = {
        'logo_client_list' : logo_client_list,
        'recent_travail_list': recent_travail_list,
        # 'category_list' : category_list,
    }

    template_name = 'eventapp/index.html'
    return render(request, template_name, context)


def contact(request):
    template_name = 'eventapp/contact.html'
    return render(request, template_name)


def about(request):
    about_manager_list = About_manager.objects.all()
    about_porfolio_list = About_porfolio.objects.all()
    about_text_list = About_text.objects.all()
    manager_list = Manager_say.objects.all()
    context = {
        'about_manager_list' : about_manager_list,
        'about_porfolio_list' : about_porfolio_list,
        'about_text_list' : about_text_list,
        'manager_list' : manager_list
    }
    template_name = 'eventapp/about.html'
    return render(request, template_name, context)


def presentation(request):
    ''' Vue for page presentation '''
    presentation_list = Presentation.objects.all()
    context = {
        "presentation_list" : presentation_list
    }
    template_name = 'eventapp/presentation.html'
    return render(request, template_name, context)
    
    
def details(request, id):
    '''Detail for page presentation  '''
    presentation = get_object_or_404(Presentation, id=id)
    context = {
        'presentation' : presentation
    }
    template_name = 'eventapp/details.html'
    return render(request, template_name, context)


def prix(request):
    template_name = 'eventapp/pricingbox.html'
    return render(request, template_name)

def handler404(request):
    return render(request, 'errors/404.html', {}, status=404)

def handler500(request):
    return render(request, 'errors/500.html', {}, status=500)

