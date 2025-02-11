from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
from utils import is_prime, is_perfect, properties, digit_sum


app = FastAPI()

origins = ['*']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_methods=['*'],
                   allow_headers=['*'])

@app.get('/')
async def home():
    return JSONResponse(status_code=404,
                        content={'error': True,
                                 'message': 'go to /api/classify-number?number=<number>'
                        }
                        )

@app.get('/api/classify-number')
async def hello(number):
    try:
        type_casted_number = int(number)
    except:
        return JSONResponse(status_code=400,
                           content={'number':'alphabet',
                                    'error': True
                            }
        )
    if number != str(type_casted_number):
        return JSONResponse(status_code=400,
                            content={'error': True}
                            )
    number = type_casted_number
    content = requests.get(f'http://numbersapi.com/{number}/math?json')
    result = {'number': number,
              'is_prime': is_prime(number),
              'is_perfect': is_perfect(number),
              'properties':properties(number),
              'digit_sum': digit_sum(number),
              'fun_fact': content.json()['text']
    }
    
    return result
