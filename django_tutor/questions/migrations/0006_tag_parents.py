# Generated by Django 5.1.6 on 2025-02-08 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_answer_author_question_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='parents',
            field=models.ManyToManyField(blank=True, related_name='children', to='questions.tag'),
        ),
    ]
