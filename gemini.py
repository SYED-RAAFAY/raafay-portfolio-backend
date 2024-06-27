import google.generativeai as genai

genai.configure(api_key='AIzaSyCQfuMGceiOlbbgOkBVfhWsFFrX5ET8PGs')

model = genai.GenerativeModel('gemini-1.0-pro-latest')


def callGemini(query, name, data="Not received"):
    # print(data)
    prompt = ('You are a very helpfull bot which helps to answer questions based on resume content'
              'This are lines from the resume of ' + name + '\n' + data + '\n' +
              'answer the question' + " " + query + " " +
              'give answer to the question using only the most relevant line or lines from the resume, and answer in '
              'paragraph of at max 2-3 lines but try to be crisp in explaining the answer. Note: dont give direct '
              'lines from resume')
    # print(prompt)
    return generateResponse(prompt)


def generateResponse(data="Say Hi in multiple ways?"):
    response = model.generate_content(data)
    res = response.text
    return res
