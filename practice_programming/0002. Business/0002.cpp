#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

struct Project {
    int profit;
    int duration;
    int deadline;
};

bool compare_deadline(Project a, Project b) {
    return a.deadline < b.deadline;
}

int max_profit(vector<Project> &projects) {
    // Sort projects by their deadline
    sort(projects.begin(), projects.end(), compare_deadline);

    // Find the latest deadline
    int max_deadline = 0;
    for (auto &project : projects) {
        max_deadline = max(max_deadline, project.deadline);
    }

    // Initialize the DP array
    vector<int> dp(max_deadline + 1, 0);

    for (auto &project : projects) {
        // Update DP array backwards
        for (int t = project.deadline; t >= project.duration; --t) {
            dp[t] = max(dp[t], dp[t - project.duration] + project.profit);
        }
    }

    return *max_element(dp.begin(), dp.end());
}

int main() {
    int N;
    cin >> N;

    vector<Project> projects(N);
    for (int i = 0; i < N; ++i) {
        cin >> projects[i].profit >> projects[i].duration >> projects[i].deadline;
    }

    // Calculate and print the maximum profit
    cout << max_profit(projects) << endl;

    return 0;
}
