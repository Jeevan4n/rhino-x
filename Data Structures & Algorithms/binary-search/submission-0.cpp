class Solution {
public:
    int search(vector<int>& ans, int target) {
        int low=0,high=ans.size()-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            if(ans[mid]==target){
                return mid;
            }
            if(ans[mid]>target){
                high=mid-1;
            }
            else{
                low=mid+1;
            }
        }
        return -1;
        
    }
};
