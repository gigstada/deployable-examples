ifneq (,$(wildcard ./.env))
    include .env
    export
endif

install:
	pip install -r requirements.txt

dev:
	uvicorn server:app --reload

deploy:
	gcloud run deploy hello-fastapi --source . --project ${GCP_PROJECT_ID} --region ${GCP_REGION} --verbosity=debug \
	--update-env-vars SOME_ENV_VAR=${SOME_ENV_VAR},ANOTHER_VAR="some value" --allow-unauthenticated
