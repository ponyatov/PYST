.PHONY: run all

run: bin/python ST.py
	./$^

.PHONY: deb
deb:
	sudo apt install -u gnu-smalltalk-browser

.PHONY: install update requirements.txt

.PHONY: merge release
MERGE  = Makefile .gitignore README.md
MERGE += ST.py ST.st
merge:
	git checkout master
	git checkout ponyatov -- $(MERGE)

NOW = $(shell date +%d%m%y)
REL = $(shell git rev-parse --short=4 HEAD)
release:
	git tag $(NOW)-$(REL)
	git push -v && git push --tags
	git checkout ponyatov
