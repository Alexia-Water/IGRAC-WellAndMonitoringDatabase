# Generated by Django 2.2.12 on 2020-07-03 09:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('gwml2', '0013_view_well_information'),
    ]

    sql = """
            CREATE VIEW well_information_uuid AS
            select *
            from well_information as w
            LEFT JOIN user_uuid u ON w.users @> ARRAY [u.user_id];
        """

    operations = [
        migrations.RunSQL('DROP VIEW IF EXISTS well_information_uuid;'),
        migrations.RunSQL(sql)
    ]
