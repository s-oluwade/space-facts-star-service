from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def star_facts():
    facts = [
        {"name": "Sun", "fact": "The Sun is the star at the center of the Solar System."},
        {"name": "Sirius", "fact": "Sirius is the brightest star in the night sky."},
        {"name": "Betelgeuse", "fact": "Betelgeuse is a red supergiant star in the constellation Orion."},
        {"name": "Polaris", "fact": "Polaris is known as the North Star."},
        {"name": "Neutron", "fact": "Neutron stars are the remnants of massive stars that have exploded in supernovae."},
    ]
    return render_template('index.html', title="Star Facts", facts=facts)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

