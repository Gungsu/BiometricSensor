#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Funcoes do leitor de digital
Copyright (C) 2019 Amauri B. M. de Deus
MRD Engenharia
All rights reserved.

"""
import time
import sqlConect as sql
from pyfingerprint.pyfingerprint import PyFingerprint
import hashlib
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

f = None

def writeMsg(msg):
    arquivoTxt = open('/var/www/html/msg.txt', 'w')
    htmlinit = '<h2 style="color: #ff9900; text-align: center;">'
    htmlfinish = '</h2>'
    htmlMsg = htmlinit+msg+htmlfinish
    arquivoTxt.writelines(htmlMsg)
    arquivoTxt.close()

try:
    f = PyFingerprint('/dev/ttyS0', 57600, 0xFFFFFFFF, 0x00000000)

except Exception as e:
    writeMsg('Erro!')
    #print('Exception message: ' + str(e))
    exit(1)

def readFinger():
    global f
    global GPIO
    pnt = ['.','..','...']
    n = 0
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    while ( GPIO.input(13) == 0):
	if n <= 2:
		writeMsg("Aguardando"+str(pnt[n]))
		n += 1
	else: n = 0
	time.sleep(1)
        pass

    while ( f.readImage() == False ):
        pass

    f.convertImage(0x01)
    GPIO.cleanup()

def waitFinger():
    global f
    try:
        writeMsg('Aguardando digital...')
        readFinger()
        result = f.searchTemplate()

        positionNumber = result[0]
        accuracyScore = result[1]

        if ( positionNumber == -1 ):
            writeMsg('Não autorizado!')
            return False
        else:
            writeMsg('Bem vindo!')
            return True

        f.loadTemplate(positionNumber, 0x01)

    except Exception as e:
        writeMsg('Erro na leitura!Fwf')
        print('Exception message: ' + str(e))
        exit(1)

def addFinger():
    global f
    try:
        writeMsg('Aguardando nova digital...')

        readFinger()

        #Verificando se já existe cadastro
        result = f.searchTemplate()
        positionNumber = result[0]

        if ( positionNumber >= 0 ):
            writeMsg('Ja cadastrado')
            exit(0)

        writeMsg('Tire o dedo...')
        time.sleep(2)

        writeMsg('Coloque novamente...')

        ##Esperando nova leitura
        while ( f.readImage() == False ):
            pass

        f.convertImage(0x02)

        ## Comparando leituras
        if ( f.compareCharacteristics() == 0 ):
            writeMsg('Nao coincidiu!')
            raise Exception ('Nao coincidiu!')

        ## Adicionando cadastro
        f.createTemplate()

        ##Salvando cadastro
        positionNumber = f.storeTemplate()
        writeMsg('Cadastrado!')

    except Exception as e:
        writeMsg('Erro na leitura!')
        #print('Exception message: ' + str(e))
        exit(1)

def removeFinger(np):
    global f
    try:
        #numero da posicao
        np = int(np)

        if ( f.deleteTemplate(np) == True ):
            writeMsg('Digital removida')

    except Exception as e:
        writeMsg('Erro na leitura!')
        #print('Exception message: ' + str(e))
        exit(1)

def verModo():
    m = open('/var/www/html/modo.txt', 'r')
    modo = m.readline().split("\n")[0]
    m.close()
    return modo

def sqlSearch():
	global f
	modo = verModo()
	while modo == "leitura":
		try:
			if not waitFinger():
				temp = str(f.downloadCharacteristics(0x01)).encode('utf-8')
				cvtTsha = hashlib.sha256(temp).hexdigest()
				if sql.searchFdb(cvtTsha):
					writeMsg('Bem vindo!')
					f.createTemplate()
				else:
					writeMsg('Não autorizado')
			modo = verModo()
	        	if modo != "leitura":
				writeMsg('Digite seu id.')
			time.sleep(3)

		except Exception as e:
			writeMsg('Erro na leitura!Fss')
			#print('Exception message: ' + str(e))
			exit(1)

def sqlEnroll(id):
    global f
    try:
        if sql.verId(id):
            addFinger()
            temp = str(f.downloadCharacteristics(0x01)).encode('utf-8')
            cvtTsha = hashlib.sha256(temp).hexdigest()
            sql.addFingerDb(cvtTsha,id)
        else:
            writeMsg('ID inexistente!')

    except Exception as e:
        writeMsg('Erro na leitura!')
        #print('Exception message: ' + str(e))
        exit(1)
