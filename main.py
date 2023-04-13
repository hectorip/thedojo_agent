from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

loader = TextLoader("./docs/_posts/2023-04-07-cuando-separar-el-codigo.md")
index = VectorstoreIndexCreator().from_loaders([loader])


query = "¿Cuándo separar el código?"
print(index.query(query))

query = "¿Qué es un módulo?"
print(index.query_with_sources(query))
