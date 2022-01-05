from .models import Preset, Place, Review, PlaceDesc, PlaceImage, PlaceInPreset
from rest_framework import serializers


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id']


class PlaceInPresetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceInPreset
        fields = ["place", "order"]


class PlaceDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceDesc
        fields = ["name", "desc", "audio", "lang"]


class PresetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preset
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ["image"]
