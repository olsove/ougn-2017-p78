FROM hakobera/locust
RUN easy_install names
ADD ./test /test
ENV SCENARIO_FILE /test/locustfile.py
