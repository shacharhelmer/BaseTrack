MYSQL_SCHEMA_TEMPLATE = 'mysqldump -u $user -d $dbname > $output_dir/$dbname.sql'
MYSQL_NO_DROP_FLAG = ' --skip-add-drop-table'
MYSQL_PROCEDURE_NAMES = 'SHOW PROCEDURE STATUS WHERE db = \'$dbname\''
MYSQL_SHOW_CREATE_PROCEDURE_TEMPLATE = 'SHOW CREATE PROCEDURE $spname'