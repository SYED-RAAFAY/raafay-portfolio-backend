from flask import Flask, jsonify, request
from makeVectorEmbeddings import generateQueryEmbeddings
from pineconeConnection import upsert_pinecone, retrieve_vectors_pinecone
from flask_cors import CORS
from gemini import callGemini

app = Flask(__name__)  # Flask constructor
CORS(app)

@app.route('/askQuestion', methods=['POST'])
def askQuestion():
    try:
        # Reading Request Body
        data = request.get_json()
        if not data:
            raise ValueError("No JSON data provided in the request")
        name = data.get('name')
        query = data.get('query')
        if not name:
            raise ValueError("'name' is missing in the JSON data")
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400  # Bad Request
    except Exception as e:
        return jsonify({"error": "Internal Server Error. Something went wrong while retrieving request data."}), 500
    try:
        # Retrieve chunks from pinecone_resources vector DB
        passages = retrieve_vectors_pinecone(generateQueryEmbeddings(query), name)
    except Exception as e:
        # logging.exception(f"Error occurred while retrieving vectors from pinecone_resources: {e}")
        return jsonify(
            {"error": "Error occurred while retrieving vectors from pinecone_resources."}), 500  # Internal Server Error

    context = ""
    for passage in passages:
        context = context + ", " + passage

    ans = callGemini(query, name, context)
    print(ans)
    response = {"answer": ans}
    print(response)
    return response


@app.route('/addResume', methods=['POST'])
def addResume():
    try:
        # Reading Request Body
        data = request.get_json()
        if not data:
            raise ValueError("No JSON data provided in the request")
        name = data.get('name')

        if not name:
            raise ValueError("'name' is missing in the JSON data")
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400  # Bad Request
    except Exception as e:
        return jsonify({"error": "Internal Server Error. Something went wrong while retrieving request data."}), 500

    value = upsert_pinecone(name)

    if value:
        return "Done", 200

    return "Done", 200


if __name__ == '__main__':
    app.run(port=5000)
