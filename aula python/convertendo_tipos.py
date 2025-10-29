from flask import Flask, render_template, request
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
import openai 
import os

openai.api_key = os.getenv("OPENAI_API_KEY") 
response = openai.ChatCompletion(
    model = "gpt-3.5-turbo",
    messages =[
        {"role":"system","content": "voce e um assistente util."},
        {"role": "user", "content": "como funciona a API do ChatGPT?"}
    ]
)

print(response["choices"][0]['message']["content"])

texto_base = """
A Programação Orientada a Objetos (POO) é um paradigma de programação baseado na
ideia de "objetos", que representam entidades do mundo real e são compostos por
atributos (características) e métodos (comportamentos). Diferente da
programação estruturada, que foca em funções e estruturas de controle, a POO
organiza o código de maneira mais modular e reutilizável. Os quatro pilares
fundamentais da POO são: abstração, encapsulamento, herança e polimorfismo.
A abstração permite representar conceitos complexos com simplicidade, 
escondendo os detalhes internos e expondo apenas o necessário. 
O encapsulamento assegura que os dados de um objeto sejam protegidos contra
alterações externas indevidas, favorecendo a segurança e a integridade da
informação. A herança possibilita que uma classe herde características de
outra, promovendo o reaproveitamento de código e a criação de hierarquias.
Já o polimorfismo permite que objetos diferentes respondam de maneira
distinta à mesma mensagem, aumentando a flexibilidade e a extensibilidade
dos sistemas. A POO é amplamente utilizada em linguagens como Java, Python,
C++, C# e Ruby, e é essencial no desenvolvimento de aplicações modernas, 
desde sistemas corporativos até jogos e aplicações móveis. Adotar a POO 
melhora a organização do código, facilita a manutenção e torna o 
desenvolvimento mais intuitivo e colaborativo.
"""

# Criação de embeddings e banco de dados de vetores
embeddings = OpenAIEmbeddings(OPENAI_API_KEY=OpenAI)
db = Chroma.from_texts([texto_base], embeddings)

# Criar a cadeia de perguntas e respostas
retriever = db.as_retriever()
qa_chain = ConversationalRetrievalChain.from_llm(llm=OpenAI(OPENAI_API_KEY=OpenAI), retriever=retriever)

# Configuração do Flask
app = Flask(__name__)

# Rota principal
@app.route("/", methods=["GET", "POST"])
def index():
    historico = []
    resposta = None
    if request.method == "POST":
        pergunta = request.form.get("pergunta")
        if pergunta:
            resultado = qa_chain({"question": pergunta, "chat_history": historico})
            resposta = resultado["answer"]
            historico.append((pergunta, resposta))
    return render_template("aula1 copy.html", resposta=resposta)

if __name__ == "__main__":
    app.run(debug=True)







