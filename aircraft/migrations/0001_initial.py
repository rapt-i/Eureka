# Generated by Django 2.1.7 on 2019-02-16 17:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='機体名')),
            ],
        ),
        migrations.CreateModel(
            name='FlightData',
            fields=[
                ('time', models.DateTimeField(default=django.utils.timezone.now, primary_key=True, serialize=False, unique=True, verbose_name='time')),
                ('speed', models.FloatField(default=0.0, verbose_name='速度')),
                ('height', models.FloatField(default=0.0, verbose_name='高度')),
                ('steering_angle', models.FloatField(default=0.0, verbose_name='舵角')),
                ('rotation', models.FloatField(default=0.0, verbose_name='回転数')),
                ('lat', models.FloatField(default=34.979756, verbose_name='緯度')),
                ('lng', models.FloatField(default=135.965154, verbose_name='経度')),
            ],
            options={
                'db_table': 'flight_data',
                'ordering': ['time'],
                'get_latest_by': 'time',
            },
        ),
        migrations.CreateModel(
            name='FlightType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='本数')),
                ('status', models.CharField(choices=[('n', '未指定'), ('w', '滑走'), ('j', 'ジャンプ'), ('sf', '短距離'), ('mf', '中距離'), ('lf', '長距離')], default='n', max_length=10, verbose_name='タイプ')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, unique=True, verbose_name='開始時間')),
            ],
            options={
                'db_table': 'tf_type',
                'ordering': ['created_time'],
                'get_latest_by': 'created_time',
            },
        ),
        migrations.CreateModel(
            name='TestFlightType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('in_school', '学内'), ('out_school', '学外'), ('contest', '鳥コン')], default='in_school', max_length=50, verbose_name='TFタイプ')),
                ('location', models.CharField(max_length=50, null=True, verbose_name='滑走路')),
                ('pub_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='時間')),
                ('aircraft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tf_set', to='aircraft.Aircraft', verbose_name='飛行機')),
            ],
            options={
                'db_table': 'test_flight_type',
            },
        ),
        migrations.AddField(
            model_name='flighttype',
            name='tf_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aircraft.TestFlightType', verbose_name='TFタイプ'),
        ),
        migrations.AddField(
            model_name='flightdata',
            name='flight_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aircraft.FlightType', verbose_name='TF_type'),
        ),
    ]
