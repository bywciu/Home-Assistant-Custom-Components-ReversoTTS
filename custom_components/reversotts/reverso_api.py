"""Reverso TTS API with Cloudflare bypass."""

from __future__ import annotations

import base64
import logging
from typing import Any

import cloudscraper

_LOGGER = logging.getLogger(__name__)

# Reverso Voice API endpoint
REVERSO_API_URL = "https://voice.reverso.net/RestPronunciation.svc/v1/output=json/GetVoiceStream/voiceName={voice}?voiceSpeed={speed}&mp3BitRate={bitrate}&inputText={text}"


class ReversoTTS:
    """Reverso TTS API client with Cloudflare bypass."""

    def __init__(self) -> None:
        """Initialize the Reverso TTS client."""
        self._scraper = cloudscraper.create_scraper(
            browser={
                "browser": "chrome",
                "platform": "windows",
                "desktop": True,
            },
            delay=10,
        )

    def _text_to_base64(self, message: str) -> str:
        """Encode text message to base64."""
        message_bytes = message.encode('utf-8')
        base64_bytes = base64.b64encode(message_bytes)
        return base64_bytes.decode('utf-8')

    def convert_text(
        self,
        voice: str,
        pitch: int | str = 100,
        bitrate: int | str = 128,
        msg: str = "",
    ) -> bytes | None:
        """Convert text to speech using Reverso API.

        Args:
            voice: Voice name (e.g., "Sharon-US-English")
            pitch: Voice speed/pitch (default 100)
            bitrate: MP3 bitrate (default 128)
            msg: Text message to convert

        Returns:
            MP3 audio data as bytes or None if failed
        """
        if not msg:
            _LOGGER.warning("Empty message provided")
            return None

        # Base64 encode the message
        encoded_text = self._text_to_base64(msg)
        
        # Build the API URL
        url = REVERSO_API_URL.format(
            voice=voice,
            speed=pitch,
            bitrate=bitrate,
            text=encoded_text,
        )

        _LOGGER.debug("Requesting TTS from Reverso: %s", url)

        try:
            response = self._scraper.get(url, timeout=30)
            response.raise_for_status()
            
            content_type = response.headers.get('Content-Type', '')
            _LOGGER.debug("Response status: %s, Content-Type: %s", response.status_code, content_type)
            
            # API can return either raw MP3 or JSON with base64-encoded audio
            if 'audio/' in content_type:
                # Direct MP3 response
                return response.content
            elif 'json' in content_type:
                # JSON response with base64-encoded audio
                data = response.json()
                if "AudioEncoded" in data:
                    return base64.b64decode(data["AudioEncoded"])
                else:
                    _LOGGER.error("Unexpected API response: %s", data)
                    return None
            else:
                _LOGGER.error("Unexpected content type: %s", content_type)
                return None

        except cloudscraper.exceptions.CloudflareChallengeError as exc:
            _LOGGER.error("Cloudflare challenge failed: %s", exc)
            raise
        except Exception as exc:
            _LOGGER.error("Error fetching TTS audio: %s", exc)
            raise


class AsyncReversoTTS:
    """Async wrapper for Reverso TTS API."""

    def __init__(self) -> None:
        """Initialize the async Reverso TTS client."""
        self._sync_client = ReversoTTS()

    async def convert_text_async(
        self,
        hass: Any,
        voice: str,
        pitch: int | str = 100,
        bitrate: int | str = 128,
        msg: str = "",
    ) -> bytes | None:
        """Convert text to speech asynchronously.

        Uses executor to run blocking cloudscraper in a thread pool.
        """
        return await hass.async_add_executor_job(
            self._sync_client.convert_text,
            voice,
            pitch,
            bitrate,
            msg,
        )
