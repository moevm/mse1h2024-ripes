from random import randint

def gen_task():
	text_var = ["большую", "меньшую"]
	p1 = randint(0, 1)
	p2 = randint(1, 10)
	return "На вход подается число в 10чной системе счисления(регистр t0). Необходимо посчитать количество нулей и единиц в его двоичной вариации. Ответом будет отношение большего к меньшему, округленного в {side} сторону до целого. Число: {num}. Если нулей нет, то ответ считать равным нулю. Полученный результат необходимо сохранить в регистре t1. Программа предназначена для 64-битных процессоров".format(side=text_var[p1], num = p2)

def get_txt():
	return ["Циклы", gen_task(), 2]

