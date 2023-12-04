import PySimpleGUI as sg

layout= [
          [sg.Input(size=(18,1),key='display', justification='right')],
          [sg.Button('1'),sg.Button('2'),sg.Button("3"),sg.Button("/")],
          [sg.Button("4"),sg.Button("5"),sg.Button("6"),sg.Button("*")],
          [sg.Button("7"),sg.Button("8"),sg.Button("9"),sg.Button("-")],
          [sg.Button("0"),sg.Button("."),sg.Button("C"),sg.Button("+")],
          [sg.Button('=',size=(15,1))]
        ]


window =sg.Window('calculadora',layout,return_keyboard_events =True)


expresao =''
while True:
	event,value =window.read()
	if event == sg.WINDOW_CLOSED:
		break
	if event in '1234567890.+-*/C=':
		if event =="C":
			expresao =""
		elif event == '=':
			try:
				relsudado = eval(expresao)
				expresao = str(relsudado)
               
			except:
				expresao ="erro"
		else:
				expresao += event
		window['display'].update(expresao)
window.close()