var g = {}

var jt = function (query, seperator) {
  queryItems = query.split(seperator)
  for (
    var params = {}, i = 0, queryLen = queryItems.length;
    i < queryLen;
    i++
  ) {
    var param = queryItems[i].split('=')
    if ((1 == param.length && param[0]) || 2 == param.length)
      try {
        var key = rga(param[0] || ''),
          val = rga(param[1] || '')
        key in params
          ? Array.isArray(params[key])
            ? ic(params[key], val)
            : (params[key] = [params[key], val])
          : (params[key] = val)
      } catch (error) {
        var err = error,
          key = param[0],
          p = String(jt)
        err.args = [
          {
            key: key,
            value: param[1],
            query: query,
            method: sga == p ? 'unchanged' : p
          }
        ]
        tga.hasOwnProperty(key) || ht(err)
      }
  }
  return params
}

var Hia = /^[\w.]*$/
var rga = function (a) {
  return a && a.match(Hia) ? a : Hg(a)
}
var Hg = function (a) {
  return decodeURIComponent(a.replace(/\+/g, ' '))
}
function lt(a) {
  '?' == a.charAt(0) && (a = a.substr(1))
  return jt(a, '&')
}
var tga = {
  q: !0,
  search_query: !0
}

var ht = function (a, b, c, d) {
  console.log('Errors:::', '\na', a, '\nb+++++', b, '\nc++++', c, '\nd++++', d)
  // var e = g.Ia('yt.logging.errors.log')
  // e
  //   ? e(a, 'WARNING', b, c, d)
  //   : ((e = g.O('ERRORS', [])),
  //     e.push([a, 'WARNING', b, c, d]),
  //     Zs('ERRORS', e))
}
let sga = String(jt)
// g = {}
// global.window = {document: {createElementNS: () => {return {}} }}
// g.c = window
/**
 * Returns an object based on its fully qualified external name.  The object
 * is not found if null or undefined.  If you are using a compilation pass that
 * renames property names beware that using this function will not find renamed
 * properties.
 *
 * @param {string} name The fully qualified name.
 * @param {Object=} opt_obj The object within which to look; default is
 *     |goog.global|.
 * @return {?} The value (object or primitive) or, if not found, null.
 */
g.Ia = function (name, opt_obj) {
  console.log('Name: ', name, opt_obj)
  var parts = name.split('.')
  var cur = opt_obj || g.C
  for (var i = 0; i < parts.length; i++) {
    cur = cur[parts[i]]
    if (cur == null) {
      return null
    }
  }
  return cur
}

var Xi = function (a) {
  var b = [],
    c
  for (c in a) Vi(c, a[c], b)
  return b.join('&')
}

var Vi = function (a, b, c) {
  if (Array.isArray(b))
    for (var d = 0; d < b.length; d++) Vi(a, String(b[d]), c)
  else null != b && c.push(a + ('' === b ? '' : '=' + Gg(b)))
}

var Gg = function (a) {
  return encodeURIComponent(String(a))
}

var vA = {
  Nu: function (a, b) {
    a.splice(0, b)
  },
  nx: function (a) {
    a.reverse()
  },
  c2: function (a, b) {
    var c = a[0]
    a[0] = a[b % a.length]
    a[b % a.length] = c
  }
}

var coa = function (a) {
  a = a.split('')
  vA.nx(a, 52)
  vA.Nu(a, 3)
  vA.c2(a, 19)
  vA.Nu(a, 2)
  vA.c2(a, 7)
  vA.c2(a, 58)
  vA.nx(a, 80)
  vA.Nu(a, 2)
  vA.nx(a, 45)
  return a.join('')
}
/**
 * @param a url
 * @param b sp
 * @param c s
 */
var aD = function (a, b, c) {
  b = void 0 === b ? '' : b
  c = void 0 === c ? '' : c
  a = new g.wA(a, !0)
  a.set('alr', 'yes')
  c && ((c = coa(decodeURIComponent(c))), a.set(b, encodeURIComponent(c)))
  return a
}

g.wA = function (a, b) {
  this.u = a
  this.D = void 0 === b ? !1 : b
  this.C = this.path = this.B = ''
  this.i = {}
  this.url = ''
}
g.wA.prototype.set = function (a, b) {
  this.i[a] !== b && ((this.i[a] = b), (this.url = ''))
}

var joinQuery = function (obj) {
  result = []
  var i = 0
  for (var key in obj) {
    result.push(key + '=' + obj[key])
    i++
  }
  return result.join('&')
}
var buildLink = function (a) {
  var result = [a.u, joinQuery(a.i)]

  return result.join('&')
}
var encodeU = function (l) {
  // var url = l.split('?')
  // var params = url[1]
  // var a.u = url + '?'
  // var result = []
  a = new g.wA(lt(l), !0)
  for (var i = 0; i < params.length; i++) {
    a.set(a, encodeURIComponent(params[i]))
  }
  var res = buildLink(a)
  // url.push(result.join('&'))
  return res
}
let decipher = function (strData) {
  var data = lt(strData)
  if (!('s' in data) && !('sp' in data)) return strData.url
  // console.log(data)
  var decodedURL = decodeURI(data.url)

  let decipheredObject = aD(decodedURL, data.sp, data.s)
  let decipheredLink = buildLink(decipheredObject)
  console.log('\n****** DONE DECIPHERING *********** \n', decipheredLink)
  return decipheredLink
}

// let strData =
//   's=%3DU%3DUCDU7AWMvBghyjtDnD5_wazyjl1j8EncKauJPBGCje6AAiAomcfNn1hLwfDFBax1rYRZmMmGVRaSXn6_U_A3_wMXAJAhIgRE8JQ0qOwOWwOW&sp=sig&url=https://rr1---sn-p5qs7nzk.googlevideo.com/videoplayback%3Fexpire%3D1641307087%26ei%3DbwfUYdmmNcHigwPcwYW4Aw%26ip%3D35.199.51.57%26id%3Do-AEzVDR7D8suxLTgFddIEUNoH4IPl0VrJVRB2PLKtdqcu%26itag%3D251%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DHX%26mm%3D31%252C26%26mn%3Dsn-p5qs7nzk%252Csn-ab5szn7z%26ms%3Dau%252Conr%26mv%3Du%26mvi%3D1%26pl%3D20%26gcr%3Dus%26vprv%3D1%26mime%3Daudio%252Fwebm%26ns%3DHWjICQJ1Y2J_f6-C7ukUsoAG%26gir%3Dyes%26clen%3D4028084%26dur%3D224.721%26lmt%3D1636804163826548%26mt%3D1641284970%26fvip%3D6%26keepalive%3Dyes%26fexp%3D24001373%252C24007246%26c%3DWEB_REMIX%26txp%3D5532434%26n%3DrkmrG0hKBBYCgGEO%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%26lsig%3DAG3C_xAwRAIgaVL7pTGi1aJAsdNFDcLxWTwHlHn7hBJybU-9JnLB81QCIDfq3IEWyS8gVLpzLQI5oNFIFQIZKj5iTSAOcDnH8N_T'

// decipher(strData)
