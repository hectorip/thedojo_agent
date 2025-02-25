import pinecone
import os
from langchain.embeddings import OpenAIEmbeddings

openai = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

# load all files from docs/_posts

# all_files = glob.glob("./docs/_posts/*.md")

loaders = []

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
    environment="asia-southeast1-gcp",
)

# for f in all_files:
#     print("Loading file: ", f)
#     loader = TextLoader(f)
#     loaders.append(loader)


# loader = PyPDFLoader("LISR.pdf")


# index = VectorstoreIndexCreator(
#     vectorstore_cls=Pinecone,
#     vectorstore_kwargs={"index_name": "thedojo-agent"},
# ).from_loaders([loader])
vectorstore = pinecone.Index("thedojo-agent")


while True:
    query = input("Pregúntale a ley del ISR: ")
    if not query:
        break

    result = vectorstore.query(
        vector=openai.embed_query(query),
        top_k=5,
        include_values=True
        # include_metadata=True,
    )
