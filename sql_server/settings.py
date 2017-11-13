SECRET_KEY = "django_tests_secret_key"

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'epp',                    # Or path to database file if using sqlite3.
        'HOST': 'ESSARCH-WIN2016\SQLEXPRESS',
    },
    'default': {
        'ENGINE': 'sql_server.pyodbc', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'etp',                    # Or path to database file if using sqlite3.
        'HOST': 'ESSARCH-WIN2016\SQLEXPRESS',
    },
}
print "asd"

