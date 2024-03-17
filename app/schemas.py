from marshmallow import fields, Schema

class UserSchema(Schema):
    user_id = fields.String()
    username = fields.String()
    email = fields.String()
    