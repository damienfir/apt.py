PREFIX=${HOME}/.local
EXE=dist/apt.py/apt.py

$(EXE): apt.py
	pyinstaller --name apt.py $<

clean:
	rm -r dist build apt.py.spec

install: $(EXE)
	cp $(EXE) $(PREFIX)/bin/
