import logging

from azure.functions import HttpRequest, HttpResponse
from ..shared.dateclass import get_current_date
from azure.storage.blob import BlobClient


def main(req: HttpRequest) -> HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    # Call the function
    try:
        current_date = get_current_date()
        logging.info("Current date: %s", current_date)
    except Exception as e:
        logging.error("Error while getting current date: %s", e)
        current_date = "unknown"
    
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return HttpResponse(f"Today is, {name}. This HTTP triggered function executed successfully.")
    else:
        return HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )
