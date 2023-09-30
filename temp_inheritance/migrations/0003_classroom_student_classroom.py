# Generated by Django 4.2.5 on 2023-09-27 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('temp_inheritance', '0002_studentprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classroom_students', to='temp_inheritance.classroom'),
        ),
    ]
