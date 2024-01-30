"""Constants for the Govee Bluetooth integration."""
from __future__ import annotations

from typing import Final, TypedDict

DOMAIN = "govee_ble"

EVENT_PROPERTIES: Final = "event_properties"
EVENT_TYPE: Final = "event_type"
GOVEE_BLE_EVENT: Final = "govee_ble_event"


class GoveeBleEvent(TypedDict):
    """Govee BLE event data."""

    device_id: str
    address: str
    event_class: str  # ie 'button'
    event_type: str  # ie 'press'
    event_properties: dict[str, str | int | float | None] | None
