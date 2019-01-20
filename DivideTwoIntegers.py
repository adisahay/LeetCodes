class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        rem = 0
        quo = 0

        sign = "-" if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0 else ""
        dividend = abs(dividend)
        divisor = abs(divisor)

        for i in range(31, -1, -1):
            rem = (rem << 1) + ((dividend >> i) & 1)

            if rem < divisor:
                quo = quo << 1
                continue

            rem -= divisor
            quo = (quo << 1) + 1

        if quo == 2147483648 and sign is "-":
            return -2147483648
        elif quo >= 2147483647 and sign is "":
            return 2147483647

        return int(sign + str(quo))
