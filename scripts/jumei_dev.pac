/* Last update: Wed Sep 12 18:10:00 2012 */
function FindProxyForURL(url, host) {
    if (isPlainHostName(host)) return "DIRECT";
    var H_114_112_69_252 = "PROXY 114.112.69.252:80";
    if(dnsDomainIs(host, "admin.koubei.jumei.com")) return H_114_112_69_252;
    if(dnsDomainIs(host, "koubeiman.int.jumei.com")) return H_114_112_69_252;
    if(dnsDomainIs(host, "koubei.jumei.com")) return H_114_112_69_252;
    if(dnsDomainIs(host, "images.jumei.com")) return "DIRECT";
    if(dnsDomainIs(host, "images2.jumei.com")) return "DIRECT";
    if(dnsDomainIs(host, ".corp.jumei.com")) return "DIRECT";
    if(dnsDomainIs(host, "mail.jumei.com")) return "DIRECT";
    if(dnsDomainIs(host, ".int.jumei.com")) return "DIRECT";
    if(dnsDomainIs(host, "tr.jumei.com")) return "DIRECT";
    var H_117_79_131_38 = "PROXY 117.79.131.38:80";
    if(dnsDomainIs(host, ".jumei.com")) return H_117_79_131_38;
    var H_192_168_25_9 = "PROXY 192.168.25.9:80";
    if(dnsDomainIs(host, "images.jumei.com")) return "DIRECT";
    if(dnsDomainIs(host, "images2.jumei.com")) return "DIRECT";
    if(dnsDomainIs(host, ".corp.jumei.com")) return "DIRECT";
    if(dnsDomainIs(host, "mail.jumei.com")) return "DIRECT";
    if(dnsDomainIs(host, ".jumeicd.com")) return H_192_168_25_9;
    return "DIRECT";
}
