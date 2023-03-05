import pydub


def main():
    # Set the input and output file paths
    input_file = "../../../someConversionTextToSpeegOGG.ogg"
    output_file = "../../../someConversionTextToSpeegOGG.mp3"

    # Load the input file using pydub
    audio = pydub.AudioSegment.from_file(input_file, format="ogg")

    # Export the audio to MP3 format using pydub
    audio.export(output_file, format="mp3")


if __name__ == '__main__':
    main()
