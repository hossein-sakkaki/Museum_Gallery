from django.db import models


def upload_gallery_to_folder(instance, filename):
    return f"photo/gallery/{instance.place_code}/{filename}"

class Gallery(models.Model):
    PLACE_NAME = [
        ('1','1. Museum halls'),
        ('2','2. Ferdows cinema'),
        ('3','3. Tamadon cinema'),
        ('4','4. Book shop'),
        ('5','5. Viuna cafe'),
        ('6','6. Other picture'),
    ]
    place_code = models.CharField(max_length=15, choices=PLACE_NAME ,verbose_name="Place Code")
    shot_photo_date = models.DateField(auto_now_add=False)
    register_date = models.DateField(auto_now_add=True)
    image_name = models.ImageField(upload_to=upload_gallery_to_folder, max_length=50, verbose_name="Picture Name")
    text_info = models.TextField(verbose_name="Information")
    parent_code = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='child', verbose_name="Parent Code")
    slug = models.SlugField(max_length=50, verbose_name='Slug')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    
    def __str__(self) -> str:
        return self.place_code
        # return f"{self.place_code} {self.shot_photo_date} {self.image_name} {self.text_info} {self.parent_code} {self.slug} {str(self.is_active)}"

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
    
