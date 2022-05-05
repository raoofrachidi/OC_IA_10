#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    LUIS_APP_ID = "ee000dd4-11d3-4cb4-bb30-7989b897c4d0"
    LUIS_API_KEY = "79b60d071a594d15b2a83e30ac9dc8c4"
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = "chatbotluisoc-authoring.cognitiveservices.azure.com/"
    APPINSIGHTS_INSTRUMENTATION_KEY = "c65bfa7b-7d6b-45f7-b246-d989f5a7a8e3"
