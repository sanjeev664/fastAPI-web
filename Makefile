IMAGE_TAG := "coreact_api"

build:
	DOCKER_BUILDKIT=1 docker build \
		--platform=linux/amd64 \
		-t ${IMAGE_TAG} \
		-f Dockerfile .

run:
	docker run \
		-e AWS_PROFILE=$${AWS_PROFILE:-testing} \
		--platform=linux/amd64 \
		-p 5000:5000 \
		--rm \
		${IMAGE_TAG}

interactive:
	docker run \
		--platform=linux/amd64 \
		-it \
		-e AWS_PROFILE=$${AWS_PROFILE:-testing} \
		-e PYTHONUNBUFFERED=1 \
		-p 5000:5000 \
		--rm \
		${IMAGE_TAG} \
		/bin/bash