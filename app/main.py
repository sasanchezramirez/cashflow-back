import app.application.fast_api as fast_api
import logging
from app.infrastructure.entry_point.utils.exception_handler import custom_exception_handler
from app.domain.model.util.custom_exceptions import CustomException
from fastapi.middleware.cors import CORSMiddleware


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(console_handler)

app = fast_api.create_app()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)


app.add_exception_handler(CustomException, custom_exception_handler)
