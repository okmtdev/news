FROM public.ecr.aws/lambda/python:3.11

WORKDIR /var/task

COPY /app.py ./
COPY ../../requirements.lock ./

RUN pip install -r requirements.lock

CMD ["app.lambda_handler"]
