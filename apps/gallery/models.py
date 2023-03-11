from django.db import models
# Create your models here.


class Gallery(models.Model):
    PLACE_NAME = [
        ('1','museum-halls'),
        ('2','ferdows-cinema'),
        ('3','tamadon-cinema'),
        ('4','book-shop'),
        ('5','viuna-cafe'),
    ]
    place_code = models.CharField(max_length=15, choices=PLACE_NAME ,verbose_name="Place Code")
    shot_photo_date = models.DateTimeField(auto_now_add=True)
    image_name = models.ImageField(upload_to='photo/gallery', max_length=50, verbose_name="Picture Name")
    text_info = models.TextField(verbose_name="Information")
    parent_code = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Parent Code")
    slug = models.SlugField(max_length=50, verbose_name='Slug')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    
    def __str__(self) -> str:
        return f"{self.place_code} {self.shot_photo_date} {self.image_name} {self.text_info} {self.parent_code} {self.slug} {str(self.is_active)}"
