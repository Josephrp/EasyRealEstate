import langchain_community
from langchain_community.document_loaders import UnstructuredExcelLoader

loader = UnstructuredExcelLoader(".\src\sources\LISTINGS.xlsx", mode="elements")
docs = loader.load()
docs[0]
