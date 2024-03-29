from marshmallow import Schema, fields

# Define a serializer schema for the Patient model
class PatientSchema(Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    date_of_birth = fields.Date(format='%Y-%m-%d', required=True)
    gender = fields.String(required=True)
    phone_number = fields.String(required=True)
    email = fields.Email(required=True)
    address = fields.String(required=True)
