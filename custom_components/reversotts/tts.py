"""Support for the Reverso speech service."""

from __future__ import annotations

import logging
from typing import Any

from pyttsreverso import pyttsreverso
import voluptuous as vol

from homeassistant.components.tts import (
    CONF_LANG,
    PLATFORM_SCHEMA as TTS_PLATFORM_SCHEMA,
    Provider,
    TextToSpeechEntity,
    TtsAudioType,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.util import slugify

from .const import (
    CONF_BITRATE,
    CONF_PITCH,
    DEFAULT_BITRATE,
    DEFAULT_LANG,
    DEFAULT_PITCH,
    BITRATE_OPTIONS,
    SUPPORT_LANGUAGES,
    SUPPORT_OPTIONS,
    BITRATE_OPTIONS,
)

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = TTS_PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_LANG, default=DEFAULT_LANG): vol.In(SUPPORT_LANGUAGES),
        vol.Optional(CONF_PITCH, default=DEFAULT_PITCH): str,
        vol.Optional(CONF_BITRATE, default=DEFAULT_BITRATE): vol.In(BITRATE_OPTIONS),
    }
)


async def async_get_engine(
    hass: HomeAssistant,
    config: ConfigType,
    discovery_info: DiscoveryInfoType | None = None,
) -> ReversoProvider:
    """Set up Reverso speech component."""
    return ReversoProvider(
        hass,
        config[CONF_LANG],
        config[CONF_PITCH],
        config[CONF_BITRATE],
    )


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up Reverso speech platform via config entry."""
    default_language = config_entry.data[CONF_LANG]
    default_pitch = config_entry.data[CONF_PITCH]
    default_bitrate = config_entry.data[CONF_BITRATE]
    async_add_entities([ReversoTTSEntity(config_entry, default_language, default_pitch, default_bitrate)])


class ReversoTTSEntity(TextToSpeechEntity):
    """The Reverso speech API entity."""

    def __init__(self, config_entry: ConfigEntry, lang: str, pitch: int, bitrate: str) -> None:
        """Init Reverso TTS service."""
        self._lang = lang
        self._pitch = pitch
        self._bitrate = bitrate

        self._attr_name = f"Reverso TTS {SUPPORT_LANGUAGES[self._lang]}"
        self.entity_id = f"tts.{slugify(self._attr_name)}_{self._pitch}_{self._bitrate}"
        self._attr_unique_id = config_entry.entry_id

    @property
    def default_language(self) -> str:
        """Return the default language."""
        return self._lang

    @property
    def supported_languages(self) -> list[str]:
        """Return list of supported languages."""
        return SUPPORT_LANGUAGES

    @property
    def supported_options(self) -> list[str]:
        """Return a list of supported options."""
        return SUPPORT_OPTIONS

    def get_tts_audio(
        self, message: str, language: str, options: dict[str, Any] | None = None
    ) -> TtsAudioType:
        """Load TTS from Reverso."""
        if language is None:
            language = self._lang

        try:
            tts = pyttsreverso.ReversoTTS()
            mp3_data = tts.convert_text(
                voice=language, pitch=self._pitch, bitrate=self._bitrate, msg=message
            )
        except Exception as exc:
            _LOGGER.debug(
                "Error during processing of TTS request %s", exc, exc_info=True
            )
            raise HomeAssistantError(exc) from exc

        return "mp3", mp3_data


class ReversoProvider(Provider):
    """The Reverso speech API provider."""

    def __init__(self, hass: HomeAssistant, lang: str, pitch: int, bitrate: str) -> None:
        """Init Reverso TTS service."""
        self.hass = hass
        self._lang = lang
        self._pitch = pitch
        self._bitrate = bitrate
        self.name = "Reverso TTS"

    @property
    def default_language(self) -> str:
        """Return the default language."""
        return self._lang

    @property
    def supported_languages(self) -> list[str]:
        """Return list of supported languages."""
        return SUPPORT_LANGUAGES

    @property
    def supported_options(self) -> list[str]:
        """Return a list of supported options."""
        return SUPPORT_OPTIONS

    def get_tts_audio(
        self, message: str, language: str, options: dict[str, Any] | None = None
    ) -> TtsAudioType:
        """Load TTS from Reverso."""
        if language is None:
            language = self._lang

        try:
            tts = pyttsreverso.ReversoTTS()
            mp3_data = tts.convert_text(
                voice=language, pitch=self._pitch, bitrate=self._bitrate, msg=message
            )
        except Exception:
            _LOGGER.exception("Error during processing of TTS request")
            return None, None

        return "mp3", mp3_data