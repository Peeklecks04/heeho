from flask import *
import dataset

app = Flask(__name__)
app.secret_key = "Regigigas (Japanese: レジギガス Regigigas) is a Normal-type Legendary Pokémon introduced in Generation IV. Regigigas is a large, white, golem-like Pokémon with seven black circular eyes arranged in a specific pattern. The pattern is Regigigas's way of showing its anger; its eyes glow red when it is provoked. It has six spots that are apart from its eyes, which appear to be gemstones. These gemstones seem to represent the original three Legendary titans, with red gems representing Regirock, blue gems indicating Regice, and silver gems representing Registeel. Regigigas has long arms, with three fairly human-like white fingers, and short legs that end in large mossy bushes instead of feet. Regigigas has large yellow bands on its shoulders and wrists, with a sloping section on its chest that appears to be its head and is also yellow. Its body is covered in black stripes, and it has moss growing in its back and feet. Regigigas is a skilled craftsman. It created golems out of inanimate objects and elemental energies, bringing them to life. Regigigas is also capable of controlling these Legendary titans, even if they already belong to a different Trainer. It can also survive extreme conditions as it is able to work with the boiling temperatures of magma (1300-2400 °F [700-1300 °C]) as well as frigid ice (-328 °F [-200 °C]). When Regigigas is disturbed from its slumber, it goes on a rampage and shoots powerful beams of energy. When it is befriended, however, it is calm and gentle, as seen in Pillars of Friendship!. It is able to crush targets by using its signature move, Crush Grip. According to Sinnoh legend, Regigigas's strength enables it to move continents."


@app.route('/')
def heeho ():
    return render_template('hee-ho.html')

@app.route('/chat')
def chat (): 
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)
