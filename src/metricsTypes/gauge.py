from prometheus_client import Gauge

# Events metrics
events_input = Gauge('logstash_events_input_total', 'Total input events',['host'])
events_filtered = Gauge('logstash_events_filtered_total', 'Total filtered events',['host'])
events_output = Gauge('logstash_events_output_total', 'Total output events',['host'])
events_duration_ms = Gauge('logstash_events_duration_ms', 'Event processing duration',['host'])

# jvm 
# JVM Thread Metrics
jvm_threads_count = Gauge('logstash_jvm_threads_count', 'JVM Thread Count',['host'])
jvm_threads_peak_count = Gauge('logstash_jvm_threads_peak_count', 'JVM Peak Thread Count',['host'])

# JVM Pool Metrics
jvm_pool_young_used_bytes = Gauge('logstash_jvm_pool_young_used_bytes', 'JVM Young Generation Pool Used in Bytes',['host'])
jvm_pool_young_max_bytes = Gauge('logstash_jvm_pool_young_max_bytes', 'JVM Young Generation Pool Max in Bytes',['host'])
jvm_pool_young_peak_used_bytes = Gauge('logstash_jvm_pool_young_peak_used_bytes', 'JVM Young Generation Pool Peak Used in Bytes',['host'])
jvm_pool_young_peak_max_bytes = Gauge('logstash_jvm_pool_young_peak_max_bytes', 'JVM Young Generation Pool Peak Max in Bytes',['host'])
jvm_pool_old_used_bytes = Gauge('logstash_jvm_pool_old_used_bytes', 'JVM Old Generation Pool Used in Bytes',['host'])
jvm_pool_old_max_bytes = Gauge('logstash_jvm_pool_old_max_bytes', 'JVM Old Generation Pool Max in Bytes',['host'])
jvm_pool_old_peak_used_bytes = Gauge('logstash_jvm_pool_old_peak_used_bytes', 'JVM Old Generation Pool Peak Used in Bytes',['host'])
jvm_pool_old_peak_max_bytes = Gauge('logstash_jvm_pool_old_peak_max_bytes', 'JVM Old Generation Pool Peak Max in Bytes',['host'])
jvm_pool_survivor_used_bytes = Gauge('logstash_jvm_pool_survivor_used_bytes', 'JVM Survivor Pool Used in Bytes',['host'])
jvm_pool_survivor_max_bytes = Gauge('logstash_jvm_pool_survivor_max_bytes', 'JVM Survivor Pool Max in Bytes',['host'])
jvm_pool_survivor_peak_used_bytes = Gauge('logstash_jvm_pool_survivor_peak_used_bytes', 'JVM Survivor Pool Peak Used in Bytes',['host'])
jvm_pool_survivor_peak_max_bytes = Gauge('logstash_jvm_pool_survivor_peak_max_bytes', 'JVM Survivor Pool Peak Max in Bytes',['host'])

 # JVM GC Metrics
jvm_gc_young_collection_count = Gauge('logstash_jvm_gc_young_collection_count', 'Young Generation Garbage Collection Count',['host'])
jvm_gc_young_collection_time_millis = Gauge('logstash_jvm_gc_young_collection_time_millis', 'Young Generation Garbage Collection Time in Milliseconds',['host'])
jvm_gc_old_collection_count = Gauge('logstash_jvm_gc_old_collection_count', 'Old Generation Garbage Collection Count',['host'])
jvm_gc_old_collection_time_millis = Gauge('logstash_jvm_gc_old_collection_time_millis', 'Old Generation Garbage Collection Time in Milliseconds',['host'])


jvm_heap_used_bytes = Gauge('logstash_jvm_heap_used_in_bytes','Current JVM heap memory used by Logstash process in bytes',['host'])
jvm_heap_max_bytes = Gauge('logstash_jvm_heap_max_in_bytes','Maximum JVM heap memory available to Logstash process in bytes',['host'])
jvm_heap_used_percent = Gauge('logstash_jvm_heap_used_percent','Percentage of JVM heap memory currently in use by Logstash',['host'])

# JVM Uptime
jvm_uptime_millis = Gauge('logstash_jvm_uptime_millis', 'JVM Uptime in Milliseconds',['host'])

# Node status
node_status = Gauge('logstash_node_status', '1 for Healthy (GREEN), 0 for Unhealthy(RED), 2 for unknown, 3 for Functionality degraded (YELLOW)',['host'])
 
#  Pipelines (overall stats)
pipeline_workers = Gauge('logstash_pipeline_workers', 'Number of pipeline workers',['host'])
pipeline_batch_size = Gauge('logstash_pipeline_batch_size', 'Pipeline batch size',['host'])
pipeline_batch_delay = Gauge('logstash_pipeline_batch_delay', 'Pipeline batch delay in milliseconds',['host'])

# pipeline reloads (overall)
reload_successes = Gauge('logstash_reload_successes', 'Number of successful pipeline reloads',['host'])
reload_failures = Gauge('logstash_reload_failures', 'Number of failed pipeline reloads',['host'])

# event_count
queue_events_count = Gauge('logstash_queue_events_count', 'Number of events currently in the queue',['host'])

#  process
process_open_file_descriptors = Gauge('logstash_process_open_file_descriptors', 'Number of open file descriptors',['host'])
process_peak_open_file_descriptors = Gauge('logstash_process_peak_open_file_descriptors', 'Peak number of open file descriptors',['host'])
process_max_file_descriptors = Gauge('logstash_process_max_file_descriptors', 'Maximum number of file descriptors',['host'])
process_mem_total_virtual_bytes = Gauge('logstash_process_mem_total_virtual_bytes', 'Total virtual memory in bytes',['host'])
process_cpu_total_millis = Gauge('logstash_process_cpu_total_millis', 'Total CPU time in milliseconds',['host'])
process_cpu_percent = Gauge('logstash_process_cpu_percent', 'CPU usage percent',['host'])
process_cpu_load_average_1m = Gauge('logstash_process_cpu_load_average_1m', '1-minute CPU load average',['host'])
process_cpu_load_average_5m = Gauge('logstash_process_cpu_load_average_5m', '5-minute CPU load average',['host'])
process_cpu_load_average_15m = Gauge('logstash_process_cpu_load_average_15m', '15-minute CPU load average',['host'])

# each pipeline
pipeline_events_out = Gauge('logstash_pipeline_events_out', 'Number of events outputted by the pipeline', ['pipeline','host'])
pipeline_events_in = Gauge('logstash_pipeline_events_in', 'Number of events inputted to the pipeline', ['pipeline','host'])
pipeline_events_filtered = Gauge('logstash_pipeline_events_filtered', 'Number of events filtered by the pipeline', ['pipeline','host'])
pipeline_queue_push_duration = Gauge('logstash_pipeline_queue_push_duration_millis', 'Queue push duration in milliseconds', ['pipeline','host'])
pipeline_duration_millis = Gauge('logstash_pipeline_duration_millis', 'Pipeline processing duration in milliseconds', ['pipeline','host'])