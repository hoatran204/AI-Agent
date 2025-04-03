import os

class Config:
    MODEL_ID = os.getenv("MODEL_ID", "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF")
    MODEL_PATH = os.getenv("MODEL_PATH", ".models/tinyllama-1.1b-chat-v1.0.Q4_0.gguf")
    MAX_TOKENS = 256
    TEMPERATURE = 0.7
    TOP_P = 0.95
