from django.shortcuts import render, render_to_response

from subtitles import subtitles
# Create your views here.

def ruseng(request):
    file_name, out_ru,out_en = subtitles()
       #matchObj = re.match( r'.* +([0-9]+)%.*', line, re.M|re.I)

    return render_to_response("ruseng/ruseng.html", dict(rus = out_ru, eng = out_en, file_name = file_name) )

