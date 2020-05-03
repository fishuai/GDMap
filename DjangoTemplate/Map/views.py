import json
from django.shortcuts import render, redirect

from Map.utils import getLocation, getIsOpen, getOtherInfo, changeDataBaseById, changeExcelById


def showmarker(request):
    location = getLocation()
    context = {
        "location": location,
    }
    is_open_list = getIsOpen()
    name_list, open_time_list, note_list = getOtherInfo()

    return render(request, 'showMarkers.html', {
        "location": location,
        'is_open': json.dumps(is_open_list),
        'name': json.dumps(name_list),
        'open_time': json.dumps(open_time_list),
        'note': json.dumps(note_list),
    })


def ajax_add(request):
    i1 = int(request.GET.get("i1"))
    changeid = i1
    changeDataBaseById(changeid)
    changeExcelById(changeid)

    return redirect("/map/showmarker/")
