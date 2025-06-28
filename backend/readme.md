python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app

test the sample - http://127.0.0.1:8000/api/greet?name=Surya

create .env file with the keys mentioned in .env.template file. Add yours