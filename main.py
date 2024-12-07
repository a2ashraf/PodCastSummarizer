import json
from listennotes import podcast_api
from openai import OpenAI


# Function to search for a podcast and extract the podcast ID
def search_for_podcast(query):
    api_key = '6fc563c73aca4522814bf704763a774f'
    client = podcast_api.Client(api_key=api_key)
    response = client.search(
        q=query, sort_by_date=1,
        only_in='title,description'
    )
    podcast_id = response.json()['results'][0]['id']
    return podcast_id


# Function to fetch the transcript using the podcast ID
def get_podcast_transcript(podcast_id):
    api_key = '6fc563c73aca4522814bf704763a774f'
    client = podcast_api.Client(api_key=api_key)
    response = client.fetch_episode_by_id(
        id=podcast_id,
        show_transcript=1
    )
    transcript = response.json().get('transcript')
    return transcript


# Function to summarize the transcript using OpenAI's API
def summarize_transcript(transcript):
    client = OpenAI(api_key='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')

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to summarize podcast transcripts."},
            {"role": "user", "content": f"Summarize the following podcast transcript:\n\n{transcript}"}
        ]
    )
    summary = response.choices[0].message.content.strip()
    return summary


# Main function to orchestrate the above steps
def main():
    query = 'dr-zachary-knight-the-science-of-hunger-medications-to-combat-obesity'
    podcast_id = search_for_podcast(query)
    transcript = get_podcast_transcript(podcast_id)

    if transcript:
        summary = summarize_transcript(transcript)
        print("Summary of the podcast transcript:")
        print(summary)
    else:
        print("Transcript not available for this podcast.")


# Run the main function
if __name__ == '__main__':
    main()