#!/usr/bin/python3

from xmlrpc import client
url = 'http://localhost:8073'

dbname = 'test'      #Nombre DB
user = 'admin'       #usuario DB
pwd = 'admin'        #pass DB

common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
uid = common.authenticate(dbname, user, pwd, {})

country_ids = models.execute_kw(dbname, uid, pwd, 'master', 'search', [[['country_id', '=', 1]]])

for country_id in country_ids:
    models.execute_kw(dbname,uid,pwd,'master','write',[[country_id],{'country_id':2}])

