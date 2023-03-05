from pydub import AudioSegment
import base64


def convertBase64EncodedApiMusicIntoPlayableFile(original_filetype, dest_file_location):

    # Open the file in read mode
    with open('C:\Users\\mason\\Documents\\mp3_test_goofle_to_convert.txt', 'r') as fileAudio:

        # Read the contents of the file
        file_contents = fileAudio.read()

        # Decode the audio data from base64
        decoded_audio_data = base64.b64decode(file_contents)
        audio_file_formatted = ''
        # Load the audio data as an MP3 audio segment using
        if str(original_filetype).lower() is 'mp3':
            audio_file_formatted = AudioSegment.from_mp3(decoded_audio_data)
            dest_file_location += '\\decoded_' + original_filetype + "_audio.mp3"
        if str(original_filetype).lower() is 'ogg':
            audio_file_formatted = AudioSegment.from_ogg(decoded_audio_data)
            dest_file_location += '\\decoded_' + original_filetype + "_audio.ogg"
        else:
            return 'ERROR'

        audio_file_formatted.export(dest_file_location, format=str(original_filetype).lower())


if __name__ == '__main__':
    convertBase64EncodedApiMusicIntoPlayableFile('mp3', 'C:\Users\mason\Documents')
