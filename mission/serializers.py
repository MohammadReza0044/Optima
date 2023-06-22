from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Mission


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = "__all__"

    def create(self, validated_data):
        mission = Mission.objects.create(**validated_data)
        driver = validated_data.pop("driver")
        driver.is_doing_the_mission = True
        driver.save()

        return mission

    def validate(self, data):
        data_dict = dict(data)
        driver = data_dict.get("driver")
        if driver.is_doing_the_mission == True:
            raise serializers.ValidationError(
                {
                    "driver": [
                        "این راننده در حال انجام ماموریت میباشد. لطفا راننده ی دیگری را انتخاب نمایید."
                    ]
                }
            )
        return data
