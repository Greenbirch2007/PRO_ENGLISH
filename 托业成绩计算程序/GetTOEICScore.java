import java.util.Scanner;

/**
 *@author movis
 */
public class GetTOEICScore {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        System.out.println("托业考试计算器\n");
        
        int w;
        int ls = 0;
        int rs = 0;
        System.out.println("请选择得到结果的方式（输入正确个数为1，输入错误个数为2）");
        w = in.nextInt();
        if(w == 1) {
            System.out.print("请输入听力的正确个数：");
            w = in.nextInt();
            ls = getListeningScore(w);
            System.out.print("请输入阅读的正确个数：");
            w = in.nextInt();
            rs = getReadingScore(w);
        }
        else if(w == 2) {
            System.out.print("请输入听力的错误个数：");
            w = in.nextInt();
            ls = getListeningScore(100-w);
            System.out.print("请输入阅读的错误个数：");
            w = in.nextInt();
            rs = getReadingScore(100-w);
        }
        
        if(ls != -1 && rs != -1) {
            System.out.println("\n您的成绩为：");
            System.out.println("阅读听力分数为："+ls);
            System.out.println("阅读部分分数为："+rs);
            System.out.println("总分为："+(ls+rs));
        }
        
        in.close();
    }
    
    //计算听力部分分数
    public static int getListeningScore(int a) {
        int score = 0;
        if(a >= 0 && a <= 6)
            score = 5;
        else if(a >= 7 && a <= 25)
            score = 5 + 5*(a-7);
        else if(a >= 26 && a<= 34)
            score = 110 + 5*(a-26);
        else if(a >= 35 && a <= 43)
            score = 160 + 5*(a-35);
        else if(a >= 44 && a <= 46)
            score = 210 + 5*(a-44);
        else if (a == 47)
            score = 230;
        else if(a >= 48 && a <= 52)
            score = 240 + 5*(a-48);
        else if(a >= 53 && a <= 55)
            score = 270 + 5*(a-53);
        else if(a >= 56 && a <= 58)
            score = 290 + 5*(a-56);
        else if(a >= 59 && a <= 63)
            score = 310 + 5*(a-59);
        else if(a >= 64 && a <= 66)
            score = 340 + 5*(a-64);
        else if(a >= 67 && a <= 69)
            score = 360 + 5*(a-67);
        else if(a >= 70 && a <= 76)
            score = 380 + 5*(a-70);
        else if(a >= 77 && a <= 79)
            score = 420 + 5*(a-77);
        else if(a >= 80 && a <= 82)
            score = 440 + 5*(a-80);
        else if(a >= 83 && a <= 90)
            score = 460 + 5*(a-83);
        else if(a >= 91 && a <= 100)
            score = 495;
        else
            score = -1;
        return score;
    }
    
    //计算阅读部分分数
    public static int getReadingScore(int a) {
        int score = 0;
        if(a >= 0 && a <= 15)
            score = 5;
        else if(a >= 16 && a <= 24)
            score = 10 + 5*(a-16);
        else if(a >= 25 && a <= 27)
            score = 60 + 5*(a-25);
        else if(a >= 28 && a <= 32)
            score = 80 + 5*(a-28);
        else if(a >= 33 && a <= 37)
            score = 110 + 5*(a-33);
        else if(a >= 38 && a <= 40)
            score = 140 + 5*(a-38);
        else if(a >= 41 && a <= 45)
            score = 160 + 5*(a-41);
        else if(a >= 46 && a <= 48)
            score = 190 + 5*(a-46);
        else if(a >= 49 && a <= 55)
            score = 210 + 5*(a-49);
        else if(a >= 56 && a <= 60)
            score = 250 + 5*(a-56);
        else if(a >= 61 && a <= 63)
            score = 280 + 5*(a-61);
        else if(a >= 64 && a <= 66)
            score = 300 + 5*(a-64);
        else if(a >= 67 && a <= 71)
            score = 320 + 5*(a-67);
        else if(a >= 72 && a <= 76)
            score = 350 + 5*(a-72);
        else if(a >= 77 && a <= 88)
            score = 380 + 5*(a-77);
        else if(a >= 89 && a <= 91)
            score = 445 + 5*(a-89);
        else if(a >= 92 && a <= 93)
            score = 465 + 5*(a-92);
        else if(a >= 94 && a <= 97)
            score = 480 + 5*(a-94);
        else if(a >= 98 && a <= 100)
            score = 495;
        else
            score = -1;
        return score;
    }

}
