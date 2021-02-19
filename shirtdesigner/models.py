from django.db import models

def upload_location(instance, filename):
    file_path = 'shirt_designer/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename)
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


    class Meta:
        ordering = ('price', )
        verbose_name = 'fabric'
        verbose_name_plural = 'fabrics'

    def __str__(self):
        return self.fabric



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
    global_menu = models.ForeignKey(SideBarModel, blank=True, null=True, on_delete=models.CASCADE, related_name='sub_list')
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




# *****************Style Model********************

class StyleModel(models.Model):
    style_bar = models.ForeignKey(SideBarModel, related_name='model_style', on_delete=models.CASCADE, blank=True, null=True)
    style_name = models.CharField(max_length=250,  null=True, blank=True)
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(self.style_name)



# *****************Siluet Model********************
class SiluetStyleModel(models.Model):
    siluet_bar = models.ForeignKey(SideBarModel, related_name='siluet_style', on_delete=models.CASCADE, blank=True, null=True)
    style_name = models.CharField(max_length=250,  null=True, blank=True, verbose_name='Silhouette')
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)


    def __str__(self):
        return str(self.style_name)

class SiluetObjModel(models.Model):
    style_siluet = models.ForeignKey(SiluetStyleModel, related_name='siluet_obj', on_delete=models.CASCADE, blank=True, null=True)
    fabric = models.ForeignKey(FabricModel,related_name='siluet_obj', on_delete=models.CASCADE, blank=True, null=True,)


# *****************Sleeve Model********************
class SleeveStyleModel(models.Model):
    sleeve_bar = models.ForeignKey(SideBarModel, related_name='sleeve_style', on_delete=models.CASCADE, blank=True,
                                   null=True)
    style_name = models.CharField(max_length=250, null=True, blank=True)
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(self.style_name)

class SleeveObjModel(models.Model):
    style_sleeve = models.ForeignKey(SleeveStyleModel, related_name='sleeve_obj', on_delete=models.CASCADE, blank=True,
                                     null=True)
    fabric = models.ForeignKey(FabricModel, related_name='sleeve_obj', on_delete=models.CASCADE, blank=True,
                               null=True, )


# *****************Collar Model********************
class CollarStyleModel(models.Model):
    collar_bar = models.ForeignKey(SideBarModel, related_name='collar_style', on_delete=models.CASCADE, blank=True,
                                   null=True)
    style_name = models.CharField(max_length=250, null=True, blank=True)
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(self.style_name)

# class CollarObjModel(models.Model):
#     style_collar = models.ForeignKey(default=CuffObjModel.objects, related_name='collar_obj', on_delete=models.CASCADE, blank=True,
#                                      null=True)
#     fabric = models.ForeignKey(FabricModel, related_name='collar_obj', on_delete=models.CASCADE, blank=True,
#                                null=True, )

class CollarBandHeightModel(models.Model):
    collar_bar = models.ForeignKey(SideBarModel, related_name='collar_band_height', on_delete=models.CASCADE, blank=True,
                                   null=True)
    choices = models.CharField(max_length=250, null=True, blank=True)
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)

class CollarBandBtntModel(models.Model):
    collar_bar = models.ForeignKey(SideBarModel, related_name='collar_band_btn', on_delete=models.CASCADE, blank=True,
                                   null=True)
    choices = models.CharField(max_length=250, null=True, blank=True)
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)

class CollarStiffnessModel(models.Model):
    collar_bar = models.ForeignKey(SideBarModel, related_name='collar_stiffness', on_delete=models.CASCADE, blank=True,
                                   null=True)
    choices = models.CharField(max_length=250, null=True, blank=True)
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)


# *****************Cuff Model********************
class CuffStyleModel(models.Model):
    cuff_bar = models.ForeignKey(SideBarModel, related_name='cuff_style', on_delete=models.CASCADE, blank=True,
                                   null=True)
    style_name = models.CharField(max_length=250, null=True, blank=True)
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(self.style_name)

class CuffObjModel(models.Model):
    style_cuff = models.ForeignKey(CuffStyleModel, related_name='cuff_obj', on_delete=models.CASCADE, blank=True,
                                     null=True)
    fabric = models.ForeignKey(FabricModel, related_name='cuff_obj', on_delete=models.CASCADE, blank=True,
                               null=True, )


class CuffBtntModel(models.Model):
    cuff_bar = models.ForeignKey(SideBarModel, related_name='cuff_btn', on_delete=models.CASCADE, blank=True,
                                   null=True)
    choices = models.CharField(max_length=250, null=True, blank=True)
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)

class CuffStiffnessModel(models.Model):
    cuff_bar = models.ForeignKey(SideBarModel, related_name='cuff_stiffness', on_delete=models.CASCADE, blank=True,
                                   null=True)
    choices = models.CharField(max_length=250, null=True, blank=True)
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)

# *****************Pockets Model********************
class PocketStyleModel(models.Model):
    pocket_bar = models.ForeignKey(SideBarModel, related_name='pocket_style', on_delete=models.CASCADE, blank=True,
                                   null=True)
    style_name = models.CharField(max_length=250, null=True, blank=True)
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(self.style_name)

class PocketObjModel(models.Model):
    style_pocket = models.ForeignKey(PocketStyleModel, related_name='pocket_obj', on_delete=models.CASCADE, blank=True,
                                     null=True)
    fabric = models.ForeignKey(FabricModel, related_name='pocket_obj', on_delete=models.CASCADE, blank=True,
                               null=True, )

# *****************More details Model********************
class PlacketStyleModel(models.Model):
    placket_bar = models.ForeignKey(SideBarModel, related_name='placket_style', on_delete=models.CASCADE, blank=True,
                                   null=True)
    style_name = models.CharField(max_length=250, null=True, blank=True)
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(self.style_name)

class PlacketObjModel(models.Model):
    style_placket = models.ForeignKey(PlacketStyleModel, related_name='placket_obj', on_delete=models.CASCADE, blank=True,
                                     null=True)
    fabric = models.ForeignKey(FabricModel, related_name='placket_obj', on_delete=models.CASCADE, blank=True,
                               null=True, )


class YokeStyleModel(models.Model):
    pocket_bar = models.ForeignKey(SideBarModel, related_name='yoke_style', on_delete=models.CASCADE, blank=True,
                                   null=True)
    style_name = models.CharField(max_length=250, null=True, blank=True)
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(self.style_name)

class YokeObjModel(models.Model):
    style_yoke = models.ForeignKey(YokeStyleModel, related_name='yoke_obj', on_delete=models.CASCADE, blank=True,
                                     null=True)
    fabric = models.ForeignKey(FabricModel, related_name='yoke_obj', on_delete=models.CASCADE, blank=True,
                               null=True, )


class ShouldersStyleModel(models.Model):
    shoulders_bar = models.ForeignKey(SideBarModel, related_name='shoulders_style', on_delete=models.CASCADE, blank=True,
                                   null=True)
    style_name = models.CharField(max_length=250, null=True, blank=True)
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(self.style_name)

class ShouldersObjModel(models.Model):
    style_shoulders = models.ForeignKey(ShouldersStyleModel, related_name='shoulders_obj', on_delete=models.CASCADE, blank=True,
                                     null=True)
    fabric = models.ForeignKey(FabricModel, related_name='shoulders_obj', on_delete=models.CASCADE, blank=True,
                               null=True, )


class BackStyleModel(models.Model):
    back_bar = models.ForeignKey(SideBarModel, related_name='back_style', on_delete=models.CASCADE, blank=True,
                                   null=True)
    style_name = models.CharField(max_length=250, null=True, blank=True)
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(self.style_name)

class BackObjModel(models.Model):
    style_back = models.ForeignKey(BackStyleModel, related_name='back_obj', on_delete=models.CASCADE, blank=True,
                                     null=True)
    fabric = models.ForeignKey(FabricModel, related_name='back_obj', on_delete=models.CASCADE, blank=True,
                               null=True, )

class BottomStyleModel(models.Model):
    bottom_bar = models.ForeignKey(SideBarModel, related_name='bottom_style', on_delete=models.CASCADE, blank=True,
                                   null=True)
    style_name = models.CharField(max_length=250, null=True, blank=True)
    icon = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(self.style_name)

class BottomObjModel(models.Model):
    style_bottom = models.ForeignKey(BottomStyleModel, related_name='bottom_obj', on_delete=models.CASCADE, blank=True,
                                     null=True)
    fabric = models.ForeignKey(FabricModel, related_name='bottom_obj', on_delete=models.CASCADE, blank=True,
                               null=True, )
