from django.db import models


class Place(models.Model):
    unifiedName = models.CharField(max_length=32)

    def __str__(self):
        return self.unifiedName


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class PlaceDesc(models.Model):
    name = models.CharField(max_length=32)
    place = models.ForeignKey(Place, related_name='desc', on_delete=models.CASCADE)
    desc = models.TextField(max_length=256)
    audio = models.FileField(upload_to='audio/')

    CHINESE = 'CHN'
    ENGLISH = 'ENG'
    RUSSIAN = 'RUS'
    KYRGYZ = 'KGZ'
    LANGUAGE = [
        (CHINESE, 'Chinese'),
        (ENGLISH, 'English'),
        (RUSSIAN, 'Russian'),
        (KYRGYZ, 'Kyrgyz'),
    ]
    lang = models.CharField(
        max_length=3,
        choices=LANGUAGE,
        default=RUSSIAN
    )

    def __str__(self):
        return self.lang + str(self.place)

    def save(self, *args, **kwargs):
        obj = PlaceDesc.objects.filter(place=self.place, lang=self.lang)
        if obj:
            return obj
        return super(PlaceDesc, self).save(*args, **kwargs)


class Preset(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class PlaceInPreset(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    preset = models.ForeignKey(Preset, on_delete=models.CASCADE)
    order = models.IntegerField()


class Review(models.Model):
    identity = models.CharField(max_length=32)
    rate = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.identity
