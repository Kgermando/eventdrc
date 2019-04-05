from django.contrib import admin

from eventApp.models import Logo_Client, Recent_Travail, Category, Presentation, About_manager, About_porfolio, About_text, Manager_say
# Register your models here.
admin.site.site_header = 'EVENT ADMINISTRATION'

admin.site.register(Logo_Client)
admin.site.register(Recent_Travail)
admin.site.register(Category)
admin.site.register(About_manager)
admin.site.register(About_porfolio)
admin.site.register(About_text)
admin.site.register(Presentation)
admin.site.register(Manager_say)
