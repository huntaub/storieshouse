# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Podcast'
        db.create_table('podcast_podcast', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('podcast', ['Podcast'])

        # Adding model 'Episode'
        db.create_table('podcast_episode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('data_published', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('show_notes', self.gf('django.db.models.fields.TextField')()),
            ('audio', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('podcast', ['Episode'])


    def backwards(self, orm):
        # Deleting model 'Podcast'
        db.delete_table('podcast_podcast')

        # Deleting model 'Episode'
        db.delete_table('podcast_episode')


    models = {
        'podcast.episode': {
            'Meta': {'object_name': 'Episode'},
            'audio': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'data_published': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'show_notes': ('django.db.models.fields.TextField', [], {})
        },
        'podcast.podcast': {
            'Meta': {'object_name': 'Podcast'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['podcast']