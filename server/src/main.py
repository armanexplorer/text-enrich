import uvicorn
import os
import os.path   
from logs import LOGGER
from fastapi import FastAPI, File, UploadFile
from starlette.middleware.cors import CORSMiddleware
from milvus_helpers import MilvusHelper
from mysql_helpers import MySQLHelper
from operations.load import do_load
from operations.search import search_in_milvus
from operations.count import do_count
from operations.drop import do_drop
from logs import LOGGER
from encode import SentenceModel, LaserSentenceModel, LaBSESentenceModel
from pydantic import BaseModel
from typing import Optional, Tuple, List



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])
    
# MODEL = SentenceModel()
LASER_MODEL = LaserSentenceModel()
# LABSE_MODEL = LaBSESentenceModel()
MILVUS_CLI = MilvusHelper()
MYSQL_CLI = MySQLHelper()

class Item(BaseModel):
    Table: Optional[str] = None
    File:str

@app.post('/count')
async def count_text(table_name: str = None):
    # Returns the total number of titles in the system
    try:
        num = do_count(table_name, MILVUS_CLI)
        LOGGER.info("Successfully count the number of titles!")
        return num
    except Exception as e:
        LOGGER.error(e)
        return {'status': False, 'msg': e}, 400


@app.post('/drop')
async def drop_tables(table_name: str = None):
    # Delete the collection of Milvus and MySQL
    try:
        status = do_drop(table_name, MILVUS_CLI, MYSQL_CLI)
        LOGGER.info("Successfully drop tables in Milvus and MySQL!")
        return status
    except Exception as e:
        LOGGER.error(e)
        return {'status': False, 'msg': e}, 400


# @app.post('/load')
# async def load_text(file: UploadFile = File(...), table_name: str = None):
#     try:
#         # read file contents
#         text = await file.read()
        
#         # move the file to `data` directory
#         fname = file.filename
#         dirs = "data"
#         if not os.path.exists(dirs):
#             os.makedirs(dirs)
#         fname_path = os.path.join(os.getcwd(), os.path.join(dirs, fname))
#         with open(fname_path, 'wb') as f:
#             f.write(text)
            
#     except Exception :
#         return {'status': False, 'msg': 'Failed to load data.'}
#     # Insert all the image under the file path to Milvus/MySQL
#     try:
#         total_num = do_load(table_name, fname_path, LASER_MODEL, MILVUS_CLI, MYSQL_CLI)
#         LOGGER.info(f"Successfully loaded data, total count: {total_num}")
#         return "Successfully loaded data!"
#     except Exception as e:
#         LOGGER.error(e)
#         return {'status': False, 'msg': e}, 400


@app.get('/search')
async def do_search_api(table_name: str= None, query_sentence: str = None):
    try:
        if not table_name:
            table_names = MILVUS_CLI.list_collections()
        elif not isinstance(table_name, (List, Tuple)):
            table_names = [table_name]
            
        results = search_in_milvus(table_names, query_sentence, LASER_MODEL, MILVUS_CLI, MYSQL_CLI)
        LOGGER.info("Successfully searched similar text!")
        return results
    except Exception as e:
        LOGGER.error(e)
        return {'status': False, 'msg': e}, 400


if __name__ == "__main__":
    uvicorn.run(app=app, host='0.0.0.0', port=5000)
