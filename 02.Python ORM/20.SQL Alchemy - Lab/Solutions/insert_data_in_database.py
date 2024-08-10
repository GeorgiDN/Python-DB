from models import User, Order
from main import Session
from sqlalchemy import func, and_

##########################################################################################
# # Additional create more records and add into database
with Session() as session:
    data = [{"username": "jadamou0", "email": "cgascoyne0@wunderground.com"},
            {"username": "hriddoch1", "email": "qmatyasik1@mapy.cz"},
            {"username": "kmollitt2", "email": "nsleightholm2@cyberchimps.com"},
            {"username": "hritchings3", "email": "cflynn3@economist.com"},
            {"username": "wterrans4", "email": "tfylan4@jalbum.net"},
            {"username": "ghurd5", "email": "lcharsley5@lycos.com"},
            {"username": "scollister6", "email": "aheadings6@hp.com"},
            {"username": "ndewes7", "email": "cerangy7@newyorker.com"},
            {"username": "csurgeoner8", "email": "hbrendeke8@hc360.com"},
            {"username": "sdunlea9", "email": "ehuerta9@paginegialle.it"},
            {"username": "mmorsheada", "email": "sbogiea@usnews.com"},
            {"username": "ckloskab", "email": "gblinkhornb@npr.org"},
            {"username": "rgoodbanc", "email": "tolliverc@economist.com"},
            {"username": "jfanshawd", "email": "ghollingsheadd@sitemeter.com"},
            {"username": "kleverettee", "email": "lnannettie@cocolog-nifty.com"},
            {"username": "lmarlandf", "email": "rfianderf@e-recht24.de"},
            {"username": "cgiamettig", "email": "wsimpking@blogtalkradio.com"},
            {"username": "kmacandieh", "email": "boleaghamh@patch.com"},
            {"username": "dfroudei", "email": "jpryeri@4shared.com"},
            {"username": "fdelieuj", "email": "amaskreyj@phpbb.com"},
            {"username": "sbraizierk", "email": "ssawardk@statcounter.com"},
            {"username": "sarghentl", "email": "flanglandsl@youku.com"},
            {"username": "sbeaversm", "email": "glowndsm@csmonitor.com"},
            {"username": "jayren", "email": "bbanatn@hexun.com"},
            {"username": "stammadgeo", "email": "lrubinovo@google.com.hk"},
            {"username": "kdemarsp", "email": "dmatejkap@npr.org"},
            {"username": "ldunlopq", "email": "cocollopyq@altervista.org"},
            {"username": "rderyebarrettr", "email": "vdeaver@tumblr.com"},
            {"username": "kglentons", "email": "mmalkinsons@cornell.edu"},
            {"username": "apidgeleyt", "email": "jlindforst@hp.com"},
            {"username": "aelgaru", "email": "ibradtkeu@japanpost.jp"},
            {"username": "gfeaksv", "email": "carmfirldv@fotki.com"},
            {"username": "abrilonw", "email": "bgalvinw@homestead.com"},
            {"username": "tfugglesx", "email": "nkynmanx@infoseek.co.jp"},
            {"username": "nwhaleyy", "email": "hportaly@pinterest.com"},
            {"username": "pdoleyz", "email": "hsummerillz@prlog.org"},
            {"username": "cbrattell10", "email": "bdrawmer10@lulu.com"},
            {"username": "utreffrey11", "email": "tleftly11@bloomberg.com"},
            {"username": "cgetcliff12", "email": "pfearfull12@biblegateway.com"},
            {"username": "czaczek13", "email": "pbachman13@dropbox.com"},
            {"username": "ebaldacchi14", "email": "daish14@mail.ru"},
            {"username": "byurmanovev15", "email": "bsimoneau15@g.co"},
            {"username": "eradmer16", "email": "trosborough16@miibeian.gov.cn"},
            {"username": "ibenjamin17", "email": "wcluett17@themeforest.net"},
            {"username": "tlewtey18", "email": "bjakuszewski18@github.com"},
            {"username": "tfarland19", "email": "lmcilory19@whitehouse.gov"},
            {"username": "mglasby1a", "email": "ckoschke1a@cafepress.com"},
            {"username": "bdannett1b", "email": "lstanners1b@vimeo.com"},
            {"username": "pwallace1c", "email": "akershaw1c@squarespace.com"},
            {"username": "mklementz1d", "email": "nloker1d@elpais.com"},
            {"username": "dmcturlough1e", "email": "cpelman1e@linkedin.com"},
            {"username": "ndiggens1f", "email": "lluquet1f@tinyurl.com"},
            {"username": "fsoppeth1g", "email": "hfossick1g@wiley.com"},
            {"username": "tderisley1h", "email": "tburkin1h@mit.edu"},
            {"username": "robrollachain1i", "email": "mvannuccini1i@msu.edu"},
            {"username": "nhacon1j", "email": "jaustin1j@blogs.com"},
            {"username": "sdee1k", "email": "mbecerra1k@cpanel.net"},
            {"username": "mrucklesse1l", "email": "lrobilart1l@jigsy.com"},
            {"username": "apill1m", "email": "smcgoon1m@google.fr"},
            {"username": "abeldum1n", "email": "fmurrigan1n@addthis.com"},
            {"username": "vrimmer1o", "email": "bbronger1o@delicious.com"},
            {"username": "hcaldeiro1p", "email": "aolehane1p@github.io"},
            {"username": "wmonday1q", "email": "dcappineer1q@berkeley.edu"},
            {"username": "rcraighead1r", "email": "fstansby1r@bluehost.com"},
            {"username": "pyegorovnin1s", "email": "ctadgell1s@biblegateway.com"},
            {"username": "llead1t", "email": "ewalstow1t@aol.com"},
            {"username": "mconsadine1u", "email": "jricardon1u@fda.gov"},
            {"username": "atomasoni1v", "email": "jjanaszkiewicz1v@ustream.tv"},
            {"username": "vkelson1w", "email": "gtawn1w@4shared.com"},
            {"username": "ftant1x", "email": "ssumshon1x@wisc.edu"},
            {"username": "fafonso1y", "email": "kknott1y@wordpress.org"},
            {"username": "nbullene1z", "email": "wsaintpierre1z@alexa.com"},
            {"username": "bcham20", "email": "lgravenall20@360.cn"},
            {"username": "mzmitruk21", "email": "smcaulay21@rambler.ru"},
            {"username": "ccovington22", "email": "cnestoruk22@mapquest.com"},
            {"username": "rivamy23", "email": "rolford23@cloudflare.com"},
            {"username": "mvasyutin24", "email": "pmcbrearty24@biglobe.ne.jp"},
            {"username": "mlenthall25", "email": "nserchwell25@godaddy.com"},
            {"username": "zmcbean26", "email": "ejozwiak26@nasa.gov"},
            {"username": "vtidmarsh27", "email": "iwethers27@canalblog.com"},
            {"username": "ndeas28", "email": "rcalabry28@nbcnews.com"},
            {"username": "deaglestone29", "email": "dfotitt29@gmpg.org"},
            {"username": "omajor2a", "email": "ekennan2a@wordpress.org"},
            {"username": "fpane2b", "email": "tmantrip2b@is.gd"},
            {"username": "bfitzhenry2c", "email": "ewarman2c@boston.com"},
            {"username": "pglaserman2d", "email": "dpersehouse2d@paypal.com"},
            {"username": "aelflain2e", "email": "tthickett2e@newyorker.com"},
            {"username": "ttynan2f", "email": "agianolo2f@icq.com"},
            {"username": "jjakubovski2g", "email": "mgarroch2g@nature.com"},
            {"username": "hreims2h", "email": "lsnoden2h@home.pl"},
            {"username": "lbowering2i", "email": "ccrosier2i@seesaa.net"},
            {"username": "kjohantges2j", "email": "bquarrell2j@tinyurl.com"},
            {"username": "jdesousa2k", "email": "dmckerley2k@seattletimes.com"},
            {"username": "bdunhill2l", "email": "acheke2l@answers.com"},
            {"username": "gwakley2m", "email": "bimmings2m@360.cn"},
            {"username": "mbrandino2n", "email": "dfreake2n@de.vu"},
            {"username": "skleinert2o", "email": "cwintringham2o@youku.com"},
            {"username": "rpace2p", "email": "mblown2p@webnode.com"},
            {"username": "jwontner2q", "email": "dhourihan2q@samsung.com"},
            {"username": "aeddowes2r", "email": "mmaffini2r@unblog.fr"}]

    for d in data:
        user = User(
            username=d["username"],
            email=d["email"],
        )
        session.add(user)
    session.commit()

# Filter data
with Session() as session:
    users = session.query(User).where(User.username.startswith('a'))
    for u in users:
        print(u.username, u.email)

with Session() as session:
    users = session.query(User).filter(
        and_(func.length(User.username) >= 8, User.username.startswith('a'))
    )
    for u in users:
        print(u.username, u.email)

###########################################################################################
