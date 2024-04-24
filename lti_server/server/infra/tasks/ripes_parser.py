import json
from functools import reduce

repls = ("\n", ""), ("    ", "")

def parse_ripes(output):
	out = output[output.find("Running")+46:output.find("Post-run")-64].replace('\x00','')
	regs = output[output.find("registers")-7:] 
	regs_json = json.loads(reduce(lambda a, kv: a.replace(*kv), repls, regs))
	return [out, regs_json]
