# FastAPI in GCP

This is a simple example of a FastAPI application structured to be easily deployable on Google Cloud Run. It's meant to be a starting point for building your own application.

## Environment Variables
Environment variables are managed through `.env` files, with an example provided in `.env.example`. You can get started by renaming `.env.example` to `.env` and updating the values as needed.

Note that for environment variables you want to be available in your deployed container, you must update the deploy command in `Makefile` to include them in the `--set-env-vars` flag. This allows you to only include the variables you need in your deployed container.

## Local Development
You can start developing in your own copy of this directory with a few simple steps:
1. Rename `.env.example` to `.env` and update the values as needed.
1. Run `make install`
1. Run `make dev`

## Deployment
Before you try to deploy, ensure you have installed and set up the [gcloud CLI](https://cloud.google.com/sdk/gcloud). You also need to have a project set up on Google Cloud Platform.

After you've done that, make sure your .env file is updated with your `GCP_PROJECT_ID` and then run `make deploy`. This will build a Docker image and deploy it to Google Cloud Run.

