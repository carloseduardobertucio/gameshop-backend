from connection.sql import connect_postgres


class BasePostgresRepository:

    def __init__(self):
        self.connection = None

    def open_connection(self):
        self.connection = connect_postgres()

    def close_connection(self):
        self.connection.close()
