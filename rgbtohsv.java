//An attempt to create RGB to HSV.
// I ended up having an error, something to do with references/pointers and arrays that I didn't understand.
public class HelloWorld{
     public static float max(float[] nums) {
        if (nums[0] > nums [1] && nums[0] > nums[2]) {
            return nums[0];
        }
        if (nums[1] > nums [0] && nums[1] > nums[2]) {
            return nums[1];
        }
        if (nums[2] > nums[0] && nums[2] > nums[1]) {
            return nums[2];
        }
        return 0;
     }
     public static float min(float[] nums) {
        if (nums[0] < nums [1] && nums[0] < nums[2]) {
            return nums[0];
        }
        if (nums[1] < nums [0] && nums[1]  < nums[2]) {
            return nums[1];
        }
        if (nums[2] < nums[0] && nums[2] < nums[1]) {
            return nums[2];
        }
        return 0; 
     }
     public static float[] rgb2hsv(float r,float g, float b) {
         float h;
         //Initializes h
         h=0;
         float s;
         float v;
         // Floats added to avoid operator precedence
         float x;
         float a;
         float hue;
         //Divides by 255 
         r=r/255;
         g=g/255;
         b=b/255;
         float[] rgbArray = {r,g,b};
         float mx= max(rgbArray);
         float mn= min(rgbArray);
         float df= mx-mn;
         if (mx == mn) {
            h=0; 
         }
         if (mx==r) {
            x=g-b;
            a=x/df+360;
            hue=a % 360;
            h=hue;
         }
         if (mx==g) {
            x=b-r;
            a=x/df+120;
            hue=a % 360;
            h=hue;
         }
         if (mx==b) {
            x=r-g;
            a=x/df+240;
            hue=a % 360;
            h=hue;
         }
         
         if(mx==0) {
             s=0;
         }
         else {
             s=df/mx;
         }
         v=mx;
         float[] hsvArray = {h,s,v};
         return hsvArray;
     }
     public static void main(String []args){
     float[] x=rgb2hsv(255, 255, 0);
     System.out.println(x);
     }
}
