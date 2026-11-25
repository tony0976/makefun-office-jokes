"""Writes one office joke to /output/entry.txt."""
import os

TEXT = "HR asked us to stop replying-all to the thread asking to be removed from the thread. Forty-seven people replied-all to agree."

# Rule: the joke must be a single line under 200 characters.
# The joke lands on the self-defeating reply-all: the request to stop
# replying-all is itself answered by 47 more reply-alls.
assert "\n" not in TEXT and len(TEXT) < 200, f"entry must be one line, under 200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
