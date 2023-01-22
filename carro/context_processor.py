def importe_total_carro(request):
    total=0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total=total+float(value["precio"])
        totalf = round(total, 2)
            

    else:
        totalf="Debes hacer login"
   
        
    return {"importe_total_carro":totalf}
    