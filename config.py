#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId", "2b50b6ac-cef8-41f6-8cbf-c471d561e4a1")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "Kuk8Q~p6bn6oY3iXaCfy5mhdqb-6DfXAZnBXdcIT")
    LUIS_APP_ID = os.environ.get("LuisAppId", "e74cfb8e-ebf7-4c7a-9ffa-6204da13dc26")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "54bc33c0ca9149cdb8dac60dbdaa66c4")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "westeurope.api.cognitive.microsoft.com")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "29d4852e-8d5c-4161-a351-182bf5f3896a"
    )
