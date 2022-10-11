FROM python:3.7
# # Proxy settings
# ENV http_proxy http://...
# ENV https_proxy http://...

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