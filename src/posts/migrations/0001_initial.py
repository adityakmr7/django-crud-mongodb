# Generated by Django 2.2 on 2019-04-04 16:26

from django.db import migrations, models
import slugger.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', slugger.fields.AutoSlugField(populate_from='title')),
                ('content', models.TextField()),
                ('overview', models.CharField(max_length=60)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]