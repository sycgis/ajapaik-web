# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.contrib.gis.db.models.fields
from django.conf import settings
#import oauth2client.django_orm
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=255)),
                ('related_id', models.PositiveIntegerField(null=True, blank=True)),
                ('params', django_extensions.db.fields.json.JSONField(null=True, blank=True)),
                ('related_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'db_table': 'project_action',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('name_et', models.CharField(max_length=255, null=True)),
                ('name_en', models.CharField(max_length=255, null=True)),
                ('name_ru', models.CharField(max_length=255, null=True)),
                ('name_fi', models.CharField(max_length=255, null=True)),
                ('name_sv', models.CharField(max_length=255, null=True)),
                ('name_nl', models.CharField(max_length=255, null=True)),
                ('name_de', models.CharField(max_length=255, null=True)),
                ('slug', models.SlugField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(max_length=2047, null=True, blank=True)),
                ('atype', models.PositiveSmallIntegerField(choices=[(0, b'Curated'), (1, b'Favorites'), (2, b'Auto')])),
                ('is_public', models.BooleanField(default=True)),
                ('open', models.BooleanField(default=False)),
                ('ordered', models.BooleanField(default=False)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lon', models.FloatField(null=True, blank=True)),
                ('geography', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, geography=True, blank=True)),
                ('cover_photo_flipped', models.BooleanField(default=False)),
                ('photo_count_with_subalbums', models.IntegerField(default=0)),
                ('rephoto_count_with_subalbums', models.IntegerField(default=0)),
                ('geotagged_photo_count_with_subalbums', models.IntegerField(default=0)),
                ('comments_count_with_subalbums', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'project_album',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AlbumPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(to='ajapaik.Album')),
            ],
            options={
                'db_table': 'project_albumphoto',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('name_et', models.CharField(max_length=255, null=True)),
                ('name_en', models.CharField(max_length=255, null=True)),
                ('name_ru', models.CharField(max_length=255, null=True)),
                ('name_fi', models.CharField(max_length=255, null=True)),
                ('name_sv', models.CharField(max_length=255, null=True)),
                ('name_nl', models.CharField(max_length=255, null=True)),
                ('name_de', models.CharField(max_length=255, null=True)),
                ('lat', models.FloatField(null=True)),
                ('lon', models.FloatField(null=True)),
            ],
            options={
                'db_table': 'project_area',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CredentialsModel',
            fields=[
                ('id', models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
#                ('credential', oauth2client.django_orm.CredentialsField(null=True)),
            ],
            options={
                'db_table': 'project_credentialsmodel',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('camera_make', models.CharField(max_length=255, null=True, blank=True)),
                ('camera_model', models.CharField(max_length=255, null=True, blank=True)),
                ('lens_make', models.CharField(max_length=255, null=True, blank=True)),
                ('lens_model', models.CharField(max_length=255, null=True, blank=True)),
                ('software', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'project_device',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DifficultyFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.PositiveSmallIntegerField()),
                ('trustworthiness', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'project_difficultyfeedback',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlipFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flip', models.NullBooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'project_flipfeedback',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlowModel',
            fields=[
                ('id', models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
 #               ('flow', oauth2client.django_orm.FlowField(null=True)),
            ],
            options={
                'db_table': 'project_flowmodel',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeoTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField(validators=[django.core.validators.MinValueValidator(-85.05115), django.core.validators.MaxValueValidator(85)])),
                ('lon', models.FloatField(validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('geography', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, geography=True, blank=True)),
                ('azimuth', models.FloatField(null=True, blank=True)),
                ('azimuth_line_end_lat', models.FloatField(null=True, blank=True)),
                ('azimuth_line_end_lon', models.FloatField(null=True, blank=True)),
                ('zoom_level', models.IntegerField(null=True, blank=True)),
                ('origin', models.PositiveSmallIntegerField(default=0, choices=[(0, 'M\xe4ng'), (1, 'Kaardivaade'), (2, 'Galerii')])),
                ('type', models.PositiveSmallIntegerField(default=0, choices=[(0, 'Kaart'), (1, 'EXIF'), (2, 'GPS'), (3, 'Kinnitus')])),
                ('map_type', models.PositiveSmallIntegerField(default=0, choices=[(0, 'Google kaart'), (1, 'Google satelliit'), (2, 'OpenStreetMap')])),
                ('hint_used', models.BooleanField(default=False)),
                ('is_correct', models.BooleanField(default=False)),
                ('azimuth_correct', models.BooleanField(default=False)),
                ('score', models.IntegerField(null=True, blank=True)),
                ('azimuth_score', models.IntegerField(null=True, blank=True)),
                ('trustworthiness', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'project_geotag',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GoogleMapsReverseGeocode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField(db_index=True, validators=[django.core.validators.MinValueValidator(-85.05115), django.core.validators.MaxValueValidator(85)])),
                ('lon', models.FloatField(db_index=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('response', django_extensions.db.fields.json.JSONField()),
            ],
            options={
                'db_table': 'project_googlemapsreversegeocode',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Licence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(null=True, blank=True)),
                ('image_url', models.URLField(null=True, blank=True)),
            ],
            options={
                'db_table': 'project_licence',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'uploads', width_field=b'width', height_field=b'height', max_length=255, blank=True, null=True)),
                ('image_unscaled', models.ImageField(max_length=255, null=True, upload_to=b'uploads', blank=True)),
                ('height', models.IntegerField(null=True, blank=True)),
                ('width', models.IntegerField(null=True, blank=True)),
                ('flip', models.NullBooleanField()),
                ('invert', models.NullBooleanField()),
                ('stereo', models.NullBooleanField()),
                ('rotated', models.IntegerField(null=True, blank=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('date_text', models.CharField(max_length=255, null=True, blank=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('title_et', models.CharField(max_length=255, null=True, blank=True)),
                ('title_en', models.CharField(max_length=255, null=True, blank=True)),
                ('title_ru', models.CharField(max_length=255, null=True, blank=True)),
                ('title_fi', models.CharField(max_length=255, null=True, blank=True)),
                ('title_sv', models.CharField(max_length=255, null=True, blank=True)),
                ('title_nl', models.CharField(max_length=255, null=True, blank=True)),
                ('title_de', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('description_et', models.TextField(null=True, blank=True)),
                ('description_en', models.TextField(null=True, blank=True)),
                ('description_ru', models.TextField(null=True, blank=True)),
                ('description_fi', models.TextField(null=True, blank=True)),
                ('description_sv', models.TextField(null=True, blank=True)),
                ('description_nl', models.TextField(null=True, blank=True)),
                ('description_de', models.TextField(null=True, blank=True)),
                ('author', models.CharField(max_length=255, null=True, blank=True)),
                ('types', models.CharField(max_length=255, null=True, blank=True)),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('guess_level', models.FloatField(default=3)),
                ('lat', models.FloatField(blank=True, null=True, db_index=True, validators=[django.core.validators.MinValueValidator(-85.05115), django.core.validators.MaxValueValidator(85)])),
                ('lon', models.FloatField(blank=True, null=True, db_index=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('geography', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, geography=True, blank=True)),
                ('bounding_circle_radius', models.FloatField(null=True, blank=True)),
                ('address', models.CharField(max_length=255, null=True, blank=True)),
                ('azimuth', models.FloatField(null=True, blank=True)),
                ('confidence', models.FloatField(default=0, null=True, blank=True)),
                ('azimuth_confidence', models.FloatField(default=0, null=True, blank=True)),
                ('source_key', models.CharField(max_length=100, null=True, blank=True)),
                ('muis_id', models.CharField(max_length=100, null=True, blank=True)),
                ('muis_media_id', models.CharField(max_length=100, null=True, blank=True)),
                ('source_url', models.URLField(max_length=1023, null=True, blank=True)),
                ('first_rephoto', models.DateTimeField(null=True, blank=True)),
                ('latest_rephoto', models.DateTimeField(null=True, blank=True)),
                ('fb_object_id', models.CharField(max_length=255, null=True, blank=True)),
                ('fb_comments_count', models.IntegerField(default=0)),
                ('first_comment', models.DateTimeField(null=True, blank=True)),
                ('latest_comment', models.DateTimeField(null=True, blank=True)),
                ('geotag_count', models.IntegerField(default=0, db_index=True)),
                ('first_geotag', models.DateTimeField(null=True, blank=True)),
                ('latest_geotag', models.DateTimeField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('gps_accuracy', models.FloatField(null=True, blank=True)),
                ('gps_fix_age', models.FloatField(null=True, blank=True)),
                ('cam_scale_factor', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.5), django.core.validators.MaxValueValidator(4.0)])),
                ('cam_yaw', models.FloatField(null=True, blank=True)),
                ('cam_pitch', models.FloatField(null=True, blank=True)),
                ('cam_roll', models.FloatField(null=True, blank=True)),
                ('area', models.ForeignKey(related_name='areas', blank=True, to='ajapaik.Area', null=True)),
                ('device', models.ForeignKey(blank=True, to='ajapaik.Device', null=True)),
                ('licence', models.ForeignKey(blank=True, to='ajapaik.Licence', null=True)),
                ('rephoto_of', models.ForeignKey(related_name='rephotos', blank=True, to='ajapaik.Photo', null=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'project_photo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhotoComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fb_comment_id', models.CharField(unique=True, max_length=255)),
                ('fb_object_id', models.CharField(max_length=255)),
                ('fb_comment_parent_id', models.CharField(max_length=255, null=True, blank=True)),
                ('fb_user_id', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('created', models.DateTimeField()),
                ('photo', models.ForeignKey(related_name='comments', to='ajapaik.Photo')),
            ],
            options={
                'db_table': 'project_photocomment',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhotoMetadataUpdate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('old_title', models.CharField(max_length=255, null=True, blank=True)),
                ('new_title', models.CharField(max_length=255, null=True, blank=True)),
                ('old_description', models.TextField(null=True, blank=True)),
                ('new_description', models.TextField(null=True, blank=True)),
                ('old_author', models.CharField(max_length=255, null=True, blank=True)),
                ('new_author', models.CharField(max_length=255, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ForeignKey(related_name='metadata_updates', to='ajapaik.Photo')),
            ],
            options={
                'db_table': 'project_photometadataupdate',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.PositiveSmallIntegerField(choices=[(0, b'Geotag'), (1, b'Rephoto'), (2, b'Photo upload'), (3, b'Photo curation')])),
                ('points', models.IntegerField(default=0)),
                ('created', models.DateTimeField(db_index=True)),
                ('geotag', models.ForeignKey(blank=True, to='ajapaik.GeoTag', null=True)),
                ('photo', models.ForeignKey(blank=True, to='ajapaik.Photo', null=True)),
            ],
            options={
                'db_table': 'project_points',
                'verbose_name_plural': 'Points',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fb_name', models.CharField(max_length=255, null=True, blank=True)),
                ('fb_link', models.CharField(max_length=255, null=True, blank=True)),
                ('fb_id', models.CharField(max_length=100, null=True, blank=True)),
                ('fb_token', models.CharField(max_length=511, null=True, blank=True)),
                ('fb_hometown', models.CharField(max_length=511, null=True, blank=True)),
                ('fb_current_location', models.CharField(max_length=511, null=True, blank=True)),
                ('fb_birthday', models.DateField(null=True, blank=True)),
                ('fb_email', models.CharField(max_length=255, null=True, blank=True)),
                ('fb_user_friends', models.TextField(null=True, blank=True)),
                ('google_plus_id', models.CharField(max_length=100, null=True, blank=True)),
                ('google_plus_email', models.CharField(max_length=255, null=True, blank=True)),
                ('google_plus_link', models.CharField(max_length=255, null=True, blank=True)),
                ('google_plus_name', models.CharField(max_length=255, null=True, blank=True)),
                ('google_plus_token', models.TextField(null=True, blank=True)),
                ('google_plus_picture', models.CharField(max_length=255, null=True, blank=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('score', models.PositiveIntegerField(default=0)),
                ('score_rephoto', models.PositiveIntegerField(default=0)),
                ('score_recent_activity', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'project_profile',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ForeignKey(to='ajapaik.Photo')),
                ('user', models.ForeignKey(related_name='skips', to='ajapaik.Profile')),
            ],
            options={
                'db_table': 'project_skip',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
                'db_table': 'project_source',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='points',
            name='user',
            field=models.ForeignKey(related_name='points', to='ajapaik.Profile'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='points',
            unique_together=set([('user', 'geotag')]),
        ),
        migrations.AddField(
            model_name='photo',
            name='source',
            field=models.ForeignKey(blank=True, to='ajapaik.Source', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(related_name='photos', blank=True, to='ajapaik.Profile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='geotag',
            name='photo',
            field=models.ForeignKey(related_name='geotags', to='ajapaik.Photo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='geotag',
            name='user',
            field=models.ForeignKey(related_name='geotags', to='ajapaik.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flipfeedback',
            name='photo',
            field=models.ForeignKey(to='ajapaik.Photo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flipfeedback',
            name='user_profile',
            field=models.ForeignKey(to='ajapaik.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='difficultyfeedback',
            name='geotag',
            field=models.ForeignKey(to='ajapaik.GeoTag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='difficultyfeedback',
            name='photo',
            field=models.ForeignKey(to='ajapaik.Photo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='difficultyfeedback',
            name='user_profile',
            field=models.ForeignKey(to='ajapaik.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='albumphoto',
            name='photo',
            field=models.ForeignKey(to='ajapaik.Photo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='cover_photo',
            field=models.ForeignKey(blank=True, to='ajapaik.Photo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(related_name='albums', through='ajapaik.AlbumPhoto', to='ajapaik.Photo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='profile',
            field=models.ForeignKey(related_name='albums', blank=True, to='ajapaik.Profile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='subalbum_of',
            field=models.ForeignKey(related_name='subalbums', blank=True, to='ajapaik.Album', null=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='CSVPhoto',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('ajapaik.photo',),
        ),
    ]
