function moveR()
{
    ob = new Date()
    h = ob.getHours()
    m = ob.getMinutes()
    s = ob.getSeconds()
    cs = h + " : " + m + " : " + s
    document.relogio.value = cs
    setTimeout("moveR()",1000)
}