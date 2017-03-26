build-image:
	docker build -t hello-ecs-frontend .

run-container:
	docker run -p 5000:5000 hello-ecs-frontend

push-image:
	test -n "$(ver)"
	$$(aws ecr get-login --region eu-west-1)
	docker tag hello-ecs-frontend:latest 174422895388.dkr.ecr.eu-west-1.amazonaws.com/hello-ecs-frontend:$(ver)
	docker push 174422895388.dkr.ecr.eu-west-1.amazonaws.com/hello-ecs-frontend:$(ver)

deploy:
	test -n "$(ver)"
	aws cloudformation update-stack --stack-name hello-ecs-frontend --template-body file://frontend-ecs-svc.json --parameters ParameterKey=Version,ParameterValue=$(ver)
