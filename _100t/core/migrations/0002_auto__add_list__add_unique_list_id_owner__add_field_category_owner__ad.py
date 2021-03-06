# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'List'
        db.create_table(u'core_list', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'core', ['List'])

        # Adding unique constraint on 'List', fields [u'id', 'owner']
        db.create_unique(u'core_list', [u'id', 'owner_id'])

        # Adding field 'Category.owner'
        db.add_column(u'core_category', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)

        # Adding unique constraint on 'Category', fields [u'id', 'owner']
        db.create_unique(u'core_category', [u'id', 'owner_id'])

        # Adding field 'Item.item_list'
        db.add_column(u'core_item', 'item_list',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.List']),
                      keep_default=False)

        # Adding unique constraint on 'Item', fields ['index', 'sub_index', 'item_list']
        db.create_unique(u'core_item', ['index', 'sub_index', 'item_list_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Item', fields ['index', 'sub_index', 'item_list']
        db.delete_unique(u'core_item', ['index', 'sub_index', 'item_list_id'])

        # Removing unique constraint on 'Category', fields [u'id', 'owner']
        db.delete_unique(u'core_category', [u'id', 'owner_id'])

        # Removing unique constraint on 'List', fields [u'id', 'owner']
        db.delete_unique(u'core_list', [u'id', 'owner_id'])

        # Deleting model 'List'
        db.delete_table(u'core_list')

        # Deleting field 'Category.owner'
        db.delete_column(u'core_category', 'owner_id')

        # Deleting field 'Item.item_list'
        db.delete_column(u'core_item', 'item_list_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.category': {
            'Meta': {'unique_together': "(('id', 'owner'),)", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'core.item': {
            'Meta': {'unique_together': "(('index', 'sub_index', 'item_list'),)", 'object_name': 'Item'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {}),
            'is_set': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'item_list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.List']"}),
            'own_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'parent_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Item']", 'null': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sub_index': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'core.list': {
            'Meta': {'unique_together': "(('id', 'owner'),)", 'object_name': 'List'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['core']