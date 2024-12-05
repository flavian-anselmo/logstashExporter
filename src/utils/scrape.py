import logging
from src.scrapers.node_stats  import NodeStats

logger = logging.getLogger(__name__)

class ScrapeMetrics:
    @staticmethod
    async def collect_metrics(logstash_url:str, LOGSTASH_PORT:str):
        try:
            NodeStats.node_stats(logstash_url=logstash_url, LOGSTASH_PORT=LOGSTASH_PORT)
        except Exception as err:
            logger.error(f'ScrapeMetricsError: {err}')


              
              
      