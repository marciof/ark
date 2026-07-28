# Feed Reader

- Need to find alternatives to Liferea? It removed the external downloader tool option (on v1.15.9), and may remove more, make things more complicated, or go unmaintained? Preferably with support for plugins and OPML.
  - https://freenet.org/apps/
  - [RSS Guard](https://github.com/martinrotter/rssguard/issues/1952#issuecomment-4609281030)
  - [Akregator](https://github.com/KDE/akregator/)
  - [Alligator](https://github.com/kde/alligator)
  - [Thunderbird](https://reviewers.addons.thunderbird.net/en-us/thunderbird/tag/rss) (see also [custom CSS](https://reddit.com/r/Thunderbird/comments/1fhyvvq/kind_of_loving_thunderbird_as_an_rss_reader_right/lo3dpgu/))
  - local proxy (as done previously) as a hook for detecting enclosures, and optionally downloading and passing on as a stream to the upstream app, https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-stream-directly-to-media-player
- Helper script for getting an RSS feed URL from a YouTube channel/playlist?
  - https://codemadness.org/sfeed.html
  - check what/how Liferea does it

## Liferea

- Look into sandboxing an old fixed version that still has support for custom external download tools? https://github.com/89luca89/distrobox
- Not always updating some feeds even when it has new content  (eg. TVW The Impact).
- Calls the conversion filter with an empty stdin, when it decides incorrectly that a feed (eg. TVW The Impact) has no new content.
- Feed fetch spacing option like RSS Guard, https://github.com/lwindolf/liferea/issues/1555
- OPML automatic backup (via plugins?).
