from templates import *
from string import Template
from setup import load_conf
from os import system


conf = load_conf()
system(Template(MYSQL_TEMPLATE).substitute(dbname=conf['db_settings']['db'],
                                          user=conf['db_settings']['user']))
