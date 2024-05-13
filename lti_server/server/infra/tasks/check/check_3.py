import subprocess, os
import re, math
from .ripes_parser import parse_ripes

def check(student_id, condition):
	run1 = parse_ripes(subprocess.check_output("{d}/Ripes --appimage-extract-and-run --mode cli --src {d}/tmp_solution/{sid}_3.s -t asm --proc RV64_SS --regs --json -v".format(d=os.path.dirname(__file__), sid = student_id).split()).decode("utf-8"))	
	return "Для этого задания пока нет проверки"
	
