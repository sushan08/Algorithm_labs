import unittest
from knapsack import bruteforce_01knapsack
from knapsack import bruteforce_fractional_knapsack, greedy_fractional_knapsack, dynamic_programming_knapsack


class TestKnapsack(unittest.TestCase):
    def test_knapsack_bruteforce(self):
        weights= [5, 2, 1, 3]
        profit= [15,6,3,6]
        capacity = 6
        maximum, solution= bruteforce_01knapsack(profit, weights, capacity)
        self.assertEqual(maximum, 18)
        self.assertEqual(solution, '1010')

        maximum_fractional, solution_fractional = bruteforce_fractional_knapsack(profit, weights, capacity)
        self.assertEqual(maximum_fractional,18)


    def test_kanpsack_greedy(self):
        weights= [5, 2, 1, 3]
        profit= [15,6,3,6]
        capacity = 6
        maximum= greedy_fractional_knapsack(profit, weights, capacity)
        self.assertEqual(maximum, 18)
   

    def test_knapsack_dynamic(self):
        weights= [5, 2, 1, 3]
        profit= [15,6,3,6]
        capacity = 6
        maximum=dynamic_programming_knapsack(profit, weights, capacity)
        self.assertEqual(maximum, 18)


if __name__=="__main__":
    unittest.main()