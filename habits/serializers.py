from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    def validate(self, data):
        is_pleasant = data.get('is_pleasant')
        linked_habit = data.get('linked_habit')
        reward = data.get('reward')
        duration = data.get('duration')

        if not is_pleasant:
            if linked_habit and reward:
                raise serializers.ValidationError(
                    'Обычная привычка не может одновременно иметь награду и быть приятной!')
        else:
            if reward or linked_habit:
                raise serializers.ValidationError('Приятная привычка не может иметь награду или связанную привычку!')

        if linked_habit and not linked_habit.is_pleasant:
            raise serializers.ValidationError('В связанные привычки можно добавлять только с признаком приятной')

        if duration > 2:
            raise serializers.ValidationError('Длительность выполнения привычки не может быть больше двух минут')

        return data

    class Meta:
        model = Habit
        fields = '__all__'
