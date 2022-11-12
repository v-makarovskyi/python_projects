from gtts import gTTS
import PyPDF2

pdf_file = open('/Users/vladimir/Downloads/python_modules.pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(pdf_file)
count = pdf_reader.numPages

textList = []

for i in range(count):
    try:
        page = pdf_reader.getPage(i)
        textList.append(page.extract_text())
    except:
        pass

textString = ''.join(textList)

language = 'en'

my_audio = gTTS(text=textString, lang=language, slow=False)
my_audio.save('audio.mp3')