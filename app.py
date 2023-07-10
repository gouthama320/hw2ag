from flask import Flask, jsonify
import random

app = Flask(__name__)

choice = [
    "Why did the chicken cross the road? To get to the other side!",
    "Why did the boy cross the playground? To get to the other slide!",
    "Why did the skeleton not cross the road? It didn't have the guts!",
    "What do you call a pig that does karate? Pork Chop!",
    "What is 9 + 10? 19!",
    "Why did the bike fall over? It was two tired!",
    "Why did the man get hit by a bike every day? He was stuck in a vicious cycle.",
    "I used to play piano by ear, but now I use my hands.",
    "Why do seagulls fly over the sea? If they flew over the bay, they would be bagels.",
    "Why shouldn’t you write with a broken pen? Because it’s pointless."
]

@app.route('/joke_custom', methods = ['Get','Post'])
def joke_custom():
    joke = random.choice(choice)
    return jsonify({'joke': joke})

if __name__ == '__main__':
    app.run(port= 5000, host = '0.0.0.0')
