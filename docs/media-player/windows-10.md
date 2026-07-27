# Windows 10

## [Disable Activity History](https://learn.microsoft.com/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1822-activity-history) [^activity-hist]

As admin, in `cmd`:

```batch
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v "EnableActivityFeed" /t REG_DWORD /d 0 /f
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v "PublishUserActivities" /t REG_DWORD /d 0 /f
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v "UploadUserActivities" /t REG_DWORD /d 0 /f
```

[^activity-hist]: > _"[...] turn Off tracking of your Activity History."_

## [Disable Non-Essential Hardware Apps](https://learn.microsoft.com/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#4-device-metadata-retrieval) [^device-meta]

As admin, in `cmd`:

```batch
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Device Metadata" /v PreventDeviceMetadataFromNetwork /t REG_DWORD /d 1 /f
```

[^device-meta]: > _"[...] prevent Windows from retrieving device metadata from the Internet"_
