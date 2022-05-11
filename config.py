#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "39d10cb0-4b93-4730-be34-dd5fda4249fc")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    LUIS_APP_ID = os.environ.get("LuisAppId", "476ae015-dac4-44ce-9dcc-ca1da0154e3b")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "79b60d071a594d15b2a83e30ac9dc8c4")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "chatbotluisoc-authoring.cognitiveservices.azure.com")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "582710b5-a49e-4f08-af01-df54e3bc2ab2"
    )
