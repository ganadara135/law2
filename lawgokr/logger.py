import logging


def message(message):
    logging.warning(message)
    with open('output.log', 'a') as file:

        file.write(message + '\n')
