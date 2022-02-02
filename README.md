
# Luna23 CLI    

Encrypts and decrypts texts entered for/in luna23 encryption format. It was created to automate the boring character replacement task.



## Installation 

You can install the repository with:

```bash 
  $ git clone https://github.com/luizguilhermegzg/luna23_commandLine.git
  $ cd ./luna23_commandLine
  $ pip install -e . 
```
    
## Deployment

To run the program type in terminal:

```bash
  $ luna23
```
Then after that you should see something like that:

```bash
───────────────────────────────────────
YOU NEED TO PASS A VALID ARGUMENT LIKE:
encrypt
decrypt
info
────────────────────────────────────────
```

You have tree choices of arguments: encrypt, decrypt and info. Who you can type like that:

```bash
  $ luna23 encrypt
```
```bash
  $ luna23 decrypt
```
```bash
  $ luna23 info
```
The sequence after pass encrypt or decrypt like arguments are very similar. For example:
```bash
  $ luna23 encrypt
  INPUT: (here you type something, for example: HELLO WORLD)

  OUTPUT: POXXS QSJXH
  ────────────────────────────────────────
```
Another example now but passing decrypt like argument:
```bash
  $ luna23 decrypt
  INPUT: )here you type something, for example: POXXS QSJXH)

  OUTPUT: HELLO WORLD
  ────────────────────────────────────────
```
In the first example the text entered by the user was encrypted, in the second example the text was decrypted. And for the final example, we have:
```bash
  $ luna23 info

────────────────────────────────────────────────────────────────────────────────
Name: Luna23 Command Line Interface
Version: 0.1.0
Description: Program created to encrypt and decrypt texts in luna23 format
Created by: Luiz Guilherme Costa da Silva
Special thanks to my girlfriend who came up with the idea. Love you!
────────────────────────────────────────────────────────────────────────────────

```
## FAQ

#### What is Luna23?

Luna 23 is an encryption system created by a Russian rocket engineer named Boris Stravinsky. This system was first used in World War II by the Soviet Union in order to convey safer messages to its soldiers.
#### Why Luna23 is called Luna23?

The answer is simple. This was the name of one of the Soviet communist rockets that were trying to reach the moon at the time.
#### Ok, but what is the real history behind Luna23?

Well, it's even simpler. My girlfriend thought it would be cool if we had an encryption system of our own. And about the name, it's also simple, it's just literally the first two letters of mine and the last two of hers. The 23 in the name comes from the logic behind it all.

#### What logic?

Men, that's really hard to explain, but i will try my best:

We have 26 letters in our alphabet, right? The system is based on taking the position of each letter eg A which is 1 and multiplying either by 2 or by 3 depending on whether the position number is odd or even. So being A in position 1, and 1 being an odd number, we multiply by 3, obviously resulting in 3, which in this case would be position 3 or letter C. Finally, we have A = C.

Okay, but what if we have a letter where multiplying its position results in a number > 26, for example the letter O which is in position 15 and its multiplication by 3 results in 45. In this case we will go to the last letter of the alphabet (Z) with the number 26 in mind, then we'll return the first letter of the alphabet (A) and start to move up and add 1, until we get to 45, after we get to position 45, we'll see which letter references it, in this case Y, and so would replace.

IMPORTANT NOTE: if we go back to the beginning of the alphabet and count to such a position that it came from the result of n * 2 or 3, and end up reaching the end of the alphabet again without reaching the result, we go back to the beginning again and pick up where we left off counting.


  
## Authors

- [@luizguilhermegzg](https://github.com/luizguilhermegzg)

  
## Feedback

If you have any feedback, please reach out to us at luiz.developer@gmail.com

  
## License

[MIT](https://choosealicense.com/licenses/mit/)
