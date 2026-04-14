class Solution {
    public int maxProfit(int[] prices) {
        int minB = prices[0];
        int maxP = 0;
        for (int i = 1; i < prices.length; i++) {
            minB = Math.min(minB, prices[i]);
            maxP = Math.max(maxP, prices[i] - minB);
        }
        return maxP;
    }
}
