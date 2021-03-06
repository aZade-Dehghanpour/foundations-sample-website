import logging

logger = logging.getLogger(__name__)

def record_log(user_input, inquiery):
    
    log_entry= "User entered {} ... {}\n".format(user_input, inquiery)
    logging.debug(log_entry)