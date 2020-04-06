docker-user=jaredhanson11
name=${docker-user}/vamble-api

build:
	docker build . --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t ${name}:latest
push: build
	docker push ${name}:latest
