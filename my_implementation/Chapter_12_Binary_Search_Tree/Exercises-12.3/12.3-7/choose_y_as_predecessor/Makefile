python:
	rm -rf ./graphviz
	mypy --check-untyped-defs choose_y_as_predecessor.py
	python choose_y_as_predecessor.py

cpp:
	rm -rf ./graphviz
	mkdir -p graphviz
	clang++-18 -std=c++17 choose_y_as_predecessor.cpp -lpthread
	./a.out


