from random import randint

def gen_task():
	p1 = randint(1, 20)
	p2 = randint(2, 4)
	p3 = randint(5, 7)
	return "На вход подается число {num1}(регистр t0). Необходимо вывести каждое {num2} и {num3} число от 0 до n. Программа предназначена для 64-битных процессоров. Пример вывода для каждого 4 и 7 числа от 0 до 11: [3,6,7,11]".format(num1=p1, num2=p2, num3=p3)

def get_txt():
	return ["Вывод в stdout", gen_task(), 3]

