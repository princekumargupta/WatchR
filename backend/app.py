from flask import Flask, jsonify
from censys import censys_ip
from instagram import Instagram
from hunter import hunterIo
from phone import phoneinfo
from insta import instgrm


app = Flask(__name__)

@app.route("/")
def fun_home():
    return "Hello World"

@app.route("/1/<string:censys_input>")
def fun_censys(censys_input):
    if censys_ip(censys_input) != None :
        return jsonify(censys_ip(censys_input))
    else :
        return None

@app.route("/2/<string:first>/<string:last>/<string:domain>")
def fun_ins(first, last, domain):
    if hunterIo(first, last, domain) != None :
        return jsonify(hunterIo(first, last, domain))
    else :
        return None  

@app.route("/3/<string:phone_input>")
def fun_phone(phone_input):
    if phoneinfo(phone_input) != None :
        return phoneinfo(phone_input)
    else :
        return None

@app.route("/4/<string:insta_usrnm>")
def fun_insta(insta_usrnm):
    if instgrm(insta_usrnm) != None :
        return jsonify(instgrm(insta_usrnm))
    else :
        return None    


if __name__ == "__main__":
    app.run(debug=True, host="watchrosint51.herokuapp.com")
