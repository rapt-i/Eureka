from django.db import models
from django.utils.timezone import now


# from aircraft.models import TestFlightType


class Summary(models.Model):
    time = models.DateTimeField(verbose_name='日付', default=now)
    name = models.CharField(verbose_name='氏名', max_length=50)
    tf = models.ForeignKey(
        aircraft.TestFlightType,
        verbose_name='TFタイプ',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )


class Section(models.Model):
    STATUS_CHOICES = (
        (0, '事前準備'),
        (1, '重心試験'),
        (2, '回転試験'),
        (3, '機体搬出'),
        (4, '組み立て'),
        (5, '転がし試験'),
        (6, '滑走試験'),
        (7, 'ジャンプ試験'),
        (8, '飛行試験'),
        (9, '解体撤収'),
        (10, 'その他')
    )
    title = models.CharField(verbose_name='類名', choices=STATUS_CHOICES, default=10)
    advantage = models.CharField(verbose_name='良かった点', max_length=2000, blank=True)
    disadvantage = models.CharField('反省点', max_length=2000, blank=True)
    improvement = models.CharField('改善案', max_length=2000, blank=True)
    summary = models.ForeignKey(
        Summary,
        verbose_name='総括',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
