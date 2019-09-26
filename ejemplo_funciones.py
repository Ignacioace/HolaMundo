

#funciones con def

def function_tonta(nombre):
    separador = " "
    print(separador.join(("Wena", nombre)))
	
#llamamos a la funcion directamente

function_tonta("Fideo")

#calculo digito verificador

def digito_verificador(rut_sin_digito) :
	digito = ""
	multiplo = 0
	acumulador = 0
	contador = 2
	while rut_sin_digito > 0:
		multiplo = (rut_sin_digito % 10) * contador
		acumulador = acumulador + multiplo
		rut_sin_digito = rut_sin_digito // 10 #division entera
		contador = contador + 1
		if contador == 8:
			contador = 2
	digito = 11 - (acumulador % 11)
	if digito == 10:
		digito = 'K'
	if digito == 10:
		digito = 0
	return digito
	
mi_rut = 20433659
print("-".join((str(mi_rut), str(digito_verificador(mi_rut)))))	

#para terminar las cosas..
#git add ejemplo_funciones.py
#git commit -m "agregamos ejemplos de uso de funciones"
#git checkout master
#pull
#git merge dm_ejemplo_funciones
#git push
#git branch -d ia_ejemplo_funciones
