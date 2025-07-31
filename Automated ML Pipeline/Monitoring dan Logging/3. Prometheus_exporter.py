import time
import random
import threading
import psutil
from prometheus_client import start_http_server, Counter, Gauge, Histogram, Summary

# Definisi metrik
REQUEST_COUNT = Counter('api_request_count', 'Total API requests')
PREDICTION_LATENCY = Histogram('prediction_latency_seconds', 'Prediction latency in seconds')
PREDICTION_CONFIDENCE = Histogram('prediction_confidence', 'Confidence of model predictions')
SUCCESSFUL_PREDICTIONS = Counter('successful_predictions_total', 'Total number of successful predictions')
API_ERRORS = Counter('api_errors_total', 'Number of API errors')
BATCH_SIZE = Gauge('batch_size', 'Current batch size for predictions')
QUEUE_SIZE = Gauge('prediction_queue_size', 'Size of the prediction queue')
THROUGHPUT = Summary('prediction_throughput', 'Predictions per second')

SYSTEM_MEMORY = Gauge('system_memory_usage_percent', 'Memory usage percentage')
SYSTEM_CPU = Gauge('system_cpu_usage_percent', 'CPU usage percentage')
DISK_USAGE = Gauge('disk_usage_percent', 'Disk usage percentage of root')

# Fungsi untuk simulasi prediksi
def simulate_predictions():
    while True:
        start_time = time.time()
        
        REQUEST_COUNT.inc()
        batch_size = random.randint(1, 10)
        BATCH_SIZE.set(batch_size)
        QUEUE_SIZE.set(random.randint(0, 100))
        
        latency = random.uniform(0.01, 0.3)
        PREDICTION_LATENCY.observe(latency)
        
        confidence = random.uniform(0.5, 1.0)
        PREDICTION_CONFIDENCE.observe(confidence)
        
        if random.random() < 0.95:
            SUCCESSFUL_PREDICTIONS.inc()
        else:
            API_ERRORS.inc()
        
        THROUGHPUT.observe(1.0 / latency)
        
        elapsed = time.time() - start_time
        time.sleep(max(0.1 - elapsed, 0))

# Fungsi untuk mengumpulkan metrik sistem
def collect_system_metrics():
    while True:
        SYSTEM_MEMORY.set(psutil.virtual_memory().percent)
        SYSTEM_CPU.set(psutil.cpu_percent(interval=1))
        DISK_USAGE.set(psutil.disk_usage('/').percent)
        time.sleep(5)

if __name__ == '__main__':
    start_http_server(8000)
    print("Prometheus exporter started on port 8000")
    
    threading.Thread(target=collect_system_metrics, daemon=True).start()
    threading.Thread(target=simulate_predictions, daemon=True).start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exporter stopped")