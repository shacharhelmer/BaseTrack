MYSQL_SCHEMA_TEMPLATE = 'mysqldump -u $user -d $dbname > $output_dir/$dbname.sql'
MYSQL_NO_DROP_FLAG = ' --skip-add-drop-table'
MYSQL_PROCEDURE_NAMES = 'SHOW PROCEDURE STATUS WHERE db = \'$dbname\''
MYSQL_SHOW_CREATE_PROCEDURE = 'SHOW CREATE PROCEDURE $spname'
MYSQL_VIEW_NAMES = 'SELECT TABLE_NAME FROM information_schema.`TABLES` WHERE TABLE_TYPE LIKE "VIEW" AND TABLE_SCHEMA LIKE "$dbname";'
MYSQL_SHOW_CREATE_VIEW = 'SHOW CREATE VIEW $viewname'