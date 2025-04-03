"""Config flow for Reverso text-to-speech integration."""

from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.components.tts import CONF_LANG
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult

from .const import (
    CONF_BITRATE,
    CONF_PITCH,
    DEFAULT_BITRATE,
    DEFAULT_LANG,
    DEFAULT_PITCH,
    DOMAIN,
    SUPPORT_LANGUAGES,
    BITRATE_OPTIONS,
)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Optional(CONF_LANG, default=DEFAULT_LANG): vol.In(SUPPORT_LANGUAGES),
        vol.Optional(CONF_PITCH, default=DEFAULT_PITCH): str,
        vol.Optional(CONF_BITRATE, default=DEFAULT_BITRATE): vol.In(BITRATE_OPTIONS),
    }
)


class ReversoConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Reverso text-to-speech."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        if user_input is not None:
            self._async_abort_entries_match(
                {
                    CONF_LANG: user_input[CONF_LANG],
                    CONF_PITCH: user_input[CONF_PITCH],
                    CONF_BITRATE: user_input[CONF_BITRATE],
                }
            )
            return self.async_create_entry(
                title="Reverso text-to-speech", data=user_input
            )

        return self.async_show_form(step_id="user", data_schema=STEP_USER_DATA_SCHEMA)

    async def async_step_onboarding(
        self, data: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle a flow initialized by onboarding."""
        return self.async_create_entry(
            title="Reverso text-to-speech",
            data={
                CONF_LANG: DEFAULT_LANG,
                CONF_PITCH: DEFAULT_PITCH,
                CONF_BITRATE: DEFAULT_BITRATE,
            },
        )