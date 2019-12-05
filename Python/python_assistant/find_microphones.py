import speech_recognition
for index, name in enumerate(speech_recognition.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))