from config.templates import *
from string import Template
from config.setup import load_conf
from os import system
from sqlalchemy import create_engine

def get_mysql_procedure_names(engine, db_name):
    res = engine.execute(Template(MYSQL_PROCEDURE_NAMES).substitute(dbname=db_name))
    return [value for row in res for column, value in row.items() if column == 'Name']

def get_mysql_create_procedure_query(engine, sp_name):
    res = engine.execute(Template(MYSQL_SHOW_CREATE_PROCEDURE_TEMPLATE).substitute(spname=sp_name))
    return [value for row in res for column, value in row.items() if column == 'Create Procedure'][0]

def mysqldump_command_setup(settings):
    command = MYSQL_SCHEMA_TEMPLATE
    if settings['tables']['no_drop_tables']:
        command += MYSQL_NO_DROP_FLAG
    return command

def main(output_dir):
    settings = load_conf()
    eng = create_engine(settings['db']['conn_string'])
    system(Template(mysqldump_command_setup(settings)).substitute(dbname=settings['db']['db_name'],
                                                                  output_dir=output_dir,
                                                                  user=settings['db']['user']))
    sps = get_mysql_procedure_names(engine=eng, db_name=settings['db']['db_name'])
    create_sp_queries = [get_mysql_create_procedure_query(engine=eng, sp_name=sp) for sp in sps]
    with open('{0}/stored_procedures-{1}.sql'
                      .format(output_dir, settings['db']['db_name']), 'w+') as sp_file:
        sp_file.write('DELIMITER //' + '\n')
        for create_sp_query in create_sp_queries:
            sp_file.write(create_sp_query + '//\n')
        sp_file.write('DELIMITER ;' + '\n')