# testing_api
Creating simple FAST API for testing exercise

**Dependencies**: uvicorn, fastapi, pytest, pydantic

**Steps**
1. Create file main.py with fast api configure
2. Run server with uvicorn `main:app --reload`
3. Create file test_api.py with two tests: test_can_get, test_post_3_times
4. Run tests with `python -m pytest -v -s`
