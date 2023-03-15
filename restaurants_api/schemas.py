from marshmallow import Schema, fields


class RestaurantSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    sir = fields.Str(required=True)
    speciality = fields.Str(required=True)
    owner_id = fields.Str(required=True)
