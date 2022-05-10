from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials
from config import DefaultConfig

CONFIG = DefaultConfig()


def test_luis_intent():
    """Check LUIS non-regression on *Top intent*
    """
    # Instantiate prediction client
    clientRuntime = LUISRuntimeClient(
        CONFIG.LUIS_API_HOST_NAME,
        CognitiveServicesCredentials(CONFIG.LUIS_API_KEY))

    # Create request
    request = 'looking to go from san francisco to marseille. book me for september 18 to 22. let me know if its more ' \
              'than 2800 because thats all i can afford '

    # Get response
    response = clientRuntime.prediction.resolve(CONFIG.LUIS_APP_ID, query=request)

    check_top_intent = 'BookFlightIntent'
    is_top_intent = response.top_scoring_intent.intent
    assert check_top_intent == is_top_intent


def test_luis_origin():
    """Check LUIS non-regression on *Origin*
    """
    # Instantiate prediction client
    clientRuntime = LUISRuntimeClient(
        CONFIG.LUIS_API_HOST_NAME,
        CognitiveServicesCredentials(CONFIG.LUIS_API_KEY))

    # Create request
    request = 'looking to go from san francisco to marseille. book me for september 18 to 22. let me know if its more ' \
              'than 2800 because thats all i can afford '

    # Get response
    response = clientRuntime.prediction.resolve(CONFIG.LUIS_APP_ID, query=request)

    check_origin = 'san francisco'
    all_entities = response.entities
    is_origin = None

    for i in range(0, len(all_entities)):
        if all_entities[i].type == 'or_city':
            is_origin = all_entities[i].entity

    assert check_origin == is_origin


def test_luis_destination():
    """Check LUIS non-regression on *Destination*
    """
    # Instantiate prediction client
    clientRuntime = LUISRuntimeClient(
        CONFIG.LUIS_API_HOST_NAME,
        CognitiveServicesCredentials(CONFIG.LUIS_API_KEY))

    # Create request
    request = 'looking to go from san francisco to marseille. book me for september 18 to 22. let me know if its more ' \
              'than 2800 because thats all i can afford '

    # Get response
    response = clientRuntime.prediction.resolve(CONFIG.LUIS_APP_ID, query=request)

    check_destination = 'marseille'
    all_entities = response.entities
    is_destination = None

    for i in range(0, len(all_entities)):
        if all_entities[i].type == 'dst_city':
            is_destination = all_entities[i].entity

    assert check_destination == is_destination
