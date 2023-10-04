# Use an official Elasticsearch Docker image as the base image
FROM docker.elastic.co/elasticsearch/elasticsearch:7.15.0

# Copy the custom elasticsearch.yml configuration file into the container
COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml

# Expose the necessary ports
EXPOSE 9200 9300

# Run Elasticsearch as the default command
CMD ["elasticsearch"]
