#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "20e4dbed-7bb4-4b56-afa5-29bfd17b2616")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "AtLeastSixteenCharacters_0")
    LUIS_APP_ID = os.environ.get("LuisAppId", "476ae015-dac4-44ce-9dcc-ca1da0154e3b")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "79b60d071a594d15b2a83e30ac9dc8c4")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "https://westeurope.api.cognitive.microsoft.com/luis/v2.0/apps/476ae015-dac4-44ce-9dcc-ca1da0154e3b?subscription-key=79b60d071a594d15b2a83e30ac9dc8c4&q=")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "e3919f29-1500-4f1b-a174-1f5fc46b8715"
    )