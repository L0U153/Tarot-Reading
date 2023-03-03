import os
import openai
import cards
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# render_template("index.html", src1 = "back.png")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        topic = request.form["topic"]
        cardInfo = tarot_prompt(3, topic)
        # src1 = url_for('static', filename=cardInfo[1])
        # TODO: Generate tarot cards
 
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = "You are a professional Tarot reader. Interpret and predict my " + topic + " detailedly from the combination of these three tarot cards:\n" + cardInfo[0],
            # messages = [
            #         # {"role": "system", "content": "You are a professional Tarot reader."},
            #         {"role": "user", "content": tarot_prompt(3, topic)}
            #     ]
                # ,
            temperature = 0.7,
            presence_penalty = 0.15,
            frequency_penalty = 0.1,
            max_tokens = 256
        )
        return redirect(url_for("index", result=response.choices[0].text))

     

    result = request.args.get("result")
    # src1 = url_for('static', filename=cardInfo[1])
    return render_template("index.html", result=result)


def tarot_prompt(n, topic):
    pmt = "Read my {} from the combination of these {} cards: \n" .format(topic, n)

    deck = cards.load()
    idx = cards.draw(n)
    src1 = deck[str(idx[0])][1]

    for i in range(n):
        pmt = pmt + cards.position() + deck[str(idx[i])][0] + "\n"

    # TODO: Update tarot image src
    
    return [pmt + ".", src1]