# aws-polly-long
Converts a long UTF-8 text doc to a single audio file, via Python script

## Requirements
- Latest Version AWS CLI installed, with credentials set (Make sure you update!)
- AWS Credentials need Polly at a minimum, SNS if you want text alert when done
- Python3 (won't work with 2 anymore)
- Designed to work in a bash shell or similar (cat, etc)
- ~~mid3v2, from python-mutagen, for tagging (sudo apt-get install python-mutagen )~~ Removed
- Text to convert in a single file in UTF-8 format

## Note
- This version has Neural TTS enabled by default, for better sound quality. See the in-file comment for information on downgrading it if you wish.

## Usage
- Place text to convert and audiobook.py in the same folder
- Modify the inputfilename to match your text to convert, and if desired, change the pollyvoice and outputname.
- Run the script: nohup python3 audiobook.py &
- Let the script run (may take a while for larger texts, ~2 hours for 1.25 million characters)

## Roadmap / Future Goals
- Clean up output / logging
- Option to split into logical chunks for larger documents (ch 1, etc)
- Long goal: Options for marking different voices for characters / speakers.


#### References
This project is based on this tutorial, with some bug-fixes and QoL improvements: https://aws.amazon.com/blogs/machine-learning/convert-your-text-into-an-mp3-file-with-amazon-polly-and-a-simple-python-script/
