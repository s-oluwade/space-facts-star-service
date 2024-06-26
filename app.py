from flask import Flask, jsonify
import random

app = Flask(__name__)

facts = [
    "The Sun is a middle-aged star and has been shining for about 4.6 billion years.",
    "Betelgeuse is a red supergiant star approximately 700 light-years from Earth.",
    "Neutron stars are the remnants of massive stars that have exploded in supernovae."
]

@app.route('/star-fact', methods=['GET'])
def get_star_fact():
    fact = random.choice(facts)
    return jsonify({"fact": fact})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
