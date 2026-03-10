from datetime import datetime, timezone
from flask import jsonify, abort
from flask_smorest import Blueprint

from .schemas import SensorDataSchema, ReceiverHeadersSchema
from .settings import RECEIVER_PASSWORD

blp = Blueprint("sensor", "Sensor", url_prefix="/", description="Sensor data endpoints")

sensor_readings = []


@blp.route("/")
@blp.doc(summary="Health check", description="Returns a simple status response to verify the server is running.")
def index_view():
    return jsonify({"status": "ok"})


@blp.route("/receiver", methods=["POST"])
@blp.arguments(ReceiverHeadersSchema, location="headers")
@blp.arguments(SensorDataSchema)
@blp.doc(summary="Receive sensor data", description="Accepts sensor readings (temperature, humidity, etc.) sent by a Raspberry Pi.")
def receiver_view(headers, sensor_data):
    if headers.get("X_Password") != RECEIVER_PASSWORD:
        abort(401)
    sensor_data["timestamp"] = datetime.now(timezone.utc).isoformat()
    sensor_readings.append(sensor_data)
    return jsonify({"status": "ok", "received": sensor_data})


@blp.route("/dashboard")
@blp.doc(summary="Get all sensor readings", description="Returns the full list of sensor readings collected since the server started.")
def dashboard_view():
    return jsonify(sensor_readings)


@blp.route("/clear", methods=["DELETE"])
@blp.arguments(ReceiverHeadersSchema, location="headers")
@blp.doc(summary="Clear all sensor readings", description="Deletes all stored sensor readings from memory. Requires password.")
def clear_view(headers):
    if headers.get("X_Password") != RECEIVER_PASSWORD:
        abort(401)
    sensor_readings.clear()
    return jsonify({"status": "ok", "message": "All readings cleared"})