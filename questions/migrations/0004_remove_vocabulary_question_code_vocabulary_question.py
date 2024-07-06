# Generated by Django 5.0.6 on 2024-07-05 09:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_remove_vocabulary_question_vocabulary_question_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocabulary',
            name='question_code',
        ),
        migrations.AddField(
            model_name='vocabulary',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vocabularies', to='questions.question'),
        ),
    ]
