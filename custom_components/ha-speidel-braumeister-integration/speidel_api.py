import asyncio
import logging
from typing import Any, Dict

import aiohttp

from homeassistant.helpers.update_coordinator import UpdateFailed

_LOGGER = logging.getLogger(__name__)

class SpeidelBraumeisterApiClient:
    """Client for the MySpeidel API."""

    def __init__(
        self,
        username: str,
        password: str,
        session: aiohttp.ClientSession,
    ) -> None:
        """Initialize the API client."""
        self.username = username
        self.password = password
        self.session = session

    async def async_get_data(self) -> Dict[str, Any]:
        """Fetch data from the MySpeidel API."""
        try:
            # Get the access token
            auth_response = await self._get_access_token()

            headers = {
                "Authorization": f"Bearer {auth_response['accessToken']}",
            }

            url = "https://api.cloud.myspeidel.com/v1.0/brew/current"
            response = await self.session.get(url, headers=headers)

            if response.status == 200:
                return await response.json()
            else:
                raise UpdateFailed(f"API Error: {response.status} - {response.text}")

        except Exception as exception:
            raise UpdateFailed(f"Error updating from MySpeidel API: {exception}") from exception

    async def _get_access_token(self) -> Dict[str, Any]:
        """Get an access token from the MySpeidel API."""
        try:
            auth_data = {
                "username": self.username,
                "password": self.password,
            }

            auth_url = "https://api.cloud.myspeidel.com/v1.0/auth/authentication"
            async with self.session.post(auth_url, json=auth_data) as response:
                if response.status != 200:
                    raise SpeidelBraumeisterApiClientAuthenticationError(
                        "Authentication failed"
                    )
                return await response.json()

        except Exception as exception:
            raise SpeidelBraumeisterApiClientCommunicationError(
                "Error communicating with MySpeidel API"
            ) from exception
