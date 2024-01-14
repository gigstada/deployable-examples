# This block loads in the environment variables from the .env file.
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

install:
	pip install -r requirements.txt

dev:
	uvicorn server:app --reload

deploy:
# This is the command to deploy to Cloud Run. 
# You will need to explicitly set the environment variables that you want available in your application.
	gcloud run deploy ${GCP_SERVER_NAME} --source . --project ${GCP_PROJECT_ID} --region ${GCP_REGION} --verbosity=debug \
	--update-env-vars SOME_ENV_VAR="${SOME_ENV_VAR}",ANOTHER_VAR="some value" --allow-unauthenticated
