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

class StyleTypeModel(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.type

class SleeveTypeModel(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.type

class ShirtSleeveModel(models.Model):
    fabric = models.ForeignKey(FabricModel,
                              related_name='sleeve', blank=True, null=True,
                              on_delete=models.CASCADE)
    type = models.ForeignKey(SleeveTypeModel,
                               related_name='sleevetype', blank=True, null=True,
                               on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fabric} {self.type}'

class YokeTypeModel(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.type

class YokeModel(models.Model):
    fabric = models.ForeignKey(FabricModel,
                              related_name='yoke', blank=True, null=True,
                              on_delete=models.CASCADE)
    type = models.ForeignKey(YokeTypeModel,
                               related_name='yoketype', blank=True, null=True,
                               on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fabric} {self.type}'

class ShoulderTypeModel(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.type

class ShoulderModel(models.Model):
    fabric = models.ForeignKey(FabricModel,
                              related_name='shoulder', blank=True, null=True,
                              on_delete=models.CASCADE)
    type = models.ForeignKey(ShoulderTypeModel,
                               related_name='shouldertype', blank=True, null=True,
                               on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fabric} {self.type}'

class BackDetailsTypeModel(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.type

class BackDetailsModel(models.Model):
    fabric = models.ForeignKey(FabricModel,
                              related_name='backdetails', blank=True, null=True,
                              on_delete=models.CASCADE)
    type = models.ForeignKey(BackDetailsTypeModel,
                              related_name='backtype', blank=True, null=True,
                              on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fabric} {self.type}'

class BottomCutTypeModel(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.type

class BottomCutModel(models.Model):
    fabric = models.ForeignKey(FabricModel,
                              related_name='bottom', blank=True, null=True,
                              on_delete=models.CASCADE)
    type = models.ForeignKey(BottomCutTypeModel,
                              related_name='bottomtype', blank=True, null=True,
                              on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fabric} {self.type}'

class CollarTypeModel(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.type

class CollarModel(models.Model):
    fabric = models.ForeignKey(FabricModel,
                              related_name='collar', blank=True, null=True,
                              on_delete=models.CASCADE)
    type = models.ForeignKey(CollarTypeModel,
                               related_name='collartype', blank=True, null=True,
                               on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.fabric} {self.type}'

class CuffTypeModel(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.type

class CuffModel(models.Model):
    fabric = models.ForeignKey(FabricModel,
                              related_name='cuff', blank=True, null=True,
                              on_delete=models.CASCADE)
    type = models.ForeignKey(CuffTypeModel,
                               related_name='cufftype', blank=True, null=True,
                               on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fabric} {self.type}'

class PlacketTypeModel(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.type

class PlacketModel(models.Model):
    fabric = models.ForeignKey(FabricModel,
                              related_name='placket', blank=True, null=True,
                              on_delete=models.CASCADE)
    type = models.ForeignKey(PlacketTypeModel,
                               related_name='plackettype', blank=True, null=True,
                               on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fabric} {self.type}'