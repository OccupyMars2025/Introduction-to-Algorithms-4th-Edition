python:
	rm -rf ./graphviz
	mypy --check-untyped-defs tree_delete.py
	python tree_delete.py

cpp:
	rm -rf ./graphviz
	mkdir -p graphviz
	clang++-18 -std=c++17 tree_delete.cpp -lpthread
	./a.out


