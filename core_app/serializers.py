from rest_framework import serializers

from core_app.models import Phone, Color, PhoneImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneImage
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = ('id', 'name', 'price', 'description', 'photo')


class PhoneDetailSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)

    class Meta:
        model = Phone
        fields = (
            'name', 'price', 'memory', 'color', 'description', 'category',
            'display', 'network_support', 'camera', 'computing_resources', 'battery',
            'secure_authentication', 'display_and_body', 'water_and_dust_protection',
            'audi_and_video', 'dimensions_and_weight', 'contents_of_delivery', 'image', 'photo'
        )


#class ColorSerializer(serializers.ModelSerializer):
   # class Meta:
    #    model = Color
     #   fields = '__all__'