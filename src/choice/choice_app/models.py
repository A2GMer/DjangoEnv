from django.db import models

class Screen(models.Model):
    screen_id = models.IntegerField(unique=True)
    probability = models.FloatField()  # この画面に到達する確率
    fun_fact = models.CharField(max_length=255)  # 豆知識

    def __str__(self):
        return f"Screen {self.screen_id} - {self.probability}%"
