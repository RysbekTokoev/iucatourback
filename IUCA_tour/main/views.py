from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from django.http import JsonResponse

import os
from pathlib import Path

from .grauf_module import getPath

from .models import Place, Preset, Review, PlaceImage, PlaceDesc, PlaceInPreset
from .serializers import PlaceSerializer, ReviewSerializer, PresetSerializer, PlaceImageSerializer, PlaceDescSerializer, \
    PlaceInPresetSerializer

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


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
        data = PresetSerializer(presets, many=True).data.copy()

        for i, x in enumerate(data):
            places_in_preset = PlaceInPreset.objects.filter(preset=x['id']).order_by('order')
            places_in_preset_data = PlaceInPresetSerializer(places_in_preset_data, many=True).data.copy()
            data[i].update({"places": [place for place in places_in_preset_data]})

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


def get_image_view(request):
    # получение пораметров
    _from = request.GET.get('from', '')
    _to = request.GET.get('to', '')

    if _from == '' or _to == '':
        return JsonResponse(status=404, data={'status': 'false', 'message': 'предоставлены не верные параметры'})

    maps = generate_maps(_from, _to)
    if not maps:
        return JsonResponse(status=404, data={'status': 'false', 'message': 'путь не может быть построен'})
    else:
        return JsonResponse(status=200, data={'status': 'true', 'message': {
            "ground_floor": maps['ground_floor'],
            "first_floor": maps['first_floor'],
            "second_floor": maps['second_floor'],
            "third_floor": maps['third_floor']
        }})


def generate_maps(_from, _to):
    if os.path.exists(f'media/map_output/from_{_from}_to_{_to}_ground_floor.jpg') and os.path.exists(
            f'media/map_output/from_{_from}_to_{_to}_first_floor.jpg') and os.path.exists(
            f'media/map_output/from_{_from}_to_{_to}_second_floor.jpg') and os.path.exists(
            f'media/map_output/from_{_from}_to_{_to}_third_floor.jpg'):
        return JsonResponse(status=200, data={'status': 'true', 'message': {
            "ground_flour": f'media/map_output/from_{_from}_to_{_to}_ground_floor.jpg',
            "first_flour": f'media/map_output/from_{_from}_to_{_to}_first_floor.jpg',
            "second_flour": f'media/map_output/from_{_from}_to_{_to}_second_floor.jpg',
            "third_flor": f'media/map_output/from_{_from}_to_{_to}_third_floor.jpg'}})

    # генерирование маршрута
    try:
        maps_ = getPath(_from, _to)
    except:
        return False

    maps = {}

    maps['slug'] = f'{_from}_{_to}'

    maps['ground_floor'] = maps_[0]
    maps['first_floor'] = maps_[1]
    maps['second_floor'] = maps_[2]
    maps['third_floor'] = maps_[3]

    return maps
