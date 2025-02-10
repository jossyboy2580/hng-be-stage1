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

@app.get('/api/classify-number')
async def hello(number):
    try:
        number = int(number)
    except:
        return JSONResponse(status_code=400,
                           content={'number':'alphabet',
                                    'error': True
                            }
        )
    content = requests.get(f'http://numbersapi.com/{number}/math?json')
    result = {'number': number,
              'is_prime': is_prime(number),
              'is_perfect': is_perfect(number),
              'properties':properties(number),
              'digit_sum': digit_sum(number),
              'fun_fact': content.json()['text']
    }
    
    return result
