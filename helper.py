#!/usr/bin/env python3
import os
import re
import sys
import shutil
import traceback


def trophy_check(troph_abs):
	if os.path.isfile(troph_abs):
		with open(troph_abs, 'rb') as f:
			troph_data = f.read(3)
		if not troph_data == b'\xdc\xa2M':		
			return True
	else:
		raise Exception("Trophies are not present: " + troph_abs)

def extract_np(bind_abs):
	if not os.path.isfile(bind_abs):
		raise Exception("Bind file is missing: " + bind_abs)
	with open(bind_abs, 'rb') as f:
		data = f.read()
	np = data[0x84:0x90].decode()
	if not re.match('NPWR\d{5}_00', np):
		raise Exception("Invalid NP com ID. Check your bind file: " + bind_abs)
	return np

def replace_trophs(dec_troph_abs, troph_abs, np):
	if os.path.isfile(dec_troph_abs):
		if trophy_check(dec_troph_abs):
			raise Exception("Trophies are encrypted: {}. "
							"Was expecting unencrypted ones.".format(dec_troph_abs))
		print("Unencrypted trophies for {} from PS4 are present: {}."
			  "".format(np, dec_troph_abs))
		shutil.copyfile(dec_troph_abs, troph_abs)
		print("Replaced encrypted trophies.")
	else:
		raise Exception("Unencrypted trophies not present: " + dec_troph_abs)

def main():
	bind_abs = os.path.join(sys.argv[1], 'sce_sys', 'npbind.dat')
	troph_abs = os.path.join(sys.argv[1], 'sce_sys', 'trophy', 'trophy00.trp')
	np = extract_np(bind_abs)
	print(np)
	if trophy_check(troph_abs):
		print("Trophies are encrypted.")
		dec_troph_abs = os.path.join("trophy", "conf", np, "TROPHY.TRP")
		replace_trophs(dec_troph_abs, troph_abs, np)
	else:
		print("Trophies are already unencrypted.")

if __name__ == "__main__":
	try:
		os.chdir(os.path.dirname(sys.argv[1]))
	except OSError:
		pass
	try:
		main()
	except Exception as e:
		traceback.print_exc()
	input("\nPress enter to exit.")
