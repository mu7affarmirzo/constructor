from django.db import models

def upload_location(instance, filename):
    file_path = 'shirt_designer/{title}-{filename}'.format(
        title=str(instance.__class__.__name__), filename=filename)
    return file_path


class FabricModel(models.Model):
    WORST = '1'
    BAD = '2'
    ADEQUATE = '3'
    GOOD = '4'
    EXCELLENT = '5'
    SELECT_CHOICES = [
        (WORST, '1'),
        (BAD, '2'),
        (ADEQUATE, '3'),
        (GOOD, '4'),
        (EXCELLENT, '5'),
    ]
    fabric = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=200, unique=True)
    index = models.BooleanField(default=False)

    colour = models.CharField(max_length=500, null=True, blank=True)
    pattern = models.CharField(max_length=500, null=True, blank=True)
    season = models.CharField(max_length=500, null=True, blank=True)
    composition = models.CharField(max_length=500, null=True, blank=True)
    fineness = models.CharField(max_length=2, choices=SELECT_CHOICES, default=GOOD,)
    weight = models.CharField(max_length=2, choices=SELECT_CHOICES, default=GOOD,)
    weave = models.CharField(max_length=2, choices=SELECT_CHOICES, default=GOOD,)
    fabric_image = models.ImageField(upload_to=upload_location, null=True, blank=True)


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
    sleeve_style = models.ForeignKey('SubSideBarModel', related_name='sleeves_here', on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.type

class ShirtSleeveModel(models.Model):
    fabric = models.ForeignKey(FabricModel,
                              related_name='sleeve', blank=True, null=True,
                              on_delete=models.CASCADE)
    # type = models.ForeignKey(SleeveTypeModel,
    #                            related_name='sleevetype', blank=True, null=True,
    #                            on_delete=models.CASCADE)
    sleeve_style = models.ForeignKey('SubSideBarModel', related_name='sleeves_type', on_delete=models.CASCADE, null=True, blank=True)
    long_img = models.ImageField(upload_to=upload_location, null=True, blank=True)
    short_img = models.ImageField(upload_to=upload_location, null=True, blank=True)
    short_with_ibbon_img = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return f'{self.fabric} {self.sleeve_style}'

class YokeTypeModel(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.type

class YokeModel(models.Model):
    fabric = models.ForeignKey(FabricModel,
                              related_name='yoke', blank=True, null=True,
                              on_delete=models.CASCADE)
    type = models.ForeignKey('SubSideBarModel',
                               related_name='yoketype', blank=True, null=True,
                               on_delete=models.CASCADE)

    yoke_img = models.ImageField(upload_to=upload_location, null=True, blank=True)

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
    type = models.ForeignKey('SubSideBarModel',
                              related_name='backtype', blank=True, null=True,
                              on_delete=models.CASCADE)
    back_style_img = models.ImageField(upload_to=upload_location, null=True, blank=True)

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
    type = models.ForeignKey('SubSideBarModel',
                              related_name='bottomtype', blank=True, null=True,
                              on_delete=models.CASCADE)

    bottomcut_img = models.ImageField(upload_to=upload_location, null=True, blank=True)

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
    type = models.ForeignKey('SubSideBarModel',
                               related_name='collartype', blank=True, null=True,
                               on_delete=models.CASCADE)

    collarname = models.CharField(max_length=400, null=True, blank=True)
    collar_img = models.ImageField(upload_to=upload_location, null=True, blank=True)
    back_collar_img = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return f'{self.fabric} {self.collarname}'


class CuffTypeModel(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.type

class CuffModel(models.Model):
    fabric = models.ForeignKey(FabricModel,
                              related_name='cuff', blank=True, null=True,
                              on_delete=models.CASCADE)
    type = models.ForeignKey('SubSideBarModel',
                               related_name='cufftype', blank=True, null=True,
                               on_delete=models.CASCADE)

    typename = models.CharField(max_length=400, null=True, blank=True)
    cuff_img = models.ImageField(upload_to=upload_location, null=True, blank=True)
    back_cuff_img = models.ImageField(upload_to=upload_location, null=True, blank=True)

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
    type = models.ForeignKey('SubSideBarModel',
                               related_name='plackettype', blank=True, null=True,
                               on_delete=models.CASCADE)

    placketname = models.CharField(max_length=400, null=True, blank=True)
    placket_img = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return f'{self.fabric} {self.type}'

class PocketModel(models.Model):
    fabric = models.ForeignKey(FabricModel,
                               related_name='pocket', blank=True, null=True,
                               on_delete=models.CASCADE)
    type = models.ForeignKey('StyleSideBarModel',
                             related_name='plackettype', blank=True, null=True,
                             on_delete=models.CASCADE)

    pocketname = models.CharField(max_length=400, null=True, blank=True)
    pocket_img = models.ImageField(upload_to=upload_location, null=True, blank=True)

class CollarButtonModel(models.Model):
    name = models.CharField(max_length=50)
    collorbtn = models.ForeignKey(CollarTypeModel,
                                  related_name='collarbtn', blank=True, null=True,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.collorbtn}'

class CuffButtonModel(models.Model):
    name = models.CharField(max_length=50)

    cuffbtn = models.ForeignKey(CuffTypeModel,
                                 related_name='cuffbtn', blank=True, null=True,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.cuffbtn}'

class PlacketButtonModel(models.Model):
    name = models.CharField(max_length=50)

    placketbtn = models.ForeignKey(PlacketTypeModel,
                                 related_name='placketbtn', blank=True, null=True,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.placketbtn}'

class CollarThreadModel(models.Model):
    name = models.CharField(max_length=50)
    collorthr = models.ForeignKey(CollarTypeModel,
                                  related_name='collorthr', blank=True, null=True,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.collorthr}'

class CuffThreadModel(models.Model):
    name = models.CharField(max_length=50)
    cuffthr = models.ForeignKey(CuffTypeModel,
                                related_name='cuffthr', blank=True, null=True,
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.cuffthr}'

class PlacketThreadModel(models.Model):
    name = models.CharField(max_length=50)
    placketthr = models.ForeignKey(PlacketTypeModel,
                                   related_name='placketthr', blank=True, null=True,
                                   on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.placketthr}'

class SideBarModel(models.Model):
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    sub_stat = models.BooleanField(null=True, blank=True, default=True)
    search_url = models.URLField(null=True, blank=True)
    search_stat = models.BooleanField(null=True, blank=True, default=False)
    related_menu_stat = models.BooleanField(null=True, blank=True, default=True)

    def __str__(self):
        return str(self.title)

class SubSideBarModel(models.Model):
    global_menu = models.ForeignKey(SideBarModel, blank=True, null=True, on_delete=models.CASCADE, related_name='sub_bar')
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    sub_stat = models.BooleanField(null=True, blank=True, default=False)
    search_url = models.URLField(null=True, blank=True)
    search_stat = models.BooleanField(null=True, blank=True, default=False)
    related_menu = models.ForeignKey(SideBarModel, blank=True, null=True, on_delete=models.CASCADE, related_name='related_menu')

    # class Meta:
    #     app_label = 'tester_label'
    def __str__(self):
        return str(self.title)

class StyleSideBarModel(models.Model):
    sub_side = models.ForeignKey(SubSideBarModel, blank=True, null=True, on_delete=models.CASCADE, related_name='sub_side')
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    sub_stat = models.BooleanField(null=True, blank=True, default=False)
    search_url = models.CharField(max_length=250, blank=True, null=True)
    search_stat = models.BooleanField(null=True, blank=True, default=False)
    related_menu = models.ForeignKey(SubSideBarModel, blank=True, null=True, on_delete=models.CASCADE, related_name='related_style' )

    def __str__(self):
        return str(self.title)
    # 
    # class Meta:
    #     app_label = 'tester_label'