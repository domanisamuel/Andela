// Question 2
// A function that can accept two strings as input and print the string with maximum length  in console.
// If two strings have the same length, then the function should print all strings line by line.

// include tests
// ===================================================================================
// Answer

//inputs
s1 = ''
s2 = ''

//function that accept two argumants (strings)
function Ethic (s1, s2) {
    // let's initialize our variables
    let sentence1 = this.s1
    let sentence2 = this.s2
    // create a condition to determine the longest string
    if (sentence1.length > sentence2.length) {
        console.log(sentence1) // outputs the longest string
    } else if (sentence1.length === sentence2.length) {
        // if the strings have same length, prints all strings line by line
        console.log(sentence1)
        console.log(sentence2)
    } else {
        console.log(sentence2) // outputs sentence2 incase sentence1 is shorter
    }
}

//call the function
Ethic(s1, s2) // output: wamnyonyez