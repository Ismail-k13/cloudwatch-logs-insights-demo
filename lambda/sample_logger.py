import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("INFO level: Lambda executed successfully.")
    logger.warning("WARNING level: This is a sample warning.")
    logger.error("ERROR level: This is a sample error.")
    return {
        'statusCode': 200,
        'body': 'Log event generated.'
    }
