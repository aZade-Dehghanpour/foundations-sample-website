def record_log(user_input, log_timestamp, inquiery):

    with open('data/log.txt', 'a+') as log_file:
        log_entry= "{} User entered {}.   {}\n".format(log_timestamp, user_input, inquiery)
        log_file.writelines(log_entry)