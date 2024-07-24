from django.db import models
from django.urls import reverse
from django.utils.text import slugify





class Skill(models.Model):
    name  = models.CharField(max_length=250)
    image = models.ImageField(upload_to='SkillsImage', blank=True) 


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'    

    def __str__(self):
        return self.question[10]
    



class Project(models.Model):
    name  = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='Projects/images')
    description = models.TextField()
    demo = models.URLField()
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('portfolio:project_details', args=[self.pk , self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)    


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='project_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ProjectsImages')









class MyEmail(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return self.name 
