# Generated by Django 5.1.3 on 2024-12-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=255)),
                ('question_type', models.CharField(choices=[('multiplication', 'Multiplication'), ('checkbox', 'Checkbox')], max_length=50)),
                ('options', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
