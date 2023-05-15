calculator: main.o addition.o subtraction.o multiplication.o division.o
	cc -o calculator main.o addition.o subtraction.o multiplication.o division.o

main.o: main.c

$(objects): operations.h

objects = addition.o subtraction.o multiplication.o division.o

clean:
	rm -f $(objects) main.o

.PHONY: clean
