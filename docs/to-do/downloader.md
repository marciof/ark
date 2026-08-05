# Downloader

- Need to find other GUI alternatives?
- yt-dlp extensibility:
  - Plugins: https://github.com/yt-dlp/yt-dlp#plugins
  - `--exec` / post-processing: https://github.com/yt-dlp/yt-dlp#post-processing-options
- Embed subtitles in downloaded videos.
- Skip YouTube shorts (vertical videos) option.
- Skip video if mtime is more than 1 year in the past (eg. Last Week Tonight uploading old episodes) option.
- Make it possible to watch a video as it's being downloaded before it finishes?
- How to skip non-English videos? Eg. French/German Withings

## Instagram

- RSS feed from Instagram feed
  - https://www.instagram.com/therapyjeff/
  - eg. `a[href*="/reel/"][role=link]`
- via browser impersonation? might need to run JavaScript
  - https://github.com/CloakHQ/CloakBrowser + Playwright / Puppeteer
  - stealth browser as a localhost proxy?
  - https://en.wikipedia.org/wiki/Model_Context_Protocol
- via HTTP impersonation? might be more complex to parse w/o JavaScript
  - https://github.com/lexiforest/curl_cffi
  - https://github.com/lexiforest/curl-impersonate
  - https://github.com/jpjacobpadilla/Stealth-Requests
- via external tool/library/API?
  - https://github.com/instaloader/instaloader
  - https://imginn.com/therapyjeff/
  - https://www.picnob.com/profile/therapyjeff/
  - https://greasyfork.org/en/scripts/561325-bypass-instagram-login-redirects/code

## Youwee

- Sort download queue from recent to old.
- App is too sluggish/slow?
- Disable previews altogether in the YouTube section?
- Follow dark/light mode from OS? CLI option to change mode?
- Show timestamp when download was added/finished in the queue.
- Change number of parallel downloads, during downloading.
