from pathlib import Path
import config
import os

import psycopg2
import psycopg2.extras

def password_change_config(new_password):
	BASE_DIR = Path(__file__).resolve().parent.parent
	targer_dir = f"{BASE_DIR}\config.py"

	file = Path(targer_dir)
	data = file.read_text()

	target_dbpassword = "DB_PASSWORD1"
	replace_data = new_password

	for item in data.split("\n"):
		if target_dbpassword in item:
			target_data = item.strip().split("=")[1].lstrip().strip("'")
			replace_item = item.replace(target_data, replace_data)
			data = data.replace(item, replace_item)
			
	file.write_text(data)



def password_change_config2(old_password):
	BASE_DIR = Path(__file__).resolve().parent.parent
	targer_dir = f"{BASE_DIR}\config.py"

	print("password 2 :::::::::::::::::::::::::::::", old_password)

	file = Path(targer_dir)
	data = file.read_text()

	target_dbpassword = "DB_PASSWORD2"
	replace_data = old_password

	for item in data.split("\n"):
		if target_dbpassword in item:
			target_data = item.strip().split("=")[1].lstrip().strip("'")
			replace_item = item.replace(target_data, replace_data)
			data = data.replace(item, replace_item)
			
	file.write_text(data)


def take_second_pass():
	BASE_DIR = Path(__file__).resolve().parent.parent
	targer_dir = f"{BASE_DIR}\config.py"

	file = Path(targer_dir)
	data = file.read_text()

	target_dbpassword = "DB_PASSWORD1"

	for item in data.split("\n"):
		if target_dbpassword in item:
			target_data = item.strip().split("=")[1].lstrip().strip("'")
	return target_data



def password_change_db(new_password):
	hostname = os.environ.get('DB_HOST')
	database = os.environ.get('DB_NAME')
	username = 'postgres'
	pwd = 'postgres'
	port_id =  os.environ.get('DB_PORT')
	conn = None

	try:
		with psycopg2.connect(
					host = hostname,
					dbname = database,
					user = username,
					password = pwd,
					port = port_id) as conn:

			with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

				cur.execute(f"ALTER USER {os.environ.get('DB_USERNAME')} PASSWORD '{new_password}'")
		# print("----------------------------------",os.environ.get('DB_PASSWORD1'))

		password_change_config2(take_second_pass())

	except Exception as error:
		password_change_config(os.environ.get('DB_PASSWORD2'))
	finally:
		if conn is not None:
			conn.close()

"""
import os

os.environ['DB_NAME'] = 'passchange_db'
os.environ['DB_USERNAME'] = 'username1'
os.environ['DB_PASSWORD1'] = 'password1'
os.environ['DB_PASSWORD2'] = 'password1'
os.environ['DB_HOST'] = '127.0.0.1'
os.environ['DB_PORT'] = '5432'

"""





