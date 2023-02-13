import psycopg2

from utils.configs import DatabaseConfig


def connect_postgres():
    config = DatabaseConfig()

    try:
        connection = psycopg2.connect(
            dbname=config.postgres_database,
            user=config.postgres_user,
            password=config.postgres_password,
            host=config.postgres_host,
            port=config.postgres_port,
            options=f"-c search_path=dbo,{config.postgres_schema}"
        )

    except Exception as err:
        print(f"POSTGRES Connection ERROR: {err}")
        connection = None

    finally:
        return connection
