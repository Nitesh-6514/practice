import java.util.*;
class prime5
{
	public void check(int n)
	{
		int temp;
		boolean isprime=true;	
		for(int i=2;i<n;i++)
		{
				temp=n%i;
                  		            if(temp==0)
	        	           {
				isprime=false;
				break;
		           }
		}
		if(isprime)
		System.out.println(n+" is   prime number.");
		else
		System.out.println(n+" is  not prime number.");
		
	}
	public static void main(String args[])
	{
		prime5 p1=new prime5();
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter number.");
		int a=sc.nextInt();
		p1.check(a);
	}
}