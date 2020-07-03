# Generated by Django 2.2.12 on 2020-07-03 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwml2', '0014_auto_20200703_0501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gwconstituent',
            name='gw_constituent_relation',
        ),
        migrations.CreateModel(
            name='GWConstituteOf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gw_constituent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwml2.GWConstituent', verbose_name='GWConstituent')),
                ('gw_constituent_relation', models.ForeignKey(help_text='Relation between fluid body components, typically caused by a specific mechanism.', on_delete=django.db.models.deletion.CASCADE, to='gwml2.GWConstituentRelation', verbose_name='GWConstituentRelation')),
            ],
        ),
        migrations.AddField(
            model_name='gwconstituent',
            name='gw_constitute_of',
            field=models.ForeignKey(blank=True, help_text='A general binary relation between constituents, in which the relation type can be specified in addition to the causal mechanism that caused the relationship.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.GWConstituteOf', verbose_name='GWConstituteOf'),
        ),
    ]
