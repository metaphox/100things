# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'ListItem', fields ['item_list', 'item', 'item_index']
        db.delete_unique(u'core_listitem', ['item_list_id', 'item_id', 'item_index'])

        # Deleting model 'ListItem'
        db.delete_table(u'core_listitem')

        # Removing M2M table for field item_categories on 'ListItem'
        db.delete_table(db.shorten_name(u'core_listitem_item_categories'))

        # Adding model 'Enlist'
        db.create_table(u'core_enlist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Item'])),
            ('item_list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.List'])),
            ('item_index', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'core', ['Enlist'])

        # Adding M2M table for field item_categories on 'Enlist'
        m2m_table_name = db.shorten_name(u'core_enlist_item_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('enlist', models.ForeignKey(orm[u'core.enlist'], null=False)),
            ('category', models.ForeignKey(orm[u'core.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['enlist_id', 'category_id'])

        # Adding unique constraint on 'Enlist', fields ['item_list', 'item', 'item_index']
        db.create_unique(u'core_enlist', ['item_list_id', 'item_id', 'item_index'])


    def backwards(self, orm):
        # Removing unique constraint on 'Enlist', fields ['item_list', 'item', 'item_index']
        db.delete_unique(u'core_enlist', ['item_list_id', 'item_id', 'item_index'])

        # Adding model 'ListItem'
        db.create_table(u'core_listitem', (
            ('item_list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.List'])),
            ('item_index', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Item'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['ListItem'])

        # Adding M2M table for field item_categories on 'ListItem'
        m2m_table_name = db.shorten_name(u'core_listitem_item_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('listitem', models.ForeignKey(orm[u'core.listitem'], null=False)),
            ('category', models.ForeignKey(orm[u'core.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['listitem_id', 'category_id'])

        # Adding unique constraint on 'ListItem', fields ['item_list', 'item', 'item_index']
        db.create_unique(u'core_listitem', ['item_list_id', 'item_id', 'item_index'])

        # Deleting model 'Enlist'
        db.delete_table(u'core_enlist')

        # Removing M2M table for field item_categories on 'Enlist'
        db.delete_table(db.shorten_name(u'core_enlist_item_categories'))


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
        u'core.enlist': {
            'Meta': {'unique_together': "(('item_list', 'item', 'item_index'),)", 'object_name': 'Enlist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Item']"}),
            'item_categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Category']", 'symmetrical': 'False'}),
            'item_index': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'item_list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.List']"})
        },
        u'core.item': {
            'Meta': {'object_name': 'Item'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_set': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'own_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'parent_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Item']", 'null': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sub_index': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'core.list': {
            'Meta': {'ordering': "('created',)", 'unique_together': "(('id', 'owner'),)", 'object_name': 'List'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Item']", 'through': u"orm['core.Enlist']", 'symmetrical': 'False'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['core']