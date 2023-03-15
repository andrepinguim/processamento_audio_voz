import speech_recognition as sr
import re

def obter_audio(microfone):
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
    return audio

def transformar_audio_em_texto(microfone, audio):
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        return frase
    except sr.UnknownValueError:
        print("Não entendi")


def escutar_microfone():
    microfone = sr.Recognizer()
    audio = obter_audio(microfone)
    texto =  transformar_audio_em_texto(microfone, audio)
    return texto


def realiza_calculo(texto):
    try:
        match = re.match(r"(-?\d+)\s+([+\-/]|mais|menos|vezes|x|[dividido por])\s+(-?\d+)", texto)

        if match:
            num1 = int(match.group(1))
            operador = match.group(2)
            num2 = int(match.group(3))
            
            if operador == "mais" or operador == "+":
                resultado = num1 + num2
            elif operador == "menos" or operador == "-":
                resultado = num1 - num2
            elif operador == "vezes" or operador == "x" or operador == "dividido por" or operador == "/":
                print("O algoritmo trata apenas as operações de Adição e Subtração")
                return
            
            print(f"Operação: {num1} {operador} {num2} = {resultado}")
        else:
            print("A entrada dos dados não é válida para o algoritmo.")
    except:
        print("A entrada dos dados não é válida para o algoritmo.")


if __name__ == '__main__':
    texto = escutar_microfone()
    print(f"A frase que você disse foi: {texto}")
    realiza_calculo(texto)