# VLC

https://www.videolan.org

_(Last checked: v3.0.23)_

[TODO settings file instead of UI]:<>
[TODO embed video metadata in screenshots?]:<>
[TODO write down codec prefs that work on Lenovo Yoga Book]:<>

## Media Duration in Window Title

1. Open `Preferences`.
2. Switch to `Show settings` and `All`.
3. Open `Input / Codecs`.
4. Set `Change title according to current media` to: [^format-string]
   ```
   $Z ($D)
   ```

## Media Name in Screenshots

1. Open `Preferences`.
2. Switch to the `Video` tab.
3. Under `Video snapshots`, set `Prefix` to: [^format-string]
   ```
   $Z-
   ```

[^format-string]: [Format string documentation.](https://wiki.videolan.org/Documentation:Format_String/)
