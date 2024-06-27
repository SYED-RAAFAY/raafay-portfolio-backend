from makeVectorEmbeddings import generateEmbeddings
from pinecone import Pinecone
import base64
import uuid
import os
import csv

pc = Pinecone(api_key='28f36123-4f64-44da-a22a-a3b8ffd5c2d1')

pinecone_index = pc.Index('resume-vectors')


def get_a_uuid():
    r_uuid = base64.standard_b64encode(uuid.uuid4().bytes)
    return r_uuid.decode().replace("=", "")


def read_data(name):
    # Read data from the CSV file into a list
    data = []
    print(os.path.exists("input_data/" + name + ".csv"))
    with open("input_data/" + name + ".csv", mode='r') as file:
        reader = csv.reader(file)

        for row in reader:
            data.append(row[0])
    return data


def upsert_pinecone(name):
    data = read_data(name)
    count = 1
    for line in data:
        print(count)
        meta = {'text': line, "name": name}
        embeddings = generateEmbeddings(line)
        vid = get_a_uuid()
        to_upsert = [{"id": vid, "values": embeddings, "metadata": meta}]
        pinecone_index.upsert(vectors=to_upsert)
        count += 1
    return


def retrieve_vectors_pinecone(vectorOfQuery, name):
    # print("query: ", query)
    print(vectorOfQuery)
    vectors = vectorOfQuery.tolist()
    print(name)
    try:
        query_response = pinecone_index.query(vector=vectors,
                                              filter={
                                                  "name": {"$eq": name}
                                              },
                                              top_k=10,
                                              include_metadata=True)
    except Exception as e:
        print(e)
    print("hi")
    matched_ids = []
    for match in query_response["matches"]:
        matched_ids.append(match["id"])

    fetch_response = pinecone_index.fetch(matched_ids)
    retrieved_chunks = []
    for matched_id in fetch_response["vectors"]:
        chunk = fetch_response["vectors"][matched_id]
        retrieved_chunks.append(chunk)

    passages = []
    for chunk in retrieved_chunks:
        x = chunk["metadata"].get("text", None)
        print(x)
        passages.append(x)
    return passages
