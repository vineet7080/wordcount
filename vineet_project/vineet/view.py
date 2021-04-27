
from django.shortcuts import render
def homepage(request):
    return render(request,'home.html')
def count(request):
    data= request.GET['fulltextarea']
    word_list=data.split()
    length=len(word_list)
    worddictionary={}
    for word in word_list:
         if word in worddictionary:
             worddictionary[word]+=1
         else:
             worddictionary[word]=1

    return render(request,'count.html',{'fulltextarea':data,'word':length,'worddictionary':worddictionary.items()})
def about(request):
    return render(request,'about.html')