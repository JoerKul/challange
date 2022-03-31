# challange

a programming exercise for devs

Task: You are given the following string, which represents a scrambled message:

150-177-154-156-149-223-157-144-197-223-214

The original message, also a string, was converted via the following steps:

1\. The string was converted to a UTF-8 byte array. Note: Only ASCII characters are included.

2\. Each element in the byte array was subtracted from 255, i.e. \`255 - element\`.

3\. Every two elements in the array were swapped, i.e. \`1,2,3,4,5\` became \`2,1,4,3,5\`.

4\. The elements were converted to strings and joined with \`-\`.

Your task is to decode the original message. Preferred language is C#, but using another language is also fine! For your convenience, a template is provided below:

Console.WriteLine(Decode("150-177-154-156-149-223-157-144-197-223-214"));

string Decode(string scrambled)  
{  
 // decode and return the message here  
  
}
