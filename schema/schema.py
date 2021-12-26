from marshmallow import Schema, fields


class RateSchema(Schema):
    energy = fields.Float(required=True, data_key='energy')
    time = fields.Integer(required=True, data_key='time')
    transaction = fields.Integer(required=True, data_key='transaction')


class CDRSchema(Schema):
    meter_start = fields.Float(required=True, data_key='meterStart')
    meter_stop = fields.Float(required=True, data_key='meterStop')
    timestamp_start = fields.DateTime(required=True, data_key='timestampStart')
    timestamp_stop = fields.DateTime(required=True, data_key='timestampStop')


class RequestSchema(Schema):
    rate = fields.Nested(RateSchema, required=True, data_key='rate')
    cdr = fields.Nested(CDRSchema, required=True, data_key='cdr')
