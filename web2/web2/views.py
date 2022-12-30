from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render (request,'index.html')


def contact(request):
    return render (request,'contact.html')

def about(request):
    return render (request,'about.html')


def analyze(request):
    djtext=request.GET.get("text",'default')
    uppercase=request.GET.get('uppercase','off')
    lowercase=request.GET.get('lowercase','off')
    swapcase=request.GET.get('swapcase','off')
    title=request.GET.get('title','off')
   

    if uppercase=="on":
         djtext=djtext.upper()
         d={'analyzed':djtext,'purpose':'Upper case'}
        
         return render (request,'analyze.html',d )
 
    elif lowercase=="on":
        djtext= djtext.lower()
        d={'analyzed':djtext,'purpose':'Lower case'}
        return render (request,'analyze.html',d )

    elif swapcase=="on":
        djtext= djtext.swapcase()
        d={'analyzed':djtext,'purpose':'Swap case case'}
        return render (request,'analyze.html',d )

    elif title=="on":
        djtext= djtext.title()
        d={'analyzed':djtext,'purpose':'Title'}
        return render (request,'analyze.html',d )

    else:
        if len(djtext)<=0:
            s="You doesn't enter anything"
            d={'err':s}
            return render (request,'error.html',d)
        elif ( uppercase!="on" and  lowercase!="on" and swapcase!="on"):
             s="You doesn't select any operation"
             d={'err':s}
             return render (request,'error.html',d)
        
    

        
        #  d={'analyzed':djtext,'purpose':'lower case'}
       
    # return render (request,'analyze.html',d )

    # if swapcase=="on":
    #     djtext=djtext.swapcase()
        
    #     d={'analyzed':djtext,'purpose':'swapcase case'}
       
    # return render (request,'analyze.html',d )
    # if( uppercase!="on" and  lowercase!="on" and swapcase!="on"):
    #     return render (request,'error.html')
    # # return render (request,'analyze.html',d )


    
    
    
   


