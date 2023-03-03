import java.util.*;
class prime2
{
	public static void main (String args[])
	{
		int i,n,temp;
		boolean isprime=true;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter number=");
		n=sc.nextInt();
			
		for(i=2;i<n;i++)
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
}