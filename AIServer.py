from flask import Flask, request, jsonify

from groq import Groq

client = Groq(
    api_key="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",
)
app = Flask(__name__)
@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    question = data['question']
    context = data['context']
    if not isinstance(context, str):
        return jsonify({"error": "Context must be a string"}), 400
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question+"In the context of "+context,
            }
        ],
        model="mixtral-8x7b-32768",
    )
    return jsonify({"response": chat_completion.choices[0].message.content})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)