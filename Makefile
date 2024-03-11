dist/apt.py: apt.py
	pyinstaller --name apt.py apt.py

clean:
	rm -r dist build apt.py.spec
