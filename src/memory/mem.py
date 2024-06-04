# src/memory/mem.py

import os
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain_text_splitters import CharacterTextSplitter
# from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_openai.llms.base import OpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import chromadb
from autogen.cache import Cache
# from langchain.chat_models import ChatOpenAI
from src.config.config import load_env_file

class Upsert:
    def __init__(self, file_path, chunk_size=1000, chunk_overlap=0, model_name="nomic-ai/nomic-embed-text-v1.5", persist_directory="./src/memory"):
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
        model_kwargs = {"trust_remote_code": True}
        # Create the embedding function
        embedding_function = HuggingFaceEmbeddings(model_name=self.model_name, model_kwargs=model_kwargs)

        # Load documents into Chroma database
        db = Chroma.from_texts(docs, embedding_function, persist_directory=self.persist_directory)
        return db

class Retriever:
    def __init__(self, persist_directory="./src/memory", model_name="nomic-ai/nomic-embed-text-v1.5"):
        self.model_name = model_name
        self.persist_directory = persist_directory
        self.model_kwargs = {"trust_remote_code": True}
        self.embeddings = HuggingFaceEmbeddings(model_name=self.model_name, model_kwargs=self.model_kwargs)



    def retrieve(self : str, query) -> str:
        # Load the pre-existing ChromaDB
        db = Chroma(persist_directory=self.persist_directory, embedding_function=self.embeddings)
        retriever = db.as_retriever()
        return retriever.invoke(query)[0]


def retrieve_query(query : str, persist_directory="./src/memory", search_type="mmr", model_name="nomic-ai/nomic-embed-text-v1.5") -> str :
    # Load environment variables from .env file using os library only
    load_env_file('./src/config/.env')
    
    # Ensure the OPENAI_API_KEY is set
    if "OPENAI_API_KEY" not in os.environ:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")
    
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    llm = ChatOpenAI(model_name="gpt-4", temperature=0.9, openai_api_key=OPENAI_API_KEY)
    embeddings = HuggingFaceEmbeddings(model_name=model_name, model_kwargs={"trust_remote_code": True})
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    qa = RetrievalQA.from_chain_type(return_source_documents = True, llm=llm, chain_type="stuff", retriever=vectordb.as_retriever())
    return qa(query)['result']