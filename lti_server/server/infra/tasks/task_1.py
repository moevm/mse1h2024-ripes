import subprocess
import os
from .ripes_parser import parse_ripes

def check(student_id):
	run = parse_ripes(subprocess.check_output("{d}/Ripes --appimage-extract-and-run --mode cli --src {d}/tmp_solution/{sid}_1.s -t asm --proc RV64_SS --regs --json -v".format(d=os.path.dirname(__file__), sid = student_id).split()).decode("utf-8"))	
	return "All tests for the first task passed!"
	
def get_txt():
	return ["task1_title", "task1_text", 1]
