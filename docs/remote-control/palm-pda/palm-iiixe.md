# Palm IIIxe

https://en.wikipedia.org/wiki/Palm_IIIxe

## Motivation

Backup infrared-based remote controls, without needing the original nor spares.

## Rationale

- Cheap to replace/buy.
- Built-in infrared transceiver.
- No dependency on third-party companies.
- No dependency on internet/cloud-based services.
- Data portability/ownership.
- Uses cheap, common, regular, AAA batteries for power.
- Can use rechargeable batteries.
- Long battery life.
- Touch-screen, not limited to fixed buttons/layout.
- Runs an OS, can install apps.

## Setup

### Hardware

- Palm to serial cable: _Palm HotSync Cable, m100 Series (SKU P10701U)_
- Serial to USB-C adapter: [_Eaton (Tripp Lite) DB9 RS232 Adapter Cable (SKU USA-19HS-C)_](https://www.eaton.com/us/en-us/skuPage.USA-19HS-C.html)

### Windows 11

1. [Install drivers](https://www.eaton.com/us/en-us/skuPage.USA-19HS-C.html#tab-2) [^serial-drivers]\: `eaton-tripp-lite-series-USA-19HS-driver-win11-win10.zip` [^serial-drivers-cksum]
2. [Install Palm Desktop 6.2.2](https://palmdb.net/app/palm-desktop) [^palm-desktop]\: `PalmDesktopWin62.exe` [^palm-desktop-cksum]

> [!Important]
> [`Note Pad` (available starting in Palm OS 4)](https://palmdb.net/app/og-note-pad) support was dropped [_after_ Palm Desktop 4.1.0](https://web.archive.org/web/20081218230338/http://www.palm.com/us/support/downloads/add_downloads.html).

[^serial-drivers]: [Internet Archive.](https://archive.org/download/usa-19hs_win11_win10_driver/)

[^serial-drivers-cksum]: Checksum SHA-256: `b66bb71957994fcdedc432a8625dce0ba22408bb16c62a485d69fea6fcd0bc05`

[^palm-desktop]: Internet Archive: [www.palm.com](https://web.archive.org/web/20081217015844/http://www.palm.com/us/support/downloads/windesk62.html) or [Palm Desktop Repository](https://archive.org/download/palm_desktop_repository/Windows/Palm_Desktop_6.2.2/).

[^palm-desktop-cksum]: Checksum SHA-256: `63dd2b320d205aa05b005163436ceb8368e2de9140a3679e6baafe3f7886382d`
