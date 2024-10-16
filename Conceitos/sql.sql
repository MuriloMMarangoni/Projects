'A database is a file that ends in .db'
'sql is the language used to interact with the database'
/*sqlite_master is a table with metadata, its included when using sqlite3*/
"SELECT name FROM sqlite_master WHERE type='table';"
/*PRAGMA returns rows with 6 columns, each row contains info about  the columns of the table
the order is (number of column,name,datatype,notnull,defaultvalue,primarykey)*/
"PRAGMA table_info(tabela)"
/* PRIMARY KEY sets autoincrement automatically and ignores DEFAULT values*/
/* Atualiza dados de uma tabela, mudando o id onde a coluna é algo*/
/*Updates in table the ID column , setting to 10 in the row where column A is str*/
"UPDATE tabela SET id=10 where a='str'"
