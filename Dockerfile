FROM python:3.10.6-buster
## FROM tensorflow/tensorflow:2.10.0 -- ensure python version stays the same

WORKDIR /prod

RUN pip install --upgrade pip
# ensure all requirements are listed (no tensorflow and keras, as this comes with the env)
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY breast_lesion_DL_pack breast_lesion_DL_pack
COPY setup.py setup.py
RUN pip install .

COPY Makefile Makefile

CMD uvicorn breast_lesion_DL_pack.api.fast:app --host 0.0.0.0 --port $PORT
