FROM tiangolo/uwsgi-nginx-flask:python3.8


RUN pip install mysql-connector-python
RUN pip install SQLAlchemy
RUN pip install wheel
RUN pip install pandas
# RUN pip -Iv install pandas==1.0.4
# RUN python3 -m pip install wheel
# RUN python3 -m pip install pandas
RUN pip install python-csv

COPY ./app /app
