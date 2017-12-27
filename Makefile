default: install test

install:
	pip install -r requirements.txt
	pip install . --upgrade

deploy:
	pip install pipreqs
	pipreqs . --force

test:
	docker build . -f Dockerfile.test -t pipeline-test
	docker run -p 5000:5000 --rm -it pipeline-test

start:
	docker build . -t pipeline
	docker run -p 5000:5000 --rm -it pipeline