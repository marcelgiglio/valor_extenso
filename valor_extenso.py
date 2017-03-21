def splitNumberOnPotency(stg):
	#slpit number on parts of 3 digit inversed
	new=[]
	num = 3
	for start in (range(len(stg), 0, -num)):
  		if (start-num<0):
  			new.append(stg[0:start])
  		else:
  			new.append(stg[start-num:start])
	return new

###this function write the number on letters
def numToStr(num):
	###all words
	unidades = {
		'0': '',
		'1':'um',
		'2':'dois',
		'3':'três',
		'4':'quatro',
		'5':'cinco',
		'6':'seis',
		'7':'sete',
		'8':'oito',
		'9':'nove'
	}
	dez = {
		'10':'dez',
		'11':'onze',
		'12':'doze',
		'13':'treze',
		'14':'quatorze',
		'15':'quinze',
		'16':'dezesseis',
		'17':'dezesete',
		'18':'dezoito',
		'19':'dezenove'
	}
	dezenas = {
		'2':'vinte',
		'3':'trinta',
		'4':'quarenta',
		'5':'cinquenta',
		'6':'sessenta',
		'7':'setenta',
		'8':'oitenta',
		'9':'noventa'
	}
	centenas = {
		'1':'cento',
		'2':'duzentos',
		'3':'trezentos',
		'4':'quatrocentos',
		'5':'quinhentos',
		'6':'seiscentos',
		'7':'setecentos',
		'8':'oitocentos',
		'9':'novecentos'
	}
	pot_singular = [
		'',
		'mil',
		'milhão',
		'bilhão',
		'trilhão',
		'quatrilhão'
	]
	pot_plural = [
		'',
		'mil',
		'milhões',
		'bilhões',
		'trilhões',
		'quatrilhões'
	]
	strNum = str(num)
	intNum = int(num)
	stg = ''
	###zero needs special rule for it
	if (intNum == 0):
		stg = 'zero'
	else:
		###each three numbers have the same rules
		nums = splitNumberOnPotency(strNum)
		stgs=[]
		for idx, threeDigits in enumerate(nums):
			threeStg = ''
			#one hundred need special rule for it
			if (threeDigits == '100'):
				threeStg = 'cem'
			else:
				###first, we write two first digits
				decimalStg = ''
				decimal = int(threeDigits[-2:])
				if (decimal == 0):
					decimalStg = ''
				elif (decimal <= 9):
					decimalStg = unidades[str(decimal)]
				elif (decimal >= 10 and decimal <= 19):
					decimalStg = dez[str(decimal)]
				else:
					firstDigit = str(decimal)[:1]
					secondDigit = str(decimal)[-1:]
					decimalStg = dezenas[firstDigit]
					if (int(secondDigit)==0):
						pass
					else:
						decimalStg += ' e '
						decimalStg += unidades[str(decimal)[-1:]]
				###then, if there is three digit, we can append it
				if (int(threeDigits)>99):
					threeStg = str(centenas[threeDigits[0]])
					if (not decimal == 0):
						threeStg += ' e ' + decimalStg
				else:
					threeStg = decimalStg
			###now we localizate it on the propper potency
			if (int(threeDigits)>1):
				stgs.append(threeStg + ' ' + pot_plural[idx])
			elif(int(threeDigits)==1):
				stgs.append(threeStg + ' ' + pot_singular[idx])
			elif(int(threeDigits)==0):
				pass
		###Now join all three digit numbers
		if (stgs):
			first = True
			moreThenOnePotency = True if len(stgs)>1 else False
			for strThreeDigit in stgs:
				if (first):
					first = False
					###take off an extra space and 
					if (strThreeDigit[-1]==' '):
						strThreeDigit = strThreeDigit[:-1]
					###some necessary verbose
					if (int(strNum[-3:])<=100 and moreThenOnePotency):
						stg += 'e '
					stg += strThreeDigit
				else:
					#sabe rule for the rest of cases
					stg = strThreeDigit + ' ' + stg
	###return
	return stg

def numToCurrency (num):
	###split integer and cents parts
	stg = ''
	num = str(num)
	cent = int(num[-2:])
	if (len(num) > 2):
		inteiro = int(num[:-2])
	else:
		inteiro = 0
	###create cents string
	temCentavo = True
	if (cent == 0):
		temCentavo = False
	elif (cent == 1):
		stg = '%s centavo' %(numToStr(cent))
	else: 
		stg = '%s centavos' %(numToStr(cent))
	###create integer string and append cent
	if (inteiro == 0):
		pass
	else:
		if (temCentavo):
			stg = " e " + stg
		if(inteiro == 1):
			stg = '%s real%s' %(numToStr(inteiro), stg)
		else:
			if (str(inteiro)[:-7:-1] == "000000"):
				stg = '%s de reais%s' %(numToStr(inteiro), stg)
			else:
				stg = '%s reais%s' %(numToStr(inteiro), stg)
	###return
	return (stg)