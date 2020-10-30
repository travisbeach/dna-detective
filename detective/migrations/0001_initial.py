# Generated by Django 2.2.16 on 2020-10-29 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=2000)),
                ('status', models.CharField(choices=[('IN_PROGRESS', 'IN PROGRESS'), ('COMPLETED', 'COMPLETED')], max_length=60)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=60, null=True)),
                ('index', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('protein', models.CharField(max_length=60, null=True)),
            ],
        ),
    ]