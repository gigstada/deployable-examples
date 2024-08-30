# This block loads in the environment variables from the .env file.
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

install:
	pip install -r requirements.txt

dev:
	uvicorn server:app --reload --host=0.0.0.0 --port=8999

gh:
	open https://github.com/gigstada/deployable-examples


gcloud-setup:
	gcloud config configurations activate "${GCP_PROJECT_ID}" 

deploy:
# This is the command to deploy to Cloud Run. 
# You will need to explicitly set the environment variables that you want available in your application.
	gcloud run deploy ${GCP_SERVER_NAME} --source . --project ${GCP_PROJECT_ID} --region ${GCP_REGION} --verbosity=debug \
	--update-env-vars SOME_ENV_VAR="${SOME_ENV_VAR}",ANOTHER_VAR="some value" --allow-unauthenticated


url:
	open "https://gt-api-experiments-174772979833.us-central1.run.app/"