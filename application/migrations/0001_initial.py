# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Payment'
        db.create_table(u'application_payment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('mode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('info', self.gf('django.db.models.fields.TextField')()),
            ('timestamp', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'application', ['Payment'])

        # Adding model 'Application'
        db.create_table(u'application_application', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('placeofbirth', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('religion', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('parent_one_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('parent_one_phone', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('parent_one_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('parent_two_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('parent_two_phone', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('parent_two_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('payment', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['application.Payment'], unique=True)),
        ))
        db.send_create_signal(u'application', ['Application'])


    def backwards(self, orm):
        # Deleting model 'Payment'
        db.delete_table(u'application_payment')

        # Deleting model 'Application'
        db.delete_table(u'application_application')


    models = {
        u'application.application': {
            'Meta': {'object_name': 'Application'},
            'dob': ('django.db.models.fields.DateField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'parent_one_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'parent_one_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'parent_one_phone': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'parent_two_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'parent_two_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'parent_two_phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'payment': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['application.Payment']", 'unique': 'True'}),
            'placeofbirth': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'application.payment': {
            'Meta': {'object_name': 'Payment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'mode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'timestamp': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['application']