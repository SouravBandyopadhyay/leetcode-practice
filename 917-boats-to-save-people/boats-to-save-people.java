class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);

        int left = 0, right = people.length - 1;
        int boat = 0;
        while (left <= right) {
            int sum = people[left] + people[right];
            if (sum <= limit) {
                left++;
            }

            right--;
            boat++;
        }
        return boat;

    }
}