def check(string):  
   
    string = string.lower()  
    vowel_1 = set("aeiou")  
   
    string_1 = set({})  
   
    for character_1 in string:  
   

        if character_1 in vowel_1 :  
            string_1.add(character_1)  
        else:  
            pass  
               
  
    if len(string_1) == len(vowel_1) :  
        print ("The string is Accepted")  
    else :  
        print ("The string is Not Accepted")  
   
 
if __name__ == "__main__" :  
       
    string = str (input ("Enter the String of characters: "))  
    check(string)  