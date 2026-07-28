# Palm IIIxe

https://en.wikipedia.org/wiki/Palm_IIIxe

## Motivation

Backup infrared-based remote controls, without needing the original nor spares.

## Rationale

- Cheap to replace/buy.
- Built-in infrared transceiver.
- No dependency on third-party companies. [^logitech-stop-harmony]
- No dependency on internet/cloud-based services. [^logitech-discontinue-harmony]
- Data portability/ownership.
- Uses cheap, common, regular, AAA batteries for power.
- Can use rechargeable batteries.
- Long battery life.
- Touch-screen, not limited to fixed buttons/layout.
- Runs an OS, can install apps.

[^logitech-stop-harmony]: > _"[...] [Logitech will no longer manufacture Harmony remotes](https://support.myharmony.com/en-us/harmony-remote-manufacturing-update)."_ ([Internet Archive](https://web.archive.org/web/20260706064659/https://support.myharmony.com/en-us/harmony-remote-manufacturing-update))

[^logitech-discontinue-harmony]: > _"[...] [Logitech Harmony Remote Software no longer supports account creation or access to existing accounts for reprogramming, modifying, or making configuration changes to remotes](https://harmonyremote.com)."_ ([Internet Archive](https://web.archive.org/web/20251211222158/https://harmonyremote.com/))

## Setup

### Hardware

- Palm to serial cable: _Palm HotSync Cable, m100 Series (SKU P10701U)_
- Serial to USB-C adapter: [_Eaton (Tripp Lite) DB9 RS232 Adapter Cable (SKU USA-19HS-C)_](https://www.eaton.com/us/en-us/skuPage.USA-19HS-C.html)

### Windows

1. [Install drivers for the serial cable](https://www.eaton.com/us/en-us/skuPage.USA-19HS-C.html#tab-2) [^serial-drivers]\:
   - Windows 10 (32-bit): `eaton-tripp-lite-series-USA-19HS-driver-windows-7-8-server-2008-r2-v4.zip` [^serial-drivers-win10-32-cksum]
   - Windows 11: `eaton-tripp-lite-series-USA-19HS-driver-win11-win10.zip` [^serial-drivers-win11-cksum]
2. Connect serial cable, and verify it shows in `devmgmt.msc` under `Ports (COM & LPT)`.
3. [Install Palm Desktop 4.1.0](https://palmdb.net/app/palm-desktop) [^palm-desktop]\: `PalmDesktop41ENG.exe` [^palm-desktop-cksum]
   1. **Choose an install path that doesn't require admin rights**, so it can read its own database, and for `Note Pad` to work (it requires ActiveX).
   2. **Take note of the install path**, needed later for upgrading Palm OS.
4. Palm is now ready to be synced.

> [!Important]
> `HotSync` seems to have issues with power management (eg. computer standby and wakeup). If sync fails, then disconnect and re-connect the Palm to the serial cable.

> [!Note]
> [`Note Pad` (available starting in Palm OS 4)](https://palmdb.net/app/og-note-pad) support was dropped [_after_ Palm Desktop 4.1.0](https://web.archive.org/web/20081218230338/http://www.palm.com/us/support/downloads/add_downloads.html).

> [!Tip]
> Increase sync transfer speed in the Palm side:
> 1. Open `HotSync`, and under `Options`, go to `Connection Setup...`.
> 2. `Edit...` the `Cradle/Cable` connection.
> 3. In `Details...` choose the maximum `Speed` available.

[^serial-drivers]: Internet Archive: [Windows 10 / 11](https://archive.org/download/usa-19hs_win11_win10_driver/) or [Windows 98 / XP / 7 / 8](https://archive.org/download/eaton-tripp-lite-USA-19HS-drivers-windows-old-versions).

[^serial-drivers-win10-32-cksum]: Checksum SHA-256: `508dd51272bb1acc2826466ab9fefb0abade0c0a5754577cfa5ee9ae2ab33f94`

[^serial-drivers-win11-cksum]: Checksum SHA-256: `b66bb71957994fcdedc432a8625dce0ba22408bb16c62a485d69fea6fcd0bc05`

[^palm-desktop]: Internet Archive: [www.palm.com](https://web.archive.org/web/20081217094727/http://www.palm.com/us/support/downloads/win_desktop41.html) or [Palm Desktop Repository](https://archive.org/download/palm_desktop_repository/Windows/Palm_Desktop_4.1.0/).

[^palm-desktop-cksum]: Checksum SHA-256: `23a47e0d17760f9ecb3a9d2e5306c6fc39847a65a5df14d97d898fff81e39118`
