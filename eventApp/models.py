from django.db import models

# Create your models here.
class Logo_Client(models.Model):
    ''' logo de nos clients '''
    lien = models.URLField(blank=True, help_text="lien")
    image_logo = models.ImageField(upload_to='logo_client', blank=True, help_text="width_field=310, height_field=120")

    def __str__(self):
        return self.lien


class Recent_Travail(models.Model):
    ''' les travails accomplie par EVENT '''
    title = models.CharField(max_length=50)
    image_title = models.ImageField(upload_to='recent_travail', blank=True, help_text=" width_field=900, height_field=632")
    image_travail = models.ImageField(upload_to='recent_travail', blank=True, help_text="width_field=900, height_field=632")
    paragraphe = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Category(models.Model):
    ''' category de ce nous faisons '''
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class About_porfolio(models.Model):
    ''' for about page '''
    image_porfolio_1 = models.ImageField(upload_to='image_about_porfolio', blank=True, help_text="width_field=900, height_field=632")
    image_porfolio_2 = models.ImageField(upload_to='image_about_porfolio', blank=True, help_text="width_field=900, height_field=632")
    image_porfolio_3 = models.ImageField(upload_to='image_about_porfolio', blank=True, help_text="width_field=900, height_field=632")

class About_manager(models.Model):
    image_about_manager = models.ImageField(upload_to='about_manager', help_text="width_field=500, height_field=535")
    name = models.CharField(max_length=20)
    paragraphe = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class About_text(models.Model):
    text_1 = models.CharField(max_length=300, blank=True)
    text_2 = models.CharField(max_length=300, blank=True)
    text_3 = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.text_1

class Manager_say(models.Model):
    name = models.CharField(max_length=300, blank=True)
    paragraphe = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Presentation(models.Model):
    ''' for presentation page article '''
    title = models.CharField(max_length=100)
    image_present_1 = models.ImageField(upload_to='presentation', blank=True, help_text="width_field=870, height_field=350")
    image_present_2 = models.ImageField(upload_to='presentation', blank=True, help_text="width_field=870, height_field=350")
    image_present_3 = models.ImageField(upload_to='presentation', blank=True, help_text="width_field=870, height_field=350")
    image_present_4 = models.ImageField(upload_to='presentation', blank=True, help_text="width_field=870, height_field=350")
    image_present_5 = models.ImageField(upload_to='presentation', blank=True, help_text="width_field=870, height_field=350")
    image_present_6 = models.ImageField(upload_to='presentation', blank=True, help_text="width_field=870, height_field=350")
    image_present_7 = models.ImageField(upload_to='presentation', blank=True, help_text="width_field=870, height_field=350")
    image_present_8 = models.ImageField(upload_to='presentation', blank=True, help_text="width_field=870, height_field=350")
    date_creat = models.DateTimeField(auto_now_add=True)
    paragraphe = models.CharField(max_length=350, blank=True)

    category = models.CharField(max_length=50)
    client = models.CharField(max_length=100)
    project_url = models.URLField(blank=True)
    text_entrepise = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("details", kwargs={"id": self.id})
