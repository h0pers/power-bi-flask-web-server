from app import app
from app.settings import DEBUG


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080, debug=DEBUG)