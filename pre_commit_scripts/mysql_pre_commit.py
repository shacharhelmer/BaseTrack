from config.templates import *
from string import Template
from config.setup import load_conf
from os import system
from sqlalchemy import create_engine

def get_mysql_procedure_names(engine, db_name):
    res = engine.execute(Template(MYSQL_PROCEDURE_NAMES).substitute(dbname=db_name))
    return [value for row in res for column, value in row.items() if column == 'Name']

def get_mysql_create_procedure_query(engine, sp_name):
    res = engine.execute(Template(MYSQL_SHOW_CREATE_PROCEDURE).substitute(spname=sp_name))
    return [value for row in res for column, value in row.items() if column == 'Create Procedure'][0]

def get_mysql_views_names(engine, db_name):
    res = engine.execute(Template(MYSQL_VIEW_NAMES).substitute(dbname=db_name))
    return [value for r in res for column, value in r.items() if column == 'TABLE_NAME']

def get_mysql_create_view_query(engine, view_name):
    res = engine.execute(Template(MYSQL_SHOW_CREATE_VIEW).substitute(viewname=view_name))
    return [value for r in res for column, value in r.items() if column == 'Create View'][0]

def mysqldump_command_setup(settings):
    command = MYSQL_SCHEMA_TEMPLATE
    if settings['tables']['no_drop_tables']:
        command += MYSQL_NO_DROP_FLAG
    return command

def main(output_dir):
    settings = load_conf()
    eng = create_engine(settings['db']['conn_string'])
    # region schema
    system(Template(mysqldump_command_setup(settings)).substitute(dbname=settings['db']['db_name'],
                                                                  output_dir=output_dir,
                                                                  user=settings['db']['user']))
    # endregion schema

    # region stored_procedures
    sps = get_mysql_procedure_names(eng, settings['db']['db_name'])
    create_sp_queries = [get_mysql_create_procedure_query(eng, sp) for sp in sps]
    with open('{0}/stored_procedures-{1}.sql'.format(output_dir, settings['db']['db_name']), 'w+') as sp_file:
        sp_file.write('DELIMITER //' + '\n')
        for create_sp_query in create_sp_queries:
            sp_file.write(create_sp_query + '//\n')
        sp_file.write('DELIMITER ;' + '\n')
    # endregion stored_procedures

    # region views
    views = get_mysql_views_names(eng, settings['db']['db_name'])
    create_view_queries = [get_mysql_create_view_query(eng, view) for view in views]
    with open('{0}/views-{1}.sql'.format(output_dir, settings['db']['db_name']), 'w+') as views_file:
        for create_view_query in create_view_queries:
            views_file.write(create_view_query + ';\n')
    # endregion views
