FILENAME = MarkovLang.g4
PREFIX = $(basename $(FILENAME))

all:
	java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor $(FILENAME) -o gen/

clean:
	rm -f gen/$(PREFIX)*.py gen/$(PREFIX)*.tokens gen/$(PREFIX)*.interp
