from marshmallow import Schema, fields


class SensorDataSchema(Schema):
    temperature = fields.Float(required=True)
    humidity = fields.Float(required=True)


class ReceiverHeadersSchema(Schema):
    X_Password = fields.String(
        required=True,
        data_key="X-Password",
        metadata={"description": "Password to authorize posting sensor data."},
    )