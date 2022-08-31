package com.company;

import java.util.Scanner;

public class FortuneTeller {

	public static void main(String[] args) {
		Scanner scnr = new Scanner(System.in);

		// asking user to enter an integer from 1-10
		System.out.print("Enter an integer from 1-10: ");
		int value1 = scnr.nextInt();

		// if input is invalid, will tell the user and give a refund
		if (value1 < 1){
			System.out.println("Invalid input, here's your money back");
			return;
		} else if (value1 > 10) {
			System.out.println("Invalid input, here's your money back");
			return;
		}
		// declaring the variables
		String expression;
		String expression_symbols;

		// if statements for different possible integers the user entered
		if (value1 == 1) {
			expression = "tongue in cheek";
			expression_symbols = ":-J";

		} else if (value1 == 2) {
			expression = "tongue tied";
			expression_symbols = ":-&";

		} else if (value1 == 3) {
			expression = "blushing";
			expression_symbols = "=^_^=";

		} else if (value1 == 4) {
			expression = "alarmed";
			expression_symbols = ":-o";

		} else if (value1 == 5) {
			expression = "laughing out loud";
			expression_symbols = "=-D";

		} else if (value1 == 6) {
			expression = "angry";
			expression_symbols = ">_<";

		} else if (value1 == 7) {
			expression = "in love";
			expression_symbols = "(*_*)";

		} else if (value1 == 8) {
			expression = "bored";
			expression_symbols = "(-_-)";

		} else if (value1 == 9) {
			expression = "annoyed";
			expression_symbols = ">_<*";

		} else{
			expression = "shy";
			expression_symbols = "(*^_^*)";
		}

		// asking user to enter a letter from A-I
		System.out.print("Enter a letter from A-I: ");
		String character = scnr.next().toUpperCase();

		// declaring the variables
		String character_expression;
		String character_symbols;

		// if statements for different possible letters the user enters
		if (character.equals("A")) {
			character_expression = "with a birthday hat on";
			character_symbols = "*<:)";

		} else if (character.equals("B")) {
			character_expression = "in bed";
			character_symbols = "0_";

		} else if (character.equals("C")) {
			character_expression = "with a rose";
			character_symbols = "@~)~~~~";

		} else if (character.equals("D")) {
			character_expression = "with your eyes closed";
			character_symbols = "<•>";

		} else if (character.equals("E")) {
			character_expression = "on an airplane";
			character_symbols = "-|–‘";

		} else if (character.equals("F")) {
			character_expression = "near the christmas tree";
			character_symbols = "*<<<<=";

		} else if (character.equals("G")) {
			character_expression = "getting a gift";
			character_symbols = "8[+]";

		} else if (character.equals("H")) {
			character_expression = "looking for a four leaf clover";
			character_symbols = "%%-";

		} else if (character.equals("I")) {
			character_expression = "riding a bicycle";
			character_symbols = "(*)/(*)";

		} else {
			// if input is invalid, tells the user and gives a refund
			System.out.println("Invalid character input, here's your money back.");
			return;
		}

		// asking user to input second integer from range of 1-11
		System.out.print("Enter an integer from 1-11: ");
		int value2 = scnr.nextInt();

		// if statements for if input is invalid, will tell the user
		if (value2 < 1) {
			System.out.println("Invalid input, here's your money back");
			return;
		} else if (value2 > 11) {
			System.out.println("Invalid input, here's your money back");
			return;
			}

		// declaring variables
		String expression2;
		String expression_symbols2;

		// if statements depending on which integer the user entered
		if (value2 == 1) {
			expression2 = ("and saw a bird.");
			expression_symbols2 = ("(*V*)");

		} else if (value2 == 2) {
			expression2 = ("and saw a cat.");
			expression_symbols2 = ("=^.^=");

		} else if (value2 == 3) {
			expression2 = ("and saw a dog.");
			expression_symbols2 = (":o3");

		} else if (value2 == 4) {
			expression2 = ("and saw a fish.");
			expression_symbols2 = ("<><");

		} else if (value2 == 5) {
			expression2 = ("and saw a mouse.");
			expression_symbols2 = ("<:3)~");

		} else if (value2 == 6) {
			expression2 = ("and saw a pig.");
			expression_symbols2 = ("=8)");

		} else if (value2 == 7) {
			expression2 = ("and saw a bee.");
			expression_symbols2 = (":(III)-");

		} else if (value2 == 8) {
			expression2 = ("and saw an owl.");
			expression_symbols2 = ("^o,o^");

		} else if (value2 == 9) {
			expression2 = ("and saw a penguin.");
			expression_symbols2 = ("( *)>");

		} else if (value2 == 10) {
			expression2 = ("and saw a rabbit.");
			expression_symbols2 = ("(‘.’)");

		} else {
			expression2 = ("and saw a snail.");
			expression_symbols2 = ("_@_v");
		}
		// telling the user their fortune in symbols and a sentencce
		System.out.println();
		System.out.println("I see " + expression_symbols + " " + character_symbols + " " + expression_symbols2);
		System.out.println("You are " + expression + " " + character_expression + " " + expression2);

	}

}