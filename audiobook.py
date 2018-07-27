# coding: utf-8
import subprocess
import codecs

inputfilename = "story.txt"
outputname = "Dracula-test.mp3"
pollyvoice = "Brian"

f = codecs.open(inputfilename, encoding='utf-8')

cnt = 0

for line in f:
    rendered = ''
    line = line.replace('"', '\\"')
    command = 'aws polly synthesize-speech --text-type ssml --output-format "mp3" --voice-id "'+pollyvoice+'" --text "{0}" {1}'

    if '\r\n' == line:
        #A pause after a paragraph
        rendered = '<speak><break time= "2s"/></speak>'
    else:
        #A pause after a sentence
        rendered = '<speak><amazon:effect name=\\"drc\\">' + line.strip() + '<break time=\\"1s\\"/></amazon:effect></speak>'
    
    file_name = ' polly_out{0}.mp3'.format(u''.join(str(cnt)).encode('utf-8'))
    cnt += 1
    command = command.format(rendered.encode('utf-8'), file_name)
    print command
    subprocess.call(command, shell=True)

num_add = 0

while num_add < cnt:
    execute_command = 'cat '+outputname+' polly_out' + str(num_add) + '.mp3 >> '+outputname
    subprocess.call(execute_command, shell=True)
    num_add += 1


execute_command = 'rm polly_out*.mp3'
print 'Removing temporary files: ' + execute_command
subprocess.call(execute_command, shell=True)
