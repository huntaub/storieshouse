# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Episode.podcast'
        db.add_column('podcast_episode', 'podcast',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['podcast.Podcast']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Episode.podcast'
        db.delete_column('podcast_episode', 'podcast_id')


    models = {
        'podcast.episode': {
            'Meta': {'object_name': 'Episode'},
            'audio': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'data_published': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'podcast': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['podcast.Podcast']"}),
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