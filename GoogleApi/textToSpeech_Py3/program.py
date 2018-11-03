# https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries
#
#

from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()



# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    speaking_rate=0.75,
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

source_file = open('source.txt', encoding='utf-8', mode='r')
result_file = open('result.txt', encoding='utf-8', mode='w')
for line in source_file :
    line = line.strip()
    splitLine = line.split("\t")
# Set the text input to be synthesized	
    synthesis_input = texttospeech.types.SynthesisInput(text=splitLine[1])
# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    with open("TH-Tamean"+splitLine[0].strip()+".mp3", 'wb') as out:
# Write the response to the output file.
        out.write(response.audio_content)
        print(splitLine[0].strip())	
	
	

	
	


# The response's audio_content is binary.
