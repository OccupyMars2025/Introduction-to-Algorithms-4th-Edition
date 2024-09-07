python:
	rm -rf ./graphviz
	mypy --check-untyped-defs recursive_tree_insert.py
	python recursive_tree_insert.py

cpp:
	rm -rf ./graphviz
	mkdir -p graphviz
	clang++-18 -std=c++17 recursive_tree_insert.cpp -lpthread
	./a.out


