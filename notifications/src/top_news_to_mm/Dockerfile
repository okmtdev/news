FROM public.ecr.aws/lambda/python:3.9

WORKDIR /var/task

COPY /app.py ./
COPY ../../requirements-dev.lock ./

RUN pip install -r requirements-dev.lock

CMD ["app.lambda_handler"]
