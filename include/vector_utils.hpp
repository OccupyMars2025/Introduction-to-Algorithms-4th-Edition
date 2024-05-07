#pragma once

#include <iostream>
#include <random>
#include <vector>
#include <cassert>
#include <algorithm>

std::vector<int> generateRandomVector(int size, int minValue, int maxValue);
void printVector(const std::vector<int>& a);
bool isSorted(const std::vector<int>& a);
void testSearchingAlgorithm(bool (*searchingMethod)(std::vector<int> const& vec, int x, int* index), std::string methodName);
void testSortingAlgorithm(void (*sortingMethod)(std::vector<int>& vec), std::string methodName);
