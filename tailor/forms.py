from django import forms
from .models import Contact , Male ,Female


GENDER_CHOICES =( 
    ("male", "male"), 
    ("female", "female"), 
 
) 






class commentForm(forms.ModelForm):


    gender = forms.ChoiceField(choices = GENDER_CHOICES, label="", initial='', widget=forms.Select(), required=True)
    checkbox = forms.BooleanField(
         required=False

        )
   
    class Meta:
        model = Contact
        fields = '__all__'


        widgets = {
                'name' : forms.TextInput(attrs={'placeholder' : 'name','required': 'true'}),
                'age' : forms.TextInput(attrs={'placeholder' : 'age','required': 'true'}),
                'address' : forms.TextInput(attrs={'placeholder' : 'address','required': 'true'}),
                'gender' : forms.TextInput( attrs={'placeholder' : 'gender','required': 'true'}),
                'number' : forms.TextInput(attrs={'placeholder' : 'number','required': 'true'}),
                'type' : forms.TextInput(attrs={'placeholder' : 'type','required': 'true'}),
                'fchest' : forms.TextInput(attrs={'placeholder' : 'chest','required': 'true'}),
                'order_date' : forms.TextInput(attrs={'placeholder' : 'order_date','required': 'true'}),
                'issue_date' : forms.TextInput(attrs={'placeholder' : 'issue_date','required': 'true'}),
        
        }
      


class maleForm(forms.ModelForm):
    
    class Meta:
        model = Male
        
       

        fields = '__all__'
        exclude = ['contact1']
        
        widgets = {
            'chest' : forms.TextInput(attrs={'placeholder' : 'chest'}),
            'neck' : forms.TextInput(attrs={'placeholder' : 'neck'}) , 
            'full_shoulder_width': forms.TextInput(attrs={'placeholder' : 'full_shoulder_width'}) ,
            'right_sleeve' : forms.TextInput(attrs={'placeholder' : 'right_sleeve'}),
            'left_sleeve': forms.TextInput(attrs={'placeholder' : 'left_sleeve'}) ,
            'bicep' : forms.TextInput(attrs={'placeholder' : 'bicep'}),     
            'arm_length' : forms.TextInput(attrs={'placeholder' : 'arm_length'}),
            'wrist' : forms.TextInput(attrs={'placeholder' : 'wrist'}),
            'hip' : forms.TextInput(attrs={'placeholder' : 'hip'}),
            'sleeve_length' : forms.TextInput(attrs={'placeholder' : 'sleeve_length'}),
            'full_back_length' : forms.TextInput(attrs={'placeholder' : 'full_back_length'}),
            'biceps' : forms.TextInput(attrs={'placeholder' : 'biceps'}),
            'seat' : forms.TextInput(attrs={'placeholder' : 'seat'}),
            'thigh' : forms.TextInput(attrs={'placeholder' : 'thigh'}),
            'waist' : forms.TextInput(attrs={'placeholder' : 'waist'}),
            'shoulder_width' : forms.TextInput(attrs={'placeholder' : 'shoulder_width'}),
            'front_chest_width' : forms.TextInput(attrs={'placeholder' : 'front_chest_width'}),
            
            }



      
        

class femaleForm(forms.ModelForm):
    class Meta:
        model = Female
        fields = '__all__'

        exclude = ['contact2']

        widgets = {

                'fchest' : forms.TextInput(attrs={'placeholder' : 'chest'}),
                'fneck' : forms.TextInput(attrs={'placeholder' : 'fneck'}),
                'seat' : forms.TextInput(attrs={'placeholder' : 'seat'}),
                'fwaist' : forms.TextInput(attrs={'placeholder' : 'fwaist'}),
                'shoulder_width' : forms.TextInput(attrs={'placeholder' : 'shoulder_width'}),
                'arm_length' : forms.TextInput(attrs={'placeholder' : 'arm_length'}),
                'wrist' : forms.TextInput(attrs={'placeholder' : 'wrist'}),
                'hip' : forms.TextInput(attrs={'placeholder' : 'hip'}),
                'sleeve_length' : forms.TextInput(attrs={'placeholder' : 'sleeve_length'}),
                'arm_hole' : forms.TextInput(attrs={'placeholder' : 'arm_hole'}),
                'fneck' : forms.TextInput(attrs={'placeholder' : 'fneck'}),
                'bust' : forms.TextInput(attrs={'placeholder' : 'bust'}),
                'upper_bust' : forms.TextInput(attrs={'placeholder' : 'upper_bust'}),
                'skirt_length' : forms.TextInput(attrs={'placeholder' : 'skirt_length'}),
                'shoulder_to_shoulder' : forms.TextInput(attrs={'placeholder' : 'shoulder_to_shoulder'}),
                'full_back_length' : forms.TextInput(attrs={'placeholder' : 'full_back_length'}),
                'biceps' : forms.TextInput(attrs={'placeholder' : 'biceps'}),
                'back_length' : forms.TextInput(attrs={'placeholder' : 'back_length'}),
 
            
        }
