import sys
from youtube_transcript_api import YouTubeTranscriptApi

vid = sys.argv[1] if len(sys.argv) > 1 else "Ey_xTunLIg0"
out = sys.argv[2] if len(sys.argv) > 2 else r"C:\Users\pberg\.cursor\projects\f-aion2\agent-tools\ey_transcript.txt"
api = YouTubeTranscriptApi()
t = api.fetch(vid, languages=["en", "de", "en-US"])
parts = []
for s in t.snippets:
    start = getattr(s, "start", 0)
    parts.append(f"[{start:.0f}s] {s.text}")
text = "\n".join(parts)
with open(out, "w", encoding="utf-8") as f:
    f.write(text)
print("lines", len(parts), "chars", len(text))
