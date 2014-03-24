# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'core_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'core', ['Category'])

        # Adding model 'Item'
        db.create_table(u'core_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('index', self.gf('django.db.models.fields.IntegerField')()),
            ('sub_index', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_set', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('own_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('parent_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Item'], null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Item'])

        # Adding M2M table for field category on 'Item'
        m2m_table_name = db.shorten_name(u'core_item_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'core.item'], null=False)),
            ('category', models.ForeignKey(orm[u'core.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'core_category')

        # Deleting model 'Item'
        db.delete_table(u'core_item')

        # Removing M2M table for field category on 'Item'
        db.delete_table(db.shorten_name(u'core_item_category'))


    models = {
        u'core.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'core.item': {
            'Meta': {'object_name': 'Item'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {}),
            'is_set': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'own_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'parent_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Item']", 'null': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sub_index': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['core']