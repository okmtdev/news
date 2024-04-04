FROM public.ecr.aws/lambda/python:3.9

WORKDIR /var/task

COPY /top_news_to_mm.py ./
COPY ../../../requirements-dev.lock ./

RUN pip install -r requirements-dev.lock

CMD ["top_news_to_mm.lambda_handler"]
