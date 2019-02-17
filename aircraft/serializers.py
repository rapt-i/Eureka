from rest_framework import serializers
from .models import Aircraft, TestFlightType, FlightType, FlightData
from .utils import ChoiceDisplayField


class FlightDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightData
        fields = '__all__'


class FlightTypeSerializer(serializers.ModelSerializer):
    #    flightdata_set = FlightDataSerializer(many=True, read_only=True)

    class Meta:
        model = FlightType
        fields = '__all__'


class TestFlightTypeSerializer(serializers.ModelSerializer):
    #    flighttype_set = FlightTypeSerializer(many=True, read_only=True)
    STATUS_CHOICES = (
        ("in_school", "学内"),
        ("out_school", "学外"),
        ("contest", "鳥コン")
    )
    status = ChoiceDisplayField(choices=STATUS_CHOICES)

    class Meta:
        model = TestFlightType
        fields = '__all__'


class AircraftSerializer(serializers.ModelSerializer):
    # tf_set = TestFlightTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Aircraft
        fields = '__all__'  # ('name', 'created_time')也可以用这种方式指定字段
        depth = 1
