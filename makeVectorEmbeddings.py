from sentence_transformers import SentenceTransformer

model = SentenceTransformer('intfloat/e5-large-v2')


def generateEmbeddings(line):
    # 'query: how much protein should a female eat',
    input_texts = [
        "passage: " + line + " "
    ]
    embeddings = model.encode(input_texts, normalize_embeddings=True)
    print(embeddings[0])
    return embeddings[0]


def generateQueryEmbeddings(query):
    input_texts = [
        'query: ' + query + ' '
    ]
    embeddings = model.encode(input_texts, normalize_embeddings=True)
    print(embeddings)
    return embeddings[0]
