def splitNumber(stg, num):
	new=[]
	for start in (range(len(stg), 0, -num)):
  		if (start-num<0):
  			new.append(stg[0:start])
  		else:
  			new.append(stg[start-num:start])
	return new

def numToStr(num):
	###banco de palavras
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
		'6':'seisentos',
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
	if (int(num) == 0):
		stg = 'zero'
	else:
		num = str(num)
		nums = splitNumber(num, 3)
		stgs=[]
		for idx, threeDigits in enumerate(nums):
			stg = ''
			if (threeDigits == '100'):
				stg = 'cem'
			else:
				decimal = int(threeDigits[-2:])
				if (decimal <= 9):
					stg = unidades[str(decimal)]
				elif (decimal >= 10 and decimal <= 19):
					stg = dez[str(decimal)]
				else:
					firstDigit = str(decimal)[:1]
					secondDigit = str(decimal)[-1:]
					stg = dezenas[firstDigit]
					if (int(secondDigit)==0):
						pass
					else:
						stg += ' e '
						stg += unidades[str(decimal)[-1:]]
				if (int(threeDigits)>99):
					print ((threeDigits[0]))
					stg = str(centenas[threeDigits[0]]) + ' e ' + stg
			if (int(threeDigits)>1):
				stgs.append(stg + ' ' + pot_plural[idx])
			elif(int(threeDigits)==1):
				stgs.append(stg + ' ' + pot_singular[idx])
		stgs = stgs[::-1]
		if (stgs):
			stg = ' '.join(stgs)
	return stg

def numToCurrency (num):
	### separar centavos
	stg = ''
	num = str(num)
	cent = int(num[-2:])
	if (len(num) > 2):
		inteiro = int(num[:-2])
	else:
		inteiro = 0
	### criar stg de centavos
	if (cent == 0):
		pass
	elif (cent == 1):
		stg = ' e %scentavo.' %(numToStr(cent))
	else: 
		stg = ' e %scentavos.' %(numToStr(cent))
	### criar stg de parte inteira
	if (inteiro == 1):
		stg = '%s real%s' %(numToStr(inteiro), stg)
	elif(inteiro == 0):
		pass
	else:
		stg = '%s reais%s' %(numToStr(inteiro), stg)
	return (stg)

'''for i in range (90000, 100000):
	print ( str(i) + " - " + numToCurrency(i))
'''
print (numToCurrency(101000))
"""while True:
	print('coloque um número: ')
	print (numToCurrency(input()))"""