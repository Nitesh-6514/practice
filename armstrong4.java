import java.util.*;
class armstrong4
{
	public static void main(String args[])
	{
		int num,start,end,i,rem,temp,count=0;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the start number=");
		start=sc.nextInt();
		System.out.println("Enter the end number=");
		end=sc.nextInt();
		sc.close();
			
		for(i=start;i<end;i++)
		{
			temp=i;
			num=0;
			while(temp>0)
			{
				rem=temp%10;
				num=num+rem*rem*rem;
				temp=temp/10;
			}
			if(i==num)
			System.out.println(i);
		}
		
	}
}
