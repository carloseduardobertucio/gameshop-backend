from repositories.base_repository import BasePostgresRepository

from psycopg2.extras import RealDictCursor


class UsersRepository(BasePostgresRepository):

    def get_user(self, email):
        sql = f"""
            SELECT
            	*
            FROM
            	users u
            WHERE
                email = '{email}'
        """

        self.open_connection()

        try:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()

        except Exception as err:
            print(
                f"An error occurred when trying to get users. \n"
                f"Error: {err}"
            )
            result = False

        finally:
            self.close_connection()
            return result
