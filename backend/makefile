build-image:
	docker build -t hello-ecs-backend .

run-container:
	docker run -p 5000:5000 hello-ecs-backend

push-image:
	test -n "$(ver)"
	$$(aws ecr get-login --region eu-west-1)
	docker tag hello-ecs-backend:latest 174422895388.dkr.ecr.eu-west-1.amazonaws.com/hello-ecs-backend:$(ver)
	docker push 174422895388.dkr.ecr.eu-west-1.amazonaws.com/hello-ecs-backend:$(ver)

deploy:
	test -n "$(ver)"
	aws cloudformation update-stack --stack-name hello-ecs-backend --template-body file://backend-ecs-svc.json --parameters ParameterKey=Version,ParameterValue=$(ver)
