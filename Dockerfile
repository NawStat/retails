FROM python:3.7

ENV http_proxy http://proxy.dsi.scom:8080
ENV https_proxy http://proxy.dsi.scom:8080

WORKDIR /var/web
RUN mkdir -p "/var/web"
VOLUME ["/var/web"]
ENTRYPOINT ["/var/web/manage.py"]
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update
RUN apt install  -y default-jre
COPY entrypoint.sh  /
ENTRYPOINT ["/entrypoint.sh"]
CMD ["runserver"]