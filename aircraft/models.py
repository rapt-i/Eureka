from django.db import models
from django.utils.timezone import now


class Aircraft(models.Model):
    name = models.CharField(verbose_name='機体名', max_length=50)


class TestFlightType(models.Model):
    STATUS_CHOICES = (
        ("in_school", "学内"),
        ("out_school", "学外"),
        ("contest", "鳥コン")
    )
    status = models.CharField(verbose_name="TFタイプ", max_length=50, choices=STATUS_CHOICES, default="in_school")
    location = models.CharField(verbose_name="滑走路", max_length=50, null=True)
    pub_time = models.DateTimeField(verbose_name="時間", default=now)
    aircraft = models.ForeignKey(
        Aircraft,
        verbose_name='飛行機',
        related_name="tf_set",
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    def __str__(self):
        return str(self.aircraft) + str(self.id) + str(self.status)

    class Meta:
        db_table = "test_flight_type"


class FlightType(models.Model):
    STATUS_CHOICES = (
        ('n', '未指定'),
        ('w', '滑走'),
        ('j', 'ジャンプ'),
        ('sf', '短距離'),
        ('mf', '中距離'),
        ('lf', '長距離'),
    )
    number = models.IntegerField(verbose_name='本数')
    status = models.CharField(verbose_name='タイプ', max_length=10, choices=STATUS_CHOICES, default='n')
    created_time = models.DateTimeField(verbose_name='開始時間', default=now, unique=True)
    tf_type = models.ForeignKey(
        TestFlightType,
        verbose_name="TFタイプ",
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    def __str__(self):
        return str(self.status) + str(self.number)

    class Meta:
        db_table = 'tf_type'  # 数据库表名
        ordering = ['created_time']  # 按数据录入时间升序
        get_latest_by = 'created_time'


class FlightData(models.Model):
    time = models.DateTimeField(verbose_name='time', default=now, unique=True, primary_key=True)
    speed = models.FloatField(verbose_name='速度', default=0.0)
    height = models.FloatField(verbose_name='高度', default=0.0)
    steering_angle = models.FloatField(verbose_name='舵角', default=0.0)
    rotation = models.FloatField(verbose_name='回転数', default=0.0)
    lat = models.FloatField(verbose_name='緯度', default=34.979756)  # ACT α的纬度
    lng = models.FloatField(verbose_name='経度', default=135.965154)  # ACT α的经度
    flight_type = models.ForeignKey(FlightType, verbose_name='TF_type', on_delete=models.CASCADE, blank=False,
                                    null=False)

    # 关联TF type

    def __str__(self):
        return str(self.time)

    def next_data(self):  # id比当前id大，状态为已发布，发布时间不为空
        return FlightData.objects.filter(id__gt=self.id).first()

    def prev_data(self):
        return FlightData.objects.filter(id__lt=self.id).first()

    class Meta:
        ordering = ['time']  # 按数据录入时间升序指定后台显示模型复数名称
        db_table = 'flight_data'  # 数据库表名
        get_latest_by = 'time'
