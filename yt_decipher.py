__all__ = ['yt_decipher']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['Vi', 'aD', 'buildLink', 'Hia', 'decipher', 'ht', 'g', 'vA', 'Xi', 'sga', 'jt', 'Hg', 'rga', 'Gg', 'lt', 'strData', 'coa', 'tga'])
@Js
def PyJsHoisted_lt_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    ((Js('?')==var.get('a').callprop('charAt', Js(0.0))) and var.put('a', var.get('a').callprop('substr', Js(1.0))))
    return var.get('jt')(var.get('a'), Js('&'))
PyJsHoisted_lt_.func_name = 'lt'
var.put('lt', PyJsHoisted_lt_)
var.put('g', Js({}))
@Js
def PyJs_anonymous_0_(query, seperator, this, arguments, var=var):
    var = Scope({'query':query, 'seperator':seperator, 'this':this, 'arguments':arguments}, var)
    var.registers(['param', 'seperator', 'key', 'queryLen', 'p', 'query', 'i', 'val', 'params', 'err'])
    var.put('queryItems', var.get('query').callprop('split', var.get('seperator')))
    #for JS loop
    var.put('params', Js({}))
    var.put('i', Js(0.0))
    var.put('queryLen', var.get('queryItems').get('length'))
    while (var.get('i')<var.get('queryLen')):
        try:
            var.put('param', var.get('queryItems').get(var.get('i')).callprop('split', Js('=')))
            if (((Js(1.0)==var.get('param').get('length')) and var.get('param').get('0')) or (Js(2.0)==var.get('param').get('length'))):
                try:
                    var.put('key', var.get('rga')((var.get('param').get('0') or Js(''))))
                    var.put('val', var.get('rga')((var.get('param').get('1') or Js(''))))
                    ((var.get('ic')(var.get('params').get(var.get('key')), var.get('val')) if var.get('Array').callprop('isArray', var.get('params').get(var.get('key'))) else var.get('params').put(var.get('key'), Js([var.get('params').get(var.get('key')), var.get('val')]))) if var.get('params').contains(var.get('key')) else var.get('params').put(var.get('key'), var.get('val')))
                except PyJsException as PyJsTempException:
                    PyJsHolder_6572726f72_76184068 = var.own.get('error')
                    var.force_own_put('error', PyExceptionToJs(PyJsTempException))
                    try:
                        var.put('err', var.get('error'))
                        var.put('key', var.get('param').get('0'))
                        var.put('p', var.get('String')(var.get('jt')))
                        var.get('err').put('args', Js([Js({'key':var.get('key'),'value':var.get('param').get('1'),'query':var.get('query'),'method':(Js('unchanged') if (var.get('sga')==var.get('p')) else var.get('p'))})]))
                        (var.get('tga').callprop('hasOwnProperty', var.get('key')) or var.get('ht')(var.get('err')))
                    finally:
                        if PyJsHolder_6572726f72_76184068 is not None:
                            var.own['error'] = PyJsHolder_6572726f72_76184068
                        else:
                            del var.own['error']
                        del PyJsHolder_6572726f72_76184068
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('params')
PyJs_anonymous_0_._set_name('anonymous')
var.put('jt', PyJs_anonymous_0_)
var.put('Hia', JsRegExp('/^[\\w.]*$/'))
@Js
def PyJs_anonymous_1_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    return (var.get('a') if (var.get('a') and var.get('a').callprop('match', var.get('Hia'))) else var.get('Hg')(var.get('a')))
PyJs_anonymous_1_._set_name('anonymous')
var.put('rga', PyJs_anonymous_1_)
@Js
def PyJs_anonymous_2_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    return var.get('decodeURIComponent')(var.get('a').callprop('replace', JsRegExp('/\\+/g'), Js(' ')))
PyJs_anonymous_2_._set_name('anonymous')
var.put('Hg', PyJs_anonymous_2_)
pass
var.put('tga', Js({'q':Js(0.0).neg(),'search_query':Js(0.0).neg()}))
@Js
def PyJs_anonymous_3_(a, b, c, d, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'this':this, 'arguments':arguments}, var)
    var.registers(['d', 'b', 'a', 'c'])
    var.get('console').callprop('log', Js('Errors:::'), Js('\na'), var.get('a'), Js('\nb+++++'), var.get('b'), Js('\nc++++'), var.get('c'), Js('\nd++++'), var.get('d'))
PyJs_anonymous_3_._set_name('anonymous')
var.put('ht', PyJs_anonymous_3_)
var.put('sga', var.get('String')(var.get('jt')))
@Js
def PyJs_anonymous_4_(name, opt_obj, this, arguments, var=var):
    var = Scope({'name':name, 'opt_obj':opt_obj, 'this':this, 'arguments':arguments}, var)
    var.registers(['parts', 'cur', 'opt_obj', 'i', 'name'])
    var.get('console').callprop('log', Js('Name: '), var.get('name'), var.get('opt_obj'))
    var.put('parts', var.get('name').callprop('split', Js('.')))
    var.put('cur', (var.get('opt_obj') or var.get('g').get('C')))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('parts').get('length')):
        try:
            var.put('cur', var.get('cur').get(var.get('parts').get(var.get('i'))))
            if (var.get('cur')==var.get(u"null")):
                return var.get(u"null")
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('cur')
PyJs_anonymous_4_._set_name('anonymous')
var.get('g').put('Ia', PyJs_anonymous_4_)
@Js
def PyJs_anonymous_5_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'a', 'c'])
    var.put('b', Js([]))
    for PyJsTemp in var.get('a'):
        var.put('c', PyJsTemp)
        var.get('Vi')(var.get('c'), var.get('a').get(var.get('c')), var.get('b'))
    return var.get('b').callprop('join', Js('&'))
PyJs_anonymous_5_._set_name('anonymous')
var.put('Xi', PyJs_anonymous_5_)
@Js
def PyJs_anonymous_6_(a, b, c, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['d', 'b', 'a', 'c'])
    if var.get('Array').callprop('isArray', var.get('b')):
        #for JS loop
        var.put('d', Js(0.0))
        while (var.get('d')<var.get('b').get('length')):
            try:
                var.get('Vi')(var.get('a'), var.get('String')(var.get('b').get(var.get('d'))), var.get('c'))
            finally:
                    (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
    else:
        ((var.get(u"null")!=var.get('b')) and var.get('c').callprop('push', (var.get('a')+(Js('') if PyJsStrictEq(Js(''),var.get('b')) else (Js('=')+var.get('Gg')(var.get('b')))))))
PyJs_anonymous_6_._set_name('anonymous')
var.put('Vi', PyJs_anonymous_6_)
@Js
def PyJs_anonymous_7_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    return var.get('encodeURIComponent')(var.get('String')(var.get('a')))
PyJs_anonymous_7_._set_name('anonymous')
var.put('Gg', PyJs_anonymous_7_)
@Js
def PyJs_anonymous_8_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'a'])
    var.get('a').callprop('splice', Js(0.0), var.get('b'))
PyJs_anonymous_8_._set_name('anonymous')
@Js
def PyJs_anonymous_9_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    var.get('a').callprop('reverse')
PyJs_anonymous_9_._set_name('anonymous')
@Js
def PyJs_anonymous_10_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'a', 'c'])
    var.put('c', var.get('a').get('0'))
    var.get('a').put('0', var.get('a').get((var.get('b')%var.get('a').get('length'))))
    var.get('a').put((var.get('b')%var.get('a').get('length')), var.get('c'))
PyJs_anonymous_10_._set_name('anonymous')
var.put('vA', Js({'Nu':PyJs_anonymous_8_,'nx':PyJs_anonymous_9_,'c2':PyJs_anonymous_10_}))
@Js
def PyJs_anonymous_11_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    var.put('a', var.get('a').callprop('split', Js('')))
    var.get('vA').callprop('nx', var.get('a'), Js(52.0))
    var.get('vA').callprop('Nu', var.get('a'), Js(3.0))
    var.get('vA').callprop('c2', var.get('a'), Js(19.0))
    var.get('vA').callprop('Nu', var.get('a'), Js(2.0))
    var.get('vA').callprop('c2', var.get('a'), Js(7.0))
    var.get('vA').callprop('c2', var.get('a'), Js(58.0))
    var.get('vA').callprop('nx', var.get('a'), Js(80.0))
    var.get('vA').callprop('Nu', var.get('a'), Js(2.0))
    var.get('vA').callprop('nx', var.get('a'), Js(45.0))
    return var.get('a').callprop('join', Js(''))
PyJs_anonymous_11_._set_name('anonymous')
var.put('coa', PyJs_anonymous_11_)
@Js
def PyJs_anonymous_12_(a, b, c, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'a', 'c'])
    var.put('b', (Js('') if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('b')) else var.get('b')))
    var.put('c', (Js('') if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('c')) else var.get('c')))
    var.put('a', var.get('g').get('wA').create(var.get('a'), Js(0.0).neg()))
    var.get('a').callprop('set', Js('alr'), Js('yes'))
    (var.get('c') and PyJsComma(var.put('c', var.get('coa')(var.get('decodeURIComponent')(var.get('c')))),var.get('a').callprop('set', var.get('b'), var.get('encodeURIComponent')(var.get('c')))))
    return var.get('a')
PyJs_anonymous_12_._set_name('anonymous')
var.put('aD', PyJs_anonymous_12_)
@Js
def PyJs_anonymous_13_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'a'])
    var.get(u"this").put('u', var.get('a'))
    var.get(u"this").put('D', (Js(1.0).neg() if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('b')) else var.get('b')))
    var.get(u"this").put('C', var.get(u"this").put('path', var.get(u"this").put('B', Js(''))))
    var.get(u"this").put('i', Js({}))
    var.get(u"this").put('url', Js(''))
PyJs_anonymous_13_._set_name('anonymous')
var.get('g').put('wA', PyJs_anonymous_13_)
@Js
def PyJs_anonymous_14_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'a'])
    (PyJsStrictNeq(var.get(u"this").get('i').get(var.get('a')),var.get('b')) and PyJsComma(var.get(u"this").get('i').put(var.get('a'), var.get('b')),var.get(u"this").put('url', Js(''))))
PyJs_anonymous_14_._set_name('anonymous')
var.get('g').get('wA').get('prototype').put('set', PyJs_anonymous_14_)
@Js
def PyJs_anonymous_15_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['result', 'i', 'key', 'a'])
    var.put('result', Js([var.get('a').get('u')]))
    var.put('i', Js(0.0))
    for PyJsTemp in var.get('a').get('i'):
        var.put('key', PyJsTemp)
        var.get('result').callprop('push', ((var.get('key')+Js('='))+var.get('a').get('i').get(var.get('key'))))
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('result').callprop('join', Js('&'))
PyJs_anonymous_15_._set_name('anonymous')
var.put('buildLink', PyJs_anonymous_15_)
@Js
def PyJs_anonymous_16_(strData, this, arguments, var=var):
    var = Scope({'strData':strData, 'this':this, 'arguments':arguments}, var)
    var.registers(['data', 'decipheredLink', 'decodedURL', 'decipheredObject', 'strData'])
    var.put('data', var.get('lt')(var.get('strData')))
    if (var.get('data').contains(Js('s')).neg() and var.get('data').contains(Js('sp')).neg()):
        return var.get('strData')
    var.put('decodedURL', var.get('decodeURI')(var.get('data').get('url')))
    var.put('decipheredObject', var.get('aD')(var.get('decodedURL'), var.get('data').get('sp'), var.get('data').get('s')))
    var.put('decipheredLink', var.get('buildLink')(var.get('decipheredObject')))
    var.get('console').callprop('log', Js('\n****** DONE DECIPHERING *********** \n'), var.get('decipheredLink'))
    return var.get('decipheredLink')
PyJs_anonymous_16_._set_name('anonymous')
var.put('decipher', PyJs_anonymous_16_)
var.put('strData', Js('s=%3D%3D%3D%3DgQFdSTWqk8DkgiQnLIskrx64FGyHIpB6cEw8jlQtqW7AiAZqi5ZmjDj6sCNaO8Hb1Yh6wfPEz2GCPbYlxxIFw-kFJAhIQRB8JQ0qOwOrwOr&sp=sig&url=https://rr5---sn-p5qs7ned.googlevideo.com/videoplayback%3Fexpire%3D1640365113%26ei%3D2afFYYDtJNKI8wS6ro_AAQ%26ip%3D35.199.51.57%26id%3Do-AF-IvqB5MLQqT-xp0hNs2EUFmzksWa3Z6URk1g1yJ8tg%26itag%3D141%26source%3Dyoutube%26requiressl%3Dyes%26mh%3Da5%26mm%3D31%252C26%26mn%3Dsn-p5qs7ned%252Csn-ab5l6nsy%26ms%3Dau%252Conr%26mv%3Dm%26mvi%3D5%26pl%3D20%26ctier%3DA%26pfa%3D5%26gcr%3Dus%26initcwndbps%3D427500%26hightc%3Dyes%26vprv%3D1%26mime%3Daudio%252Fmp4%26ns%3Ds03Zgj_skOuIxjBXTK_2zvoG%26gir%3Dyes%26clen%3D7764855%26dur%3D241.173%26lmt%3D1591494671651115%26mt%3D1640343194%26fvip%3D5%26keepalive%3Dyes%26fexp%3D24001373%252C24007246%26c%3DWEB_REMIX%26txp%3D5431432%26n%3DsI0Mxv6YxkImmzXx%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cctier%252Cpfa%252Cgcr%252Chightc%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgLfT9N9lo9VC9cB--s-DkGXvABf9NmNDKZOzXoOWWsuoCIQC2ObYYHY_zrU0IVnxYoNf2IVrjxCwpWyoHElpzwiadFg%253D%253D'))
var.get('decipher')(var.get('strData'))


# Add lib to the module scope
yt_decipher = var.to_python()

