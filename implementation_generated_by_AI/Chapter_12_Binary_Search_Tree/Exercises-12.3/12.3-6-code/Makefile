python:
	rm -rf ./graphviz
	mypy --check-untyped-defs bst.py
	python bst.py

cpp:
	rm -rf ./graphviz
	mkdir -p graphviz
	clang++-18 -std=c++17 bst.cpp -lpthread
	./a.out


