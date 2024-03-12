EXE=apt.py
DIST=dist/$(EXE)

$(DIST): apt.py
	pyinstaller --onefile --noconfirm --name $(EXE) $<

clean:
	rm -r dist build apt.py.spec
