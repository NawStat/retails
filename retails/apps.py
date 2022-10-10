import os
from django.apps import AppConfig
from django.conf import settings
from .spark_utils import spark_computations

spark_dataframe = None

class RetailsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'retails'

    def ready(self):
        #for the Java gateway process
        os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-1.11.0-openjdk-amd64"
        # To avoid reloading spark session  many times, we declare the var in apps.py to use it later in views
        global spark_dataframe
        spark_dataframe = spark_computations(settings.DATABASE_NAME, settings.COLLECTION, settings.IP, settings.PORT)


