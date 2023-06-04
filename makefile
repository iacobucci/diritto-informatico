all: 
	python3 convert.py > notes.md
	pandoc --from=gfm --pdf-engine=xelatex --metadata-file=style.yml -H deeplists.tex --to=pdf notes.md -o notes.pdf
