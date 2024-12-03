# Usar la imagen oficial de Elasticsearch
FROM docker.elastic.co/elasticsearch/elasticsearch:8.16.1

# Copia tu archivo de configuración desde el directorio local al interior del contenedor
COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml

# Exponer el puerto por defecto de Elasticsearch
EXPOSE 9200

# Ejecutar Elasticsearch
CMD ["elasticsearch"]