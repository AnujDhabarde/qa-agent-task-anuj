from youtube_transcript_api import YouTubeTranscriptApi


video_id = "IK62Rk47aas"

transcript = YouTubeTranscriptApi.get_transcript(video_id)

with open("transcript.txt", "w") as f:
    for entry in transcript:
        f.write(entry['text'] + "\n")
print("✅ Transcript saved as transcript.txt")
