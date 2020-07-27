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
		raise Exception("Bind file is not present: " + bind_abs)
	pos = 0
	nps = []
	with open(bind_abs, 'rb') as f:
		data = f.read()
		while True:
			pos = data.find(b'\x10\x00\x0c', pos)
			if pos == -1:
				break
			pos += 3
			f.seek(pos)
			try:
				np = f.read(12).decode()
			except UnicodeDecodeError:
				raise Exception("Failed to decode NP ID. Check your bind file: " + bind_abs)
			if not re.match('NPWR\d{5}_00', np):
				raise Exception("Invalid NP ID. Check your bind file: " + bind_abs)
			nps.append(np)
	if not nps:
		raise Exception("Could not find any NP IDs. Check your bind file: " + bind_abs)
	return nps

def replace_trophs(un_troph_abs, troph_abs):
	if os.path.isfile(un_troph_abs):
		if trophy_check(un_troph_abs):
			raise Exception("Trophies are encrypted: {}. "
							"Was expecting unencrypted ones.".format(un_troph_abs))
		print("Unencrypted trophies are present: " + un_troph_abs)
		shutil.copyfile(un_troph_abs, troph_abs)
		print("Replaced encrypted trophies.")
	else:
		raise Exception("Unencrypted trophies not present: " + un_troph_abs)

def main():
	bind_abs = os.path.join(sys.argv[1], 'sce_sys', 'npbind.dat')
	nps = extract_np(bind_abs)
	total = len(nps)
	if total > 1:
		print("Game uses more than one trophy file.")
	for num, np in enumerate(nps):
		print(np)
		troph_abs = os.path.join(sys.argv[1], 'sce_sys',
								'trophy', 'trophy{}.trp'.format(str(num).zfill(2)))
		if trophy_check(troph_abs):
			print("Trophies are encrypted.")
			un_troph_abs = os.path.join('trophy', 'conf', np, 'TROPHY.TRP')
			replace_trophs(un_troph_abs, troph_abs)
		else:
			print("Trophies are already unencrypted.")

if __name__ == "__main__":
	try:
		os.chdir(os.path.dirname(sys.argv[1]))
	except OSError:
		pass
	try:
		main()
	except Exception:
		traceback.print_exc()
	input("\nPress enter to exit.")