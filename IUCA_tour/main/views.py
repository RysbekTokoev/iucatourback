from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import Place, Preset, Review, PlaceImage, PlaceDesc, PlaceInPreset
from .serializers import PlaceSerializer, ReviewSerializer, PresetSerializer, PlaceImageSerializer, PlaceDescSerializer, PlaceInPresetSerializer


class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'head']

    def list(self, request):
        places = Place.objects.all()
        serializerPlace = PlaceSerializer(places, many=True)
        data = serializerPlace.data.copy()

        for i, x in enumerate(data):
            images = PlaceImage.objects.filter(place=x['id'])
            if request.query_params.get('lang'):
                descriptions = PlaceDesc.objects.filter(place=x['id'], lang=request.query_params.get('lang'))

                serializerDesc = PlaceDescSerializer(descriptions, many=True)
                [data[i].update(description) for description in serializerDesc.data]
            else:
                descriptions = PlaceDesc.objects.filter(place=x['id'])
                serializerDesc = PlaceDescSerializer(descriptions, many=True)
                data[i].update({"descriptions": serializerDesc.data})

            serializerImage = PlaceImageSerializer(images, many=True)
            data[i].update({"images": [image['image'] for image in serializerImage.data]})

        return Response(data)

    def retrieve(self, request, pk=None):
        queryset = Place.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PlaceSerializer(user)
        data = serializer.data.copy()

        images = PlaceImage.objects.filter(place=data['id'])
        if request.query_params.get('lang'):
            descriptions = PlaceDesc.objects.filter(place=data['id'], lang=request.query_params.get('lang'))

            serializerDesc = PlaceDescSerializer(descriptions, many=True)
            [data.update(description) for description in serializerDesc.data]
        else:
            descriptions = PlaceDesc.objects.filter(place=data['id'])
            serializerDesc = PlaceDescSerializer(descriptions, many=True)
            data.update({"descriptions": serializerDesc.data})

        serializerImage = PlaceImageSerializer(images, many=True)
        data.update({"images": [image['image'] for image in serializerImage.data]})

        return Response(data)


class PresetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Preset.objects.all()
    serializer_class = PresetSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'head']

    def list(self, request):
        presets = Preset.objects.all()
        serializerPreset = PresetSerializer(presets, many=True)
        data = serializerPreset.data.copy()

        for i, x in enumerate(data):
            places = PlaceInPreset.objects.filter(preset=x['id'])
            serializerPlace = PlaceInPresetSerializer(places, many=True)
            data[i].update({"places": [place for place in serializerPlace.data]})

        return Response(data)

    def retrieve(self, request, pk):
        presets = Preset.objects.all()
        preset = get_object_or_404(presets, pk=pk)

        serializerPreset = PresetSerializer(preset)
        data = serializerPreset.data.copy()

        places = PlaceInPreset.objects.filter(preset=data['id'])
        serializerPlace = PlaceInPresetSerializer(places, many=True)
        data.update({"places": [place for place in serializerPlace.data]})

        return Response(data)


class PlaceDescViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlaceDesc.objects.all()
    serializer_class = PlaceDescSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'head']


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'head']


class PlaceImageViewSet(viewsets.ViewSet):
    parser_classes = (MultiPartParser, FormParser)

    def list(self, request):
        all_images = PlaceImage.objects.all()
        serializer = PlaceImageSerializer(all_images, many=True)
        return Response(serializer.data)
