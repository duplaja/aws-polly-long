# aws-polly-long
Converts a long UTF-8 text doc to a single audio file, via Python script

## Requirements
- Latest Version AWS CLI installed, with credentials set
- AWS Credentials need Polly at a minimu, SNS if you want text alert when done
- Python
- Text to convert in a single file in UTF-8 format


## Usage
- Place text to convert and audiobook.py in the same folder
- Modify the inputfilename to match your text to convert, and if desired, change the pollyvoice and outputname.
- Run the script: nohup python audiobook.py &
- Let the script run (may take a while for larger texts, ~2 hours for 1.25 million characters

## Roadmap / Future Goals
- Handle appropriate MP3 tagging (will require another dependency)
- Clean up output / logging
- Option to split into logical chunks for larger documents (ch 1, etc)
- Long goal: Options for marking different voices for characters / speakers.


#### References
This project is based on this tutorial, with some bug-fixes and QoL improvements: https://aws.amazon.com/blogs/machine-learning/convert-your-text-into-an-mp3-file-with-amazon-polly-and-a-simple-python-script/
