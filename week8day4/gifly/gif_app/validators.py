import re
from django.core.exceptions import ValidationError
  
def check_splcharacter(test): 
 
    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
    
    if(string_check.search(test) == None): 
        pass
          
    else: 
        raise ValidationError