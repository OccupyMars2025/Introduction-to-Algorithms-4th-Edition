python:
	rm -rf ./graphviz
	mypy --check-untyped-defs give_equal_priority_to_predecessor_and_successor.py
	python give_equal_priority_to_predecessor_and_successor.py

cpp:
	rm -rf ./graphviz
	mkdir -p graphviz
	clang++-18 -std=c++17 give_equal_priority_to_predecessor_and_successor.cpp -lpthread
	./a.out


