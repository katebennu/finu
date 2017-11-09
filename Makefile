frontend/node_modules:
	cd frontend && yarn install

frontend/build: frontend/node_modules
	cd frontend && yarn build

prod: frontend/build
	docker-compose build
	docker-compose up

api-image:
	docker build -f Dockerfile.api -t api-image .

dev: frontend/node_modules api-image
	cd frontend && yarn start &
	docker run -p 5000:5000 -v $(CURDIR):/code --rm -it api-image

clean:
	rm -rf frontend/node_modules

.PHONY: dev prod api-image clean