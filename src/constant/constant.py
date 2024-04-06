import os
from dotenv import load_dotenv

load_dotenv()

VIDEO_PROCESS_TABLE = f'velo-sync-video-process-table-{os.getenv("STAGE")}'

S3_STORAGE_BUCKET = f'velo-sync-storage-bucket-{os.getenv("STAGE")}'

METRIC_TYPE = {
    "POWER": 0,
    "HEART_RATE": 1,
    "CADENCE": 2,
    "SPEED": 3,
    "DISTANCE": 4,
    "GRADIENT": 5,
    "ELEVATION": 6,
    "MAP": 7
}

SUFFIX_MP4 = '.mp4'