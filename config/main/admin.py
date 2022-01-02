from django.contrib import admin
from .models import Place, Preset, Review, PlaceImage, PlaceDesc, PlaceInPreset


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1


class PlaceDescInline(admin.TabularInline):
    model = PlaceDesc
    extra = 1


class PlaceInPresetInline(admin.TabularInline):
    model = PlaceInPreset
    extra = 1


class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline, PlaceDescInline]


class PresetAdmin(admin.ModelAdmin):
    inlines = [PlaceInPresetInline, ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Preset, PresetAdmin)
admin.site.register(Review)
