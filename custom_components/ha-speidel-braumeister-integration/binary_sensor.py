"""Binary sensor platform for ha-speidel-braumeister-integration."""
from __future__ import annotations

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)

from .const import DOMAIN
from .coordinator import BraumeisterDataUpdateCoordinator
from .entity import SpeidelBraumeisterEntity

ENTITY_DESCRIPTIONS = (
    BinarySensorEntityDescription(
        key="ha-speidel-braumeister-integration",
        name="Speidel Braumeister Binary Sensor",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
    ),
)


async def async_setup_entry(hass, entry, async_add_devices):
    """Set up the binary_sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        SpeidelBraumeisterBinarySensor(
            coordinator=coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class SpeidelBraumeisterBinarySensor(SpeidelBraumeisterEntity, BinarySensorEntity):
    """ha-speidel-braumeister-integration binary_sensor class."""

    def __init__(
        self,
        coordinator: BraumeisterDataUpdateCoordinator,
        entity_description: BinarySensorEntityDescription,
    ) -> None:
        """Initialize the binary_sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def is_on(self) -> bool:
        """Return true if the binary_sensor is on."""
        return self.coordinator.data.get("title", "") == "foo"
