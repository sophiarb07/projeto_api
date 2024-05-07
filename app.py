from flask import Flask

app = Flask(_name_)


from api import bp
app.register_blueprint(bp)




