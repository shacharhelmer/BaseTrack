from templates import *
from string import Template
from setup import load_conf
from os import system
from sqlalchemy import create_engine


def get_mysql_procedure_names(engine, db_name):
    res = engine.execute(Template(MYSQL_PROCEDURE_NAMES).substitute(dbname=db_name))
    return [value for row in res for column, value in row.items() if column == 'Name']

def get_mysql_create_procedure_query(engine, sp_name):
    res = engine.execute(Template(MYSQL_SHOW_CREATE_PROCEDURE_TEMPLATE).substitute(spname=sp_name))
    return [value for row in res for column, value in row.items() if column == 'Create Procedure'][0]

def main():
    db_settings = load_conf()['db_settings']
    eng = create_engine(db_settings['conn_string'])
    # mysql dump output
    system(Template(MYSQL_SCHEMA_TEMPLATE).substitute(dbname=db_settings['db'],
                                                      user=db_settings['user']))
    sps = get_mysql_procedure_names(engine=eng, db_name=db_settings['db'])
    create_sp_queries = [get_mysql_create_procedure_query(engine=eng, sp_name=sp) for sp in sps]
    with open(f'stored_procedures-{db_settings["db"]}', 'w'):
        for create_sp_query in create_sp_queries:
            pass


if __name__ == "__main__":
    main()