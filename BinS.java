package binarybonus;

import java.util.Scanner;

public class BinS {
	
	public static void binary(int[] a, int start, int end) {
		if(start > end) {
			System.out.println("NONE");
			return;
		}
		if(start == end) {
			System.out.println(a[start]);
			return;
		}
		
		int mid = (start+end)/2;
		
		if(mid%2 == 0) {
			
			if(a[mid] == a[mid+1]) {
				binary(a, mid+2, end);
			}
			
			else {
				binary(a,start,mid);
			}
		}
		else if(mid%2 == 1) {
			
			if(a[mid] == a[mid-1]) {
				binary(a,mid+1,end);
			}
			
			else {
				binary(a,start,mid-1);
			}
		}
		
	}
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String input = scanner.nextLine();
		String[] strs = input.split(" ");
		int[] a = new int[strs.length];
		for(int i = 0; i < strs.length; i++) {
			a[i] = Integer.parseInt(strs[i]);
		} 
		binary(a,0,a.length-1);
	}

}
