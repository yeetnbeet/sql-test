import os
import sqlalchemy
import pymysql


def connect_unix_socket() -> sqlalchemy.engine.base.Engine:
    """ Initializes a Unix socket connection pool for a Cloud SQL instance of MySQL. """
    # Note: Saving credentials in environment variables is convenient, but not
    # secure - consider a more secure solution such as
    # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    # keep secrets safe.
    db_user = os.getenv("DB_USER")  # e.g. 'my-database-user'
    db_pass = os.getenv("DB_PASS")  # e.g. 'my-database-password'
    db_name = os.getenv("DB_NAME")  # e.g. 'my-database'
    unix_socket_path = os.getenv("INSTANCE_UNIX_SOCKET")  # e.g. '/cloudsql/project:region:instance'

    pool = sqlalchemy.create_engine(
        # Equivalent URL:
        # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=<socket_path>/<cloud_sql_instance_name>
        sqlalchemy.engine.url.URL.create(
            drivername="mysql+pymysql",
            username=db_user,
            password=db_pass,
            database=db_name,
            query={"unix_socket": unix_socket_path},
        ),
        # ...
    )
    return pool

