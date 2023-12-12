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
    
    major=None
    lecture_name=None
    skip=0
    limit=10
    
    if event["queryStringParameters"] is None:
        data=crud.get_portal_page(db=db, skip=skip, limit=limit)
        result=[schemas.Portal.model_validate(row) for row in data]
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps([res.dict() for res in result], ensure_ascii = False)
        }
        
    
    if "major" in event['queryStringParameters'].keys(): major = event['queryStringParameters']['major']
    
    if "lecture_name" in event['queryStringParameters'].keys():
        lecture_name = event['queryStringParameters']['lecture_name'].split(",")
        print("lecture_name", lecture_name)
    
    if "skip" in event['queryStringParameters'].keys():
        skip = int(event['queryStringParameters']['skip'])
        
    if "limit" in event['queryStringParameters'].keys():
        limit = int(event['queryStringParameters']['limit'])
    

    if major is not None and lecture_name is not None:
        print(major, lecture_name)
        data=crud.get_portal_page_by_major_multiple_lecture_name(db=db, major=major, lecture_name=lecture_name, skip=skip, limit=limit)
    elif major is not None:
        data=crud.get_portal_page_by_major(db=db, major=major, skip=skip, limit=limit)
    elif lecture_name is not None:
        data=crud.get_portal_page_by_multiple_lecture_name(db=db, lecture_name=lecture_name, skip=skip, limit=limit)
    else:
        data=crud.get_portal_page(db=db, skip=skip, limit=limit)
    
    result=[schemas.Portal.model_validate(row) for row in data]
    #print(result)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps([res.dict() for res in result], ensure_ascii = False)
    }
