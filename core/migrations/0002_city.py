# Generated by Django 4.1.2 on 2022-10-17 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tx_name', max_length=64)),
                ('state', models.ForeignKey(db_column='id_state', on_delete=django.db.models.deletion.DO_NOTHING, related_name='cities', to='core.state')),
            ],
            options={
                'db_table': 'city',
                'managed': True,
            },
        ),
    ]