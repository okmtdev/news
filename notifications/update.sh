#!/bin/bash

grep -vE '(^#.*|-e file:.*)' requirements.lock > src/top_news_to_mm/requirements.txt