/*
*** Min Cost Climbing Stairs ***

// You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
// Once you pay the cost, you can either climb one or two steps.
// You can either start from the step with index 0, or the step with index 1.
// Return the minimum cost to reach the top of the floor.

// Example 1:

// Input: cost = [10,15,20]
// Output: 15

// Explanation: You will start at index 1.
// - Pay 15 and climb two steps to reach the top.
// The total cost is 15.

// Example 2:

// Input: cost = [1,100,1,1,1,100,1,1,100,1]
// Output: 6

// Explanation: You will start at index 0.
// - Pay 1 and climb two steps to reach index 2.
// - Pay 1 and climb two steps to reach index 4.
// - Pay 1 and climb two steps to reach index 6.
// - Pay 1 and climb one step to reach index 7.
// - Pay 1 and climb two steps to reach index 9.
// - Pay 1 and climb one step to reach the top.
// The total cost is 6.

// Constraints:

// 2 <= cost.length <= 1000
// 0 <= cost[i] <= 999
*/
#include <vector>

class Solution
{
public:
    // O(n) - time | O(1) - space
    int minCostClimbingStairs(vector<int> &cost)
    {
        size_t numCosts{cost.size()};
        // Base cases
        int firstCost{cost.at(0)}, secondCost{cost.at(1)};

        // Key relationship:
        // At index i: minimumCost[i] = cost[i] + min(minimumCost(i-1), minimumCost(i-2));

        if (numCosts <= 2)
            return (firstCost < secondCost) ? firstCost : secondCost;

        int idx{2}, minCostAtIdx{0};
        while (idx < numCosts)
        {
            minCostAtIdx = cost[idx] + ((firstCost < secondCost) ? firstCost : secondCost);
            firstCost = secondCost;
            secondCost = minCostAtIdx;
            idx++;
        }
        return std::min(firstCost, secondCost);
    }
};