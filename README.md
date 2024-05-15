# Speidel Braumeister Integration

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

![Project Maintenance][maintenance-shield]

_This integration allows you to monitor your Speidel Braumeister brewing system within Home Assistant._

**This integration will set up the following platforms.**

Platform | Description
-- | --
`binary_sensor` | Show something `True` or `False`.
`sensor` | Show info from Speidel API.
`switch` | Switch something `True` or `False`.

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `ha-speidel-braumeister-integration`.
1. Download _all_ the files from the `custom_components/ha-speidel-braumeister-integration/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Restart Home Assistant
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Speidel Braumeister"

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[ha-speidel-braumeister-integration]: https://github.com/omphteliba/ha-speidel-braumeister-integration
[commits-shield]: https://img.shields.io/github/commit-activity/y/ludeeus/ha-speidel-braumeister-integration.svg?style=for-the-badge
[commits]: https://github.com/omphteliba/ha-speidel-braumeister-integration/commits/main/
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/ludeeus/ha-speidel-braumeister-integration.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Joakim%20Sørensen%20%40ludeeus-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/ludeeus/ha-speidel-braumeister-integration.svg?style=for-the-badge
[releases]: https://github.com/omphteliba/ha-speidel-braumeister-integration/releases
