from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Mission


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = "__all__"

    def create(self, validated_data):
        driver = validated_data.pop("driver")
        if driver.is_doing_the_mission != True:
            mission = Mission.objects.create(**validated_data, driver=driver)
            driver.is_doing_the_mission = True
            driver.save()
        else:
            raise serializers.ValidationError(
                {
                    "driver": [
                        "این راننده در حال انجام ماموریت میباشد. لطفا راننده ی دیگری را انتخاب نمایید."
                    ]
                }
            )
        return mission

    def update(self, instance, validated_data):
        driver = validated_data.pop("driver")
        mission_done = validated_data.pop("mission_done")
        if driver != self.instance.driver and driver.is_doing_the_mission == True:
            raise serializers.ValidationError(
                {
                    "driver": [
                        "این راننده در حال انجام ماموریت میباشد. لطفا راننده ی دیگری را انتخاب نمایید."
                    ]
                }
            )

        else:
            self.instance.driver.is_doing_the_mission = False
            self.instance.driver.save()
            self.instance.driver = driver
            self.instance.driver.is_doing_the_mission = True
            self.instance.driver.save()

        if mission_done == True:
            self.instance.mission_done = True
            self.instance.save()
            self.instance.driver.is_doing_the_mission = False
            self.instance.driver.save()

        else:
            self.instance.mission_done = False
            self.instance.save()
            self.instance.driver.is_doing_the_mission = True
            self.instance.driver.save()

        return super().update(instance, validated_data)
