# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 09:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidates', '0003_intent_likes_initial'),
        ('bills', '__first__'),
        ('votes', '__first__'),
        ('suggestions', '0005_suggestions_suggestor_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Standpoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(db_index=True, max_length=32)),
                ('pro', models.IntegerField(default=0)),
                ('bill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='standpoints', to='bills.Bills', to_field=b'uid')),
                ('intent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='standpoints', to='candidates.Intent', to_field=b'uid')),
                ('suggestion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='standpoints', to='suggestions.Suggestions', to_field=b'uid')),
                ('vote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='standpoints', to='votes.Votes', to_field=b'uid')),
            ],
        ),
        migrations.CreateModel(
            name='User_Standpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='standpoints.Standpoints', to_field=b'uid')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standpoints', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='user_standpoint',
            unique_together=set([('standpoint', 'user')]),
        ),
        migrations.AlterIndexTogether(
            name='user_standpoint',
            index_together=set([('user', 'standpoint')]),
        ),
    ]
