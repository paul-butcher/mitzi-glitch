from io import BytesIO
from flask import Flask
from flask import request
from mitzi import houndstooth

app = Flask(__name__)


@app.route("/houndstooth.png")
def get_image():
    buffer = BytesIO()

    img = houndstooth(request.args['c1'], request.args['c2'], request.args.get('size',6), (512, 512))
    img.save(buffer, "PNG")

    response = app.make_response(buffer.getvalue())
    response.mimetype = "image/png"
    return response


if __name__ == "__main__":
    app.run()