from flask import Flask, request

from repositories.games_repository import GamesRepository
from repositories.users_repository import UsersRepository
from repositories.sales_repository import SalesRepository

from operator import itemgetter

app = Flask(__name__)

@app.route("/api/login", methods=['GET'])
def login():

    email = request.args.get('email', type=str)
    password = request.args.get('password', type=int)

    if not email or not password:
        return "Invalid parameters.", 400

    repository = UsersRepository()
    user = repository.get_user(email)

    if not user:
        return "No user found", 400

    if password == user.get('password'):
        return "Invalid password.", 403

    return user, 200

@app.route("/api/get-games", methods=['GET'])
def get_games():

    order_by_price = request.args.get('order_by_price', type=int)
    order_by_score = request.args.get('order_by_score', type=int)
    order_by_alphabetic = request.args.get('order_by_alphabetic', type=int)

    repository = GamesRepository()
    games = repository.get_all_games()

    if not games:
        return "No games found.", 400

    if order_by_price:
        games = sorted(games, key=itemgetter('price'))

    if order_by_score:
        games = sorted(games, key=itemgetter('score'))

    if order_by_alphabetic:
        games = sorted(games, key=itemgetter('name'))

    return games, 200

@app.route("/api/get-sales", methods=['GET'])
def get_sales():

    user_id = request.args.get('user_id', type=int)

    if not user_id:
        return "Invalid Parameters.", 400

    repository = SalesRepository()
    sales = repository.get_all_sales(user_id)

    if not sales:
        return "No sales found.", 400

    return sales, 200


@app.route("/api/new-sale", methods=['POST'])
def new_sales():

    sale_total = request.args.get('sale_total', type=float)
    user_id = request.args.get('user_id', type=int)
    game_id = request.args.get('game_id', type=int)

    if not sale_total or not user_id or not game_id:
        return "Invalid Parameters.", 400

    repository = SalesRepository()
    sale = repository.insert_new_sale(sale_total,user_id, game_id)

    if not sale:
        return "No sale inserted.", 400

    return "New sale inserted successfully", 200