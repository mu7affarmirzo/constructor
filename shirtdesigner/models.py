from django.db import models

def upload_location(instance, filename):
    file_path = 'shirt_designer/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename)
    return file_path

class FabricModel(models.Model):
    fabric = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=200, unique=True)
    index = models.BooleanField(default=False)

    class Meta:
        ordering = ('price', )
        verbose_name = 'fabric'
        verbose_name_plural = 'fabrics'

    def __str__(self):
        return self.fabric
