from flask_restful import Resource
from flask import jsonify, request, json
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.Order import Order, OrderSchema
from helpers.api import custom_json_response

order_schema = OrderSchema()


class OrderResource(Resource):
    @jwt_required
    def put(self, id):
        req_body = request.get_json()
        order = Order.get_by_id(id)
        order.fulfill(req_body.get("clientSecret"))
        return custom_json_response({"message": "order created"}, 201)

    @jwt_required
    def get(self, id):
        order = Order.get_by_id(id)
        return order_schema.dump(order)