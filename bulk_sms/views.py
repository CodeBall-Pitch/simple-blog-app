from django.shortcuts import render
#from  .forms import TextForm
# Create your views here.
import africastalking
username = "techkiash"    
api_key = "ef5c9674d8423ab708659d6c38e0660c2edc993785cd9a1929497df5affc4179"
africastalking.initialize(username, api_key)

sms = africastalking.SMS
def SmsView(request):
    # textform = TextForm()
    if request.method=="POST":
        # textform=TextForm(request.POST)
        # if textform.is_valid():
        text=request.POST.get('message')
        phone_no=request.POST.get('phone')
        response = sms.send(text, [f"{phone_no}"])
        print(response)     
  
    return render(request,'bulk_sms/sms.html')

