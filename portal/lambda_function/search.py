import json
from sqlalchemy.orm import Session
from typing import Annotated

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def lambda_handler(event, context):
    # database
    db = next(get_db())
    
    # query param
    
    major = event['queryStringParameters']['major']
    keyword = event['queryStringParameters']['keyword']
    condition = event['queryStringParameters']['condition']
    
    # fetch from table
    if condition == 'name':
        data = crud.get_portal_by_major_lecture_name(db=db, major=major, lecture_name=keyword)
    elif condition == 'professor':
        data = crud.get_portal_by_major_professor(db=db, major=major, name=keyword)
    # exception
    else:
        result = {'detail': 'Condition must be name or professor'}
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(result, ensure_ascii = False)
        }
        
    # sqlalchemy to pydantic model
    result = [schemas.Portal.model_validate(row) for row in data]
    
    print(data)
    real = [row.model_dump_json() for row in result]
    print(real)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps([res.dict() for res in result], ensure_ascii = False)
    }
