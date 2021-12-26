from flask import Flask, jsonify, request
from marshmallow import ValidationError
from http import HTTPStatus
from datetime import timedelta

from schema.schema import RequestSchema

app = Flask(__name__)


def validate_schema(data):
    schema = RequestSchema()
    try:
        return schema.load(data)
    except ValidationError as e:
        return jsonify(e.messages), HTTPStatus.BAD_REQUEST


def calculate_overall(data):
    consumed_energy = (data['cdr']['meter_stop'] - data['cdr']['meter_start']) / 1000
    consumed_time = data['cdr']['timestamp_stop'] - data['cdr']['timestamp_start']

    energy_fee = consumed_energy * data["rate"]["energy"]
    time = (consumed_time.seconds / 3600) * data["rate"]["time"]
    service_fee = data["rate"]["transaction"]
    overall = energy_fee + time + service_fee

    return energy_fee, time, service_fee, overall


@app.route("/rate", methods=['POST'])
def rate():
    """
    Example:
        input:
            {
              "rate": {
                "energy": 0.3,
                "time": 2,
                "transaction": 1
              },
              "cdr": {
                "meterStart": 1204307,
                "timestampStart": "2021-04-05T10:04:00Z",
                "meterStop": 1215230,
                "timestampStop": "2021-04-05T11:27:00Z"
              }
            }

        :return:
            {
              "overall": 7.04,
              "components": {
                "energy": 3.277,
                "time": 2.767,
                "transaction": 1
              }
            }
    """
    data = validate_schema(request.get_json())
    energy_fee, time, service_fee, overall = calculate_overall(data=data)
    return jsonify({'overall': round(overall, 2),
                    "components": {
                        "energy": round(energy_fee, 3),
                        "time": round(time, 3),
                        "transaction": service_fee}
                    }), HTTPStatus.OK


if __name__ == "__main__":
    app.run()
