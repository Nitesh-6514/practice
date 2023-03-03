import java.util.*;
class prime4
{
	public static void main(String args[])
	{
		
		int sum;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter your range= ");
		int n1=sc.nextInt();
		System.out.println("To ");
		int n2=sc.nextInt();
		for(int i=n1;i<=n2;i++)
		{
			 sum=0;
			for(int j=1;j<=i;j++)
			{
				if(i % j == 0)
				{
				   sum=sum+1;
				}
			}
			if(sum==2)
			{
			  System.out.println(i);
			}
			
		}
		
		
	}
}