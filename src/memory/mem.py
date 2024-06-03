# src/memory/mem.py

import os
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
import chromadb

load_dotenv()

class Upsert:
    def __init__(self, file_path, chunk_size=1000, chunk_overlap=0, model_name="nomic-embed-text-v1.5", persist_directory="./src/memory"):
        self.file_path = file_path
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.model_name = model_name
        self.persist_directory = persist_directory

    def upsert_documents(self):
        # Load the documents from the Excel file
        loader = UnstructuredExcelLoader(self.file_path, mode="elements")
        documents = loader.load_and_split()

        # Split documents into chunks
        text_splitter = CharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        docs = text_splitter.split_documents(documents)

        # Create the embedding function
        embedding_function = SentenceTransformerEmbeddings(model_name=self.model_name)

        # Load documents into Chroma database
        db = chromadb.Chroma.from_documents(docs, embedding_function, persist_directory=self.persist_directory)
        return db

class Retriever:
    def __init__(self, persist_directory="./src/memory"):
        self.persist_directory = persist_directory

    def retrieve(self, query, search_type="mmr"):
        # Load the pre-existing ChromaDB
        db = chromadb.Chroma(persist_directory=self.persist_directory)
        retriever = db.as_retriever(search_type=search_type)
        return retriever.invoke(query)[0]


def retrieve_query(query, persist_directory="./src/memory", search_type="mmr"):
    retriever = Retriever(persist_directory=persist_directory)
    return retriever.retrieve(query, search_type)