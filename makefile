all: 
	cd chapters; ls| grep .vml | sort --numeric-sort | xargs vml -m | pandoc --from=gfm --pdf-engine=xelatex --metadata-file=../style.yml -H ../deeplists.tex --to=pdf -o ../notes.pdf