from django.shortcuts import render, render_to_response
from django.views.decorators.clickjacking import xframe_options_exempt
from subprocess import Popen, PIPE
import re


# Create y;our views here.
@xframe_options_exempt
def status(request):
    p1 = Popen(["di","-I","rootfs", "-f mfp"], stdout=PIPE)
    di_status = p1.communicate()[0]
    out_list = di_status.splitlines()
    stat_lines = []
    for line in out_list:
       matchObj = re.match( r'.* +([0-9]+)%.*', line, re.M|re.I)
       if matchObj:
          stat_lines.append([matchObj.group(0),matchObj.group(1)])

    return render_to_response("server/status.html", dict(status = stat_lines) )

