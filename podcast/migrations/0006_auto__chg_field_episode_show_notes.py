# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Episode.show_notes'
        db.alter_column('podcast_episode', 'show_notes', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'Episode.show_notes'
        db.alter_column('podcast_episode', 'show_notes', self.gf('django.db.models.fields.TextField')(default=' '))

    models = {
        'podcast.episode': {
            'Meta': {'object_name': 'Episode'},
            'audio': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'data_published': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'podcast': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['podcast.Podcast']"}),
            'show_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'podcast.podcast': {
            'Meta': {'object_name': 'Podcast'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'schedule': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['podcast']