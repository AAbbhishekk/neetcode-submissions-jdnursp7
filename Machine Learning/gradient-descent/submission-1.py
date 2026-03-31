class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        for i in range(iterations):
            dw = 2*init
            init = init - dw*learning_rate

        return round(init,5)
    