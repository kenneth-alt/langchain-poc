import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain.chains.api.prompt import API_RESPONSE_PROMPT
from langchain.chains import APIChain
from langchain.prompts.prompt import PromptTemplate
from langchain.chains.api import open_meteo_docs
from apikey import apikey
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY']=apikey

llm = OpenAI(temperature=0, verbose=True)

chain_new=APIChain.from_llm_and_api_docs(llm, open_meteo_docs.OPEN_METEO_DOCS, verbose=True)

app = FastAPI()
origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


class Item(BaseModel):
    query:str
    
    
@app.get('/')
def reading():
    return {"hello from server"}

@app.post('/')
def meteo(item:Item):
    try:
        response=chain_new.run(item.query)
        return response
        
    except:
        return {"message": "Something went wrong with the server!"}

