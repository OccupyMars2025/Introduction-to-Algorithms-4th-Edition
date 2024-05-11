#pragma once

#include <iostream>
#include <random>
#include <vector>
#include <cassert>
#include <algorithm>

typedef std::vector<std::vector<int>> Matrix;


std::vector<int> generateRandomVectorWithDistinctValues(int size, int minValue, int maxValue);
std::vector<int> generateRandomVector(int size, int minValue, int maxValue);
void printVector(const std::vector<int>& a);
bool isSorted(const std::vector<int>& a);
void testSearchingAlgorithm(bool (*searchingMethod)(std::vector<int> const& vec, int x, int* index), std::string methodName);
void testSortingAlgorithm(void (*sortingMethod)(std::vector<int>& vec), std::string methodName);
Matrix generateRandomMatrix(int rows, int cols, int min, int max);
void printMatrix(Matrix const & matrix);