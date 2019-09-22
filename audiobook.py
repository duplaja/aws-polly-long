#!/usr/bin/python3
# coding: utf-8
import subprocess
import codecs

#Enter / change below as needed
inputfilename = "input-text-file.txt" # Single blank line between paragraphs

outputname = "your-output-file-name.mp3" #no spaces, will work on getting this straightened out

pollyvoice = "Brian" #If you keep neural engine, make sure you pick a voice that supports it

#Use country code first, no spaces or symbols. Ex) 12223334444. Leave as none if you don't want a text alert
phone = "none"

#Begins the process
f = codecs.open(inputfilename, encoding='utf-8')

cnt = 0

for line in f:
    rendered = ''

    #remove --engine neural if you don't want to use neural TTS (saves money, but more edges to tones)
    command = 'aws polly synthesize-speech --text-type ssml --engine neural --output-format "mp3" --voice-id "'+pollyvoice+'" --text "{0}" {1}'

    if '\n' == line:
        #A pause after a paragraph
        rendered = '<speak><break time="1200ms"/></speak>' #change this if you want less / more of a break between paragraphs
    else:
        #A pause after a sentence
        linestrip = line.strip()
        rendered = '<speak><amazon:effect name="drc">' + linestrip + '</amazon:effect></speak>'

    rendered = rendered.replace('"', '\\"')
    
    file_name = ' polly_out{0}.mp3'.format(u''.join(str(cnt)).encode('utf-8').decode('utf-8'))
    cnt += 1
    command = command.format(rendered.encode('utf-8').decode('utf-8'), file_name)
    print (command)
    subprocess.call(command, shell=True)

#Concatenates the audio files, one by one (to prevent an error with too many arguements)    
num_add = 0
while num_add < cnt:
    execute_command = 'cat polly_out' + str(num_add) + '.mp3 >> '+outputname
    subprocess.call(execute_command, shell=True)
    num_add += 1

#Removes the tempoary files
execute_command = 'rm polly_out*.mp3'
print ('Removing temporary files: ' + execute_command)
subprocess.call(execute_command, shell=True)

#Sends text alert that it is finished, if phone != "none"
if phone != "none":
    command = "aws sns publish --phone-number=+"+str(phone)+" --message=\"Audio Recording "+outputname+" finished.\""
    subprocess.call(command, shell=True)
