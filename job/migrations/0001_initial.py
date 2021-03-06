# Generated by Django 2.1 on 2020-05-03 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('information', '0001_initial'),
        ('plan', '0001_initial'),
        ('equipment', '0002_auto_20200503_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_loading',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False, verbose_name='卸船作业编号')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='作业开始时间')),
                ('start_time_after', models.DateTimeField(blank=True, null=True, verbose_name='后吊具作业开始时间')),
                ('middle_time_p', models.DateTimeField(blank=True, null=True, verbose_name='计划至中转平台时间')),
                ('middle_time_a', models.DateTimeField(blank=True, null=True, verbose_name='实际至中转平台时间')),
                ('end_time_qc_p', models.DateTimeField(blank=True, null=True, verbose_name='岸桥作业计划结束时间')),
                ('end_time_qc', models.DateTimeField(blank=True, null=True, verbose_name='岸桥作业结束时间')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='装船作业结束时间')),
                ('agv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.AGV')),
                ('plan', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='plan_job_l', to='plan.Plan_unloading', verbose_name='卸船计划编号')),
                ('qc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Quay_crane')),
                ('voy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.Voyage')),
            ],
        ),
        migrations.CreateModel(
            name='Job_unloading',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False, verbose_name='卸船作业编号')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='作业开始时间')),
                ('middle_time_p', models.DateTimeField(blank=True, null=True, verbose_name='计划至中转平台时间')),
                ('middle_time_a', models.DateTimeField(blank=True, null=True, verbose_name='实际至中转平台时间')),
                ('start_time_after', models.DateTimeField(blank=True, null=True, verbose_name='后吊具作业开始时间')),
                ('end_time_qc_p', models.DateTimeField(blank=True, null=True, verbose_name='岸桥作业计划结束时间')),
                ('end_time_qc', models.DateTimeField(blank=True, null=True, verbose_name='岸桥作业结束时间')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='卸船作业结束时间')),
                ('agv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.AGV')),
                ('plan', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='plan_job_u', to='plan.Plan_unloading', verbose_name='卸船计划编号')),
                ('qc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Quay_crane')),
                ('voy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.Voyage')),
            ],
        ),
    ]
