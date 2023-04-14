import glob
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

# from langchain.vectorstores import Pinecone
# import pinecone

# load all files from docs/_posts

all_files = glob.glob("./docs/_posts/*.md")

loaders = []

# pinecone.init(
#     api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
#     environment="asia-southeast1-gcp",
# )

for f in all_files:
    print("Loading file: ", f)
    loader = TextLoader(f)
    loaders.append(loader)

index = VectorstoreIndexCreator(
    # vectorstore_cls=Pinecone,
    # vectorstore_kwargs={"index_name": "thedojo-agent"},
).from_loaders(loaders)

while True:
    query = input("Pregúntale a The Dojo MX: ")
    if not query:
        break
    print(index.query_with_sources(query))
