# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Payment.amount'
        db.alter_column(u'application_payment', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2))
        # Adding field 'Application.status'
        db.add_column(u'application_application', 'status',
                      self.gf('django.db.models.fields.CharField')(default='PROCESSING', max_length=16),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'Payment.amount'
        db.alter_column(u'application_payment', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2))
        # Deleting field 'Application.status'
        db.delete_column(u'application_application', 'status')


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
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'PROCESSING'", 'max_length': '16'})
        },
        u'application.payment': {
            'Meta': {'object_name': 'Payment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'mode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'timestamp': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['application']