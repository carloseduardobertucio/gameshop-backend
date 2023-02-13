from repositories.base_repository import BasePostgresRepository

from psycopg2.extras import RealDictCursor
from datetime import datetime


class SalesRepository(BasePostgresRepository):

    def get_all_sales(self, user_id):
        sql = f"""
            SELECT
            	*
            FROM
            	sales
            WHERE
                id_user = '{user_id}'
        """

        self.open_connection()

        try:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()

        except Exception as err:
            print(
                f"An error occurred when trying to get sales. \n"
                f"Error: {err}"
            )
            result = False

        finally:
            self.close_connection()
            return result

    def insert_new_sale(self, sale_total, user_id, game_id):
        sql = f"""
            INSERT INTO
            	sales(sale_date, status, sale_total, id_user, id_game)
            VALUES
            	('{datetime.now().date()}', '{'PENDING'}', {sale_total}, {user_id}, {game_id})
        """

        self.open_connection()

        try:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(sql)
            
            self.connection.commit()
            result = True

        except Exception as err:
            print(
                f"An error occurred when trying to get sales. \n"
                f"Error: {err}"
            )
            self.connection.rollback()
            result = False

        finally:
            self.close_connection()
            return result