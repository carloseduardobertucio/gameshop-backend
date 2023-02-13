from repositories.base_repository import BasePostgresRepository

from psycopg2.extras import RealDictCursor


class GamesRepository(BasePostgresRepository):

    def get_all_games(self):
        sql = """
            SELECT
            	*
            FROM
            	games g
        """

        self.open_connection()

        try:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()

        except Exception as err:
            print(
                f"An error occurred when trying to get games. \n"
                f"Error: {err}"
            )
            result = False

        finally:
            self.close_connection()
            return result
