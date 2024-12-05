import configparser
class Config:
    @staticmethod
    def load_config(file_path='config.conf'):
        config = configparser.ConfigParser()
        config.read(file_path)
        exporter_port = config.getint('exporter','EXPORTER_PORT',fallback='9123')
        logstash_port = config.get('logstash','LOGSTASH_PORT',fallback='9665')
        logstash_host = config.get('logstash','LOGSTASH_HOST',fallback='localhost')


        return {
            'EXPORTER_PORT': exporter_port,
            'LOGSTASH_PORT':logstash_port,
            'LOGSTASH_HOST': logstash_host
        }

config = Config.load_config()

# env 
EXPORTER_PORT = config['EXPORTER_PORT']
LOGSTASH_PORT = config['LOGSTASH_PORT']
LOGSTASH_HOST = config['LOGSTASH_HOST']