#include <iostream>
#include <string>
#include <map>
using namespace std;

bool PalindromePermutation(string s)
{
    map<char, int> stringMap; // create map to count number of each letter in string
    for (int i = 0; i < s.length(); i++) //iterate through string to add letter with count to map
    {
        if (stringMap.count(s[i]) == 0)
            stringMap[s[i]] = 1;
        else
            stringMap[s[i]]++;
    }
    bool foundOdd = false; //check if letter with odd count is found, if two or more odd counts, then not a palindrome
    map<char, int>::iterator it = stringMap.begin(); //iterate through map to check results
    for (it; it != stringMap.end(); it++) {
        cout << it->first << " " << it->second << endl; //print out map values while iterating
        if ((it->second % 2) == 1) { //if count is odd, checks if already had odd count and return false since not palindrome
            if (foundOdd == true)
                return false;
            else
                foundOdd = true; //set foundOdd to true since found an odd count
                continue;
        }
        else //even letter counts are ignored
            continue;
    }
    return true;
}

int main()
{
    string word = "tests"; //replace with word to test as palindrome
    bool test = PalindromePermutation(word);
    string result = "";
    if (test == false) {
        result = "\" is not a palindrome.";
    }
    else
        result = "\" is a palindrome.";
    cout << "Result: \"" << word << result << endl;
    return 0;
}