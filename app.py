from flask import Flask

app = Flask(__name__)


from api import bp
app.register_blueprint(bp)




