from configparser import ConfigParser


class Config:

    def __init__(self):
        self.parser = ConfigParser()
        self.parser.read("./config.ini")


class DatabaseConfig(Config):

    def __init__(self):
        super().__init__()
        self.config = self.parser["Database"]
        self.postgres_database = self.config.get("postgres_database")
        self.postgres_user = self.config.get("postgres_user")
        self.postgres_password = self.config.get("postgres_password")
        self.postgres_host = self.config.get("postgres_host")
        self.postgres_port = self.config.get("postgres_port")
        self.postgres_schema = self.config.get("postgres_schema")
