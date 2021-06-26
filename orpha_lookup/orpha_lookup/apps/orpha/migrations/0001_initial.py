from django.db import migrations, models
import django.db.models.functions.text
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False,
                                                                verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False,
                                                                      verbose_name='modified')),
                ('orpha_code', models.IntegerField(unique=True)),
                ('expert_link', models.CharField(default=None, max_length=256, null=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DisorderGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False,
                                                                verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False,
                                                                      verbose_name='modified')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DisorderHpos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DisorderType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False,
                                                                verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False,
                                                                      verbose_name='modified')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False,
                                                                verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False,
                                                                      verbose_name='modified')),
                ('name', models.CharField(max_length=256)),
                ('weight', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hpo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False,
                                                                verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False,
                                                                      verbose_name='modified')),
                ('hpo_id', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddIndex(
            model_name='hpo',
            index=models.Index(django.db.models.functions.text.Lower('name'), name='lower_name_idx'),
        ),
        migrations.AddField(
            model_name='disorderhpos',
            name='disorder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orpha.disorder'),
        ),
        migrations.AddField(
            model_name='disorderhpos',
            name='frequency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orpha.frequency'),
        ),
        migrations.AddField(
            model_name='disorderhpos',
            name='hpo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orpha.hpo'),
        ),
        migrations.AddField(
            model_name='disorder',
            name='disorder_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orpha.disordergroup'),
        ),
        migrations.AddField(
            model_name='disorder',
            name='disorder_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orpha.disordertype'),
        ),
    ]
