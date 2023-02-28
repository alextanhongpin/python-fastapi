start:
	@uvicorn main:app --reload


freeze:
	@pip freeze > requirements.txt


install:
	@pip install -r requirements.txt


docs:
	@open http://localhost:8000/docs
	@open http://localhost:8000/redocs
