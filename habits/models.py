from django.db import models

from users.models import User


class Habit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Владелец")
    place = models.CharField(max_length=255, blank=True, null=True, verbose_name="Место выполнения")
    action_time = models.CharField(max_length=255, blank=True, null=True, verbose_name="Время выполнения")
    action = models.CharField(max_length=255, verbose_name="Действие")
    is_pleasant = models.BooleanField(default=False, verbose_name="Приятная привычка")
    associated_habit = models.ManyToManyField("self", blank=True, null=True, verbose_name="Связанная привычка")
    periodicity = models.PositiveIntegerField(verbose_name="Периодичность выполнения")
    reward = models.CharField(max_length=255, null=True, blank=True, verbose_name="Вознаграждение")
    lead_time = models.PositiveIntegerField(verbose_name="Продолжительность выполнения")
    is_public = models.BooleanField(default=False, verbose_name="Публичная привычка")

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}.'

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"


# class HabitExecution(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Владелец")
#     habit = models.ForeignKey(Habit, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Привычка", related_name="habit")
#     executed_at = models.DateTimeField()
#     is_executed = models.BooleanField()
